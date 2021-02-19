{% load vrouter %}

const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes: [ 
        {% vue_routes %}
    ]
})