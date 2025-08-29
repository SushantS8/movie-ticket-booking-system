from django.urls import path
from . import views

app_name = 'cinema'
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('showtime/<int:showtime_id>/', views.showtime_detail, name='showtime_detail'),
    path('book/<int:showtime_id>/', views.book_seats, name='book_seats'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
]
