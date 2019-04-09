from django.urls import path
from .views import UserViewSet

# from .filter import ArticleList


app_name = 'user'
urlpatterns = [
    path('userlist/', UserViewSet.as_view({'get': 'list_user'})), 
]


#get list of user and create user
       