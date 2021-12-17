from django.urls import path

from .views import UserProfileCreate, UserProfileList, UserProfileUpdate, RegisterAPIViewSet, LoginAPIViewSet

p = 'profile'
urlpatterns = [
    path('register/', RegisterAPIViewSet.as_view(), name='user_register'),
    path('login/', LoginAPIViewSet.as_view(), name='user_login'),
    # Profile
    path(f'{p}/create/', UserProfileCreate.as_view(), name='profile_create'),
    path(f'{p}/list/', UserProfileList.as_view(), name='profile_list'),
    path(f'{p}/update/<int:pk>/', UserProfileUpdate.as_view(), name='profile_update'),
    #

]
