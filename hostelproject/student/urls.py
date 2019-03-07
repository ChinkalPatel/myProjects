from django.conf.urls import url
from . import views
urlpatterns = [
    url('profile/', views.profile, name='profile'),
    url('canteen/', views.canteen, name='canteen'),
    url('complain/', views.complain, name='complain'),
    url('complainregister/', views.complainregister, name='complainregister'),
    url('changepassword/', views.changepassword, name='changepassword'),
    url('changepassworddone/', views.changepassworddone, name='changepassworddone'),
    url('mess/', views.mess, name='mess'),
    url('gatepass/', views.gatepass, name='gatepass'),
    url('gatepassregister/', views.gatepassregister, name='gatepassregister'),
    url('electricity/', views.electricity, name='electricity'),
    url('logout/',views.logout,name='logout'),
   
    ]
