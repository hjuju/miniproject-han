from member import views
from django.conf.urls import url


urlpatterns = [
    url(r'^register', views.members),
    url(r'^list', views.members),
    url(r'^login', views.member),
    url(r'^modify', views.member)


    # 바로옆에있는 view중 members라는 view를 찾아가라
]


