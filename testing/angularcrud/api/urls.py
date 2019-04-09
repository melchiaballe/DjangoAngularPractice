from django.urls import path
from .views import TodoViewSet

# from .filter import ArticleList


app_name = 'testing'
urlpatterns = [

    path('todo/' , TodoViewSet.as_view({'get':'get_Todo', 'post':'create_Todo'})),
    path('todo/<int:todo_id>/', TodoViewSet.as_view({'put':'update_Todo', 'delete':'delete_Todo'}))
#     path('movie/', TodoViewSet.as_view({'get': 'list_user', 'put': 'update_Movie', 'post':'create_Movie'})),
#     path('movie/<int:movie_id>/', TodoViewSet.as_view({'put': 'update_Movie', 'delete':'delete_Movie'})),
#     path('movie/mini/', TodoViewSet.as_view({'get': 'get_Movie_Title'})),
 ]


#get list of user and create user
       