from django.urls import path
from .views import blog_list,register,login_view,logout_view,create_blog,CreateBlogAPIView,BlogListAPIView,UserRegistrationAPIView,UserLoginAPIView,UserLogoutAPIView,delete_blog

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-blog/', create_blog, name='create_blog'),
    path('', blog_list, name='blog_list'),
    path('delete-blog/<int:id>/',delete_blog,name="delete_blog"),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user_registration_api'),
    path('api/login/', UserLoginAPIView.as_view(), name='user_login_api'),
    path('api/logout/', UserLogoutAPIView.as_view(), name='user_logout_api'),
    path('api/create_blog/', CreateBlogAPIView.as_view(), name='create_blog_api'),
    path('api/blog_list/', BlogListAPIView.as_view(), name='blog_list_api'),
]
