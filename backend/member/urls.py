from django.urls import path
from . import views

urlpatterns = [
    path('member/sign_up', views.member_list)
]
