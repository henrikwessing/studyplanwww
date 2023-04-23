from django.urls import path

from . import views

urlpatterns = [
    path('2023/', views.index, {"year": 2023},name='index'),
    path('', views.index, {"year":2022},name='index'),
    path('<str:flow_id>', views.flow, {"year":2022}, name = "Studieforløb årgang 2022"),
    path('2023/<str:flow_id>', views.flow, {"year":2023}, name = "Studieforløb årgang 2023")
]