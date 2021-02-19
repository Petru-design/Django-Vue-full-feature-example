from django.urls import path
from . import views
from .vuerouter import router

app_name = 'vuetest'

r = router.Router(appname='vuetest',
                  redirect_view=views.base_component)

# app.add_children(coaches, specifi_coach, register, request_messages)

r.register([views.App, views.TheHeader])

urlpatterns = [
    # path('', views.base_component),
    # path(r'components/TheHeader.vue', views.load_header, name='header'),
    path(r'components/CoachItem.vue', views.coach_item, name='coach_item'),

]

urlpatterns += r.get_urls()
