from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('pay_gate',views.payment,name='payment'),
    path('ticket',views.ticket,name='ticket'),
    path('notification/', views.notificationfrompaytm, name ='notification'),
    path('home',views.index,name='home')
   
]
