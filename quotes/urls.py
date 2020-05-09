from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="home"),
	path('about/',views.about,name="about"),
    path('add_stonk/',views.add_stonk,name='add'),
     path('delete/<stonk_id>',views.delete,name='delete')
]