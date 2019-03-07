from django.conf.urls import url
from . import views
urlpatterns = [
    url('index1/', views.index1, name='index1'),
    url('updateadmin/', views.updateadmin, name='updateadmin'),
    url('employee1/', views.employee1, name='employee1'),
    url('employee1remove/', views.employee1remove, name='employee1remove'),
    url('employee1add/', views.employee1add, name='employee1add'),
    url('student/', views.student, name='student'),
    url('studentremove/', views.studentremove, name='studentremove'),
    url('changepassword1/', views.changepassword1, name='changepassword1'),
    url('changepassworddone1/', views.changepassworddone1, name='changepassworddone1'),
    url('signout/', views.signout, name='signout'),
    
    ]