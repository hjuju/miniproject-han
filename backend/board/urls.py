from django.conf.urls import url
from .views import Boards as boards

urlpatterns = [
    url('postwrite', boards.as_view())

]
