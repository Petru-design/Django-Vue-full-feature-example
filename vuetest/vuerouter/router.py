from django.urls import path, reverse
import re
from django.shortcuts import render


class Router():
    def __init__(self, appname, redirect_view):
        self.app_name = appname
        self.routes = []
        self.redirect_view = redirect_view

    def register(self, routes=[]):
        self.routes = [r() for r in routes]

    def get_urls(self):
        urls = []

        for r in self.routes:
            urls += r.get_url()
            urls += r.get_redirect(redirect_view=self.redirect_view)

        return urls

    def get_vroute(self):
        paths = []
        for p in self.routes:
            paths.append(p.get_vroute(self.app_name))

        return ',\n'.join(paths)


class Route():
    route = {}
    redirect = ''

    vue_path = None
    vue_name = None
    pyhton_path = ''
    python_name = None
    template = None
    children = []
    add_route = True

    def __init__(self):
        self.children = [c() for c in self.children]

    def route_data(self):
        route = {'vue_path': self.vue_path,
                 'vue_name': self.vue_name,
                 'pyhton_path': self.pyhton_path,
                 'python_name': self.python_name,
                 'template': self.template,
                 'children': self.children,
                 'add_route': self.add_route}

        return route

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *children):
        for child in children:
            self.children.append(child)

    def get_url(self):
        view = self.view_funticon
        own = path(self.pyhton_path,
                   view,
                   name=self.python_name,)
        urls = []
        for c in self.children:
            urls += c.get_url()

        urls.append(own)
        return urls

    def get_redirect(self, parent=None, redirect_view=None):
        if self.add_route:
            children = self.children

            if parent:
                self.redirect = parent + "/" + self.vue_path
            else:
                self.redirect = self.vue_path[1:]

            urls = []
            for c in children:
                urls += c.get_redirect(parent=self.redirect,
                                       redirect_view=redirect_view)

            own = path(self.redirect, redirect_view)
            urls.append(own)
            return urls
        else:
            return []
        

    def get_vroute(self, appname=None):
        if self.add_route:
            url = ''
            children_list = self.children
            if appname:
                url = reverse(f"{appname}:{self.python_name}")
            else:
                url = reverse(self.python_name)

            children = ''
            for c in children_list:
                children += c.get_vroute(appname)

            vue_path = re.sub('<str(:.*)>', r'\1', self.vue_path)
            route = f"""{{path: '{vue_path}',
                        name: '{self.vue_name}',
                        component: () => loadModule(`{url}`, options), props: true,
                        children: [{children}]}},"""

            return route

        else:
            return ''

    def view_funticon(self, request):
        return render(request,
                      self.template,
                      context={})
