
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fnIndex),
    path('ass1',views.assginment1),
    path('ass2/',views.assginment2,name="ass2"),
    path('ass3',views.assginment3),
    path('ass4',views.assginment4),
    path('ass5',views.assignment5)
]
