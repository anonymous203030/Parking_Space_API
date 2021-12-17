from django.urls import path

from .views import CreateBookTimeAPIViewSet, BookTimeDetailsAPIViewSet, BookTimeListAPIViewSet, CreateReserveAPIVIewSet, \
    ListReserveAPIViewSet, DetailsReserveAPIViewSet

r = 'reserve'
urlpatterns = [
    path('create/', CreateBookTimeAPIViewSet.as_view(), name='create_book_time'),
    path('details/<int:pk>/', BookTimeDetailsAPIViewSet.as_view(), name='details_book_time'),
    path('list/', BookTimeListAPIViewSet.as_view(), name='list_book_time'),
    # Reserve
    path(f'{r}/create/', CreateReserveAPIVIewSet.as_view(), name='reserve_create'),
    path(f'{r}/list/', ListReserveAPIViewSet.as_view(), name='reserve_list'),
    path(f'{r}/details/<int:pk>/', DetailsReserveAPIViewSet.as_view(), name='reserve_details'),
]
