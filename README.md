# Django-Vue-full-feature-example
This is an example of a project combining Django and Vue in a full functional manner, getting all the functionalities from both. Works with Vuex and Vue-router as well.

This is not yet a full module/ project, but is is useful to offer an idea of how this two very powerfull frameworks ca work toghether with no limitations.

You can still use Django-rest in this setup, but it is not required. You can use the standard Django MCV. 

The setup is compatible for both Vue-router and Vuex. You can define paths and urls in a single place using a helper Router class, and the django urls and vue routes will be built for you. 

Using this setup, you can serve vue components as django templates, prerender them in django with model/vue/templete logic, and them have any frontend logic processed by Vue, without the need for Vue cli.

If you like this setup, or find it usefull, feel free to contribute, join discussions, or submit issues. Maybe we can build a full django reusable app.

Big thanks to FranckFreiburger for vue3-sfc-loader, which makes all of this work toghether
https://github.com/FranckFreiburger/vue3-sfc-loader

How it all works:

You will find mostly the standard Django setup, with the exception of a 'vuerouter' module. This module has some helper classes wich we will need to use.

Fist of all, we need an index.html page. There we import Vuejs and all other dependances (vue3-sfc-loader is required for this to work) using ormal '<script>' tags.
We set up a Vuejs app, but change the delimiters to '[[',']]', so it does not conflict with Django delimiters.

We then need to crate a Basic component to serve this index html, and process the redirect (if we use vue-router), which we can pass as a parameter to context.)

Now in urls.py we import our Router as 'from .vuerouter import router', and instantiate or base Router as
'r = router.Router(appname='vuetest',
                   redirect_view=views.base_component)'
                  
We then append to our urlpatterns the r.get_urls() (which returns a list of url patterns).
With this, the setup essentialy works.

To add extra components, you will need to create a view for each component, expanding the router.Route class, and providing the following parameters:
    
    vue_path - path you want to register to vue-router (Django will automatically redirect this path to index.html using our base component view). Leave blank if not needed
    vue_name - name to to register to vue-router, if you want to have redirects inside components
    pyhton_path - url pattern that will trigger the python view. When a component is loaded, vue3-sfc-loader will send a request to ./components/path/you/used/as/import/component/ComponentName.vue. So if I have iside my App.vue somethimg like "import TheHeader from './TheHeader.vue'" the resulting request will go to -> 'components/TheHeader.vue', and this is what will trigger a url pattern.
    python_name - name to be used for url pattern by Django
    template - path to actual component, as normal django template. As per above example: 'vuetest/components/layout/TheHeader.vue'
    add_route - Bool. Default True. Specify whether or not you want the component to be handeld by vue-router. You can import components directly iside other components, and might not need a specific route. In which case, you can set this to false.
    children - List of other Routes, to be processed as children handled by vue-router. 
    
If you have other components, you can register all top level components (components that are not children of other components) to the main Router in urls.py

At this point, you can just run the Django server, which will serve .vue files, and navigate to the pages provided to vue-router.
With this setup, you can use the .vue components as you would use with vue-cli, with the addition of normal django features.
