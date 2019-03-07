from django.conf.urls import url
from . import views
urlpatterns = [
    url('home/', views.index, name='index'),
    url('signup/',views.signup,name='signup'),
    url('sign/',views.sign,name='sign'),
    url('login/',views.login,name='login'),
    url('auth/',views.auth_view,name='auth_view'),
    url('contact/',views.contact,name='contact'),
    url('about/',views.about,name='about'),
    url('gallery/',views.gallery,name='gallery'),
   
    ]
