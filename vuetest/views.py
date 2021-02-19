from django.shortcuts import render
from .vuerouter import router
# from django.urls import reverse


def base_component(request, *args, **kwargs):

    redirect = request.build_absolute_uri()
    redirect = redirect.split("://")[1].split('/')
    redirect = "/".join(redirect[1:])
    redirect = "/" + redirect
    # redirect = None
    return render(request,
                  'vuetest/index.html',
                  context={'redirect': redirect,
                           })


class CoachList(router.Route):
    vue_path = '/coaches'
    vue_name = 'coaches'
    pyhton_path = 'components/CoachesList.vue'
    python_name = 'CoachesList'
    template = 'vuetest/pages/coaches/CoachesList.vue'


class CoachContact(router.Route):
    vue_path = 'contact'
    vue_name = 'contact'
    pyhton_path = 'components/CoacheContact.vue'
    python_name = 'CoacheContact'
    template = 'vuetest/pages/requests/CoacheContact.vue'


class CoachDetail(router.Route):
    vue_path = '/coaches/<str:id>'
    vue_name = 'specifiCoach'
    pyhton_path = 'components/CoacheDetail.vue'
    python_name = 'CoacheDetail'
    template = 'vuetest/pages/coaches/CoacheDetail.vue'

    children = [CoachContact]


class CoachesRegister(router.Route):
    vue_path = '/register'
    vue_name = 'register'
    pyhton_path = 'components/CoachesRegister.vue'
    python_name = 'CoachesRegister'
    template = 'vuetest/pages/coaches/CoachesRegister.vue'


class TheHeader(router.Route):
    vue_path = ''
    vue_name = ''
    pyhton_path = 'components/TheHeader.vue'
    python_name = 'header'
    template = 'vuetest/components/layout/TheHeader.vue'
    add_route = False


class RequestsRecieved(router.Route):
    vue_path = '/requests'
    vue_name = 'request'
    pyhton_path = 'components/RequestsRecieved.vue'
    python_name = 'RequestsRecieved'
    template = 'vuetest/pages/requests/RequestsRecieved.vue'


class App(router.Route):
    vue_path = '/'
    vue_name = 'app'
    pyhton_path = 'components/App.vue'
    python_name = 'App'
    template = 'vuetest/App.vue'

    children = [CoachList, CoachDetail, CoachesRegister, RequestsRecieved]

    def view_funticon(self, request):
        return render(request,
                      self.template,
                      context={})


class BaseCard(router.Route):
    pyhton_path = 'components/BaseCard.vue'
    python_name = 'base-card'
    template = 'vuetest/components/ui/BaseCard.vue'
    add_route = False


class BaseButton(router.Route):
    pyhton_path = 'components/BaseButton.vue'
    python_name = 'base-button'
    template = 'vuetest/components/ui/BaseButton.vue'
    add_route = False


class BaseBadge(router.Route):
    pyhton_path = 'components/BaseBadge.vue'
    python_name = 'base-badge'
    template = 'vuetest/components/ui/BaseBadge.vue'
    add_route = False


def load_component(request, name):
    print(name)
    color = 'blue'
    msg = 'mesage fom backend'
    if name in ['ChangeCounter', 'UserAuth']:
        template_path = f'vuetest/components/{name}.vue'
        print(template_path)
        return render(request,
                      template_path,
                      context={'color': color,
                               'msg': msg})


def coach_item(request):
    return render(request,
                  'vuetest/components/coaches/CoachItem.vue',
                  context={})
