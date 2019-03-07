from django.conf.urls import url
from . import views
urlpatterns = [
    url('profile/', views.profile, name='profile'),
    url('complainshow/',views.complainshow, name='complainshow'),
    url('changestatus/',views.changestatus, name='changestatus'),
    url('gatepass/',views.gatepass,name='gatepass'),
    url('gatepassallow/',views.gatepassallow,name='gatepassallow'),
    url('messdetail/',views.messdetail,name='messdetail'),
    url('messdetailadd/',views.messdetailadd,name='messdetailadd'),
    url('changepassword/',views.changepassword,name='changepassword'),
    url('changepassworddone/',views.changepassworddone,name='changepassworddone'),
    url('showcanteenitem/',views.showcanteenitem,name='showcanteenitem'),
    url('removecanteenitem/',views.removecanteenitem,name='removecanteenitem'),
    url('addcanteenitem/',views.addcanteenitem,name='addcanteenitem'),
    url('updatecanteenitem/',views.updatecanteenitem,name='updatecanteenitem'),
    url('electricitybill/',views.electricitybill,name='electricitybill'),
    url('electricitybillsend/',views.electricitybillsend,name='electricitybillsend'),
    url('logout/',views.logout,name='logout'),
    ]
