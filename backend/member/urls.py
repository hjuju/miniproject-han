from django.conf.urls import url
from django.urls import path, include
from .views import Members as members
from .views import Member as member
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('/signup', members.as_view()),
    path('/login/<str:pk>/', member.as_view())  #

    # 바로옆에있는 view중 members라는 view를 찾아가라
]

urlpatterns = format_suffix_patterns(urlpatterns)
