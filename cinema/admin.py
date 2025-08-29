from django.contrib import admin
from .models import Movie, Showtime, Seat, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','duration_min','rating')
    search_fields = ('title',)

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('id','movie','start_time','auditorium','rows','cols','price_cents')
    list_filter = ('movie','auditorium','start_time')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id','showtime','row_label','col_number','is_booked')
    list_filter = ('showtime','is_booked')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','user_name','user_phone','showtime','seat_row','seat_col','booked_at','status')
    list_filter = ('status','showtime')
