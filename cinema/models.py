from __future__ import annotations
from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration_min = models.PositiveIntegerField()
    rating = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    def __str__(self): return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    start_time = models.DateTimeField()
    auditorium = models.CharField(max_length=50)
    rows = models.PositiveIntegerField(default=8)
    cols = models.PositiveIntegerField(default=12)
    price_cents = models.PositiveIntegerField(default=45000)
    def __str__(self): return f"{self.movie.title} @ {self.start_time:%Y-%m-%d %H:%M} ({self.auditorium})"

class Seat(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='seats')
    row_label = models.CharField(max_length=5)
    col_number = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False)
    class Meta:
        unique_together = ('showtime', 'row_label', 'col_number')
        ordering = ['row_label', 'col_number']
    def __str__(self): return f"{self.row_label}{self.col_number} ({'X' if self.is_booked else ' '})"

class Booking(models.Model):
    STATUS_CHOICES = [('ACTIVE','Active'), ('CANCELLED','Cancelled')]
    user_name = models.CharField(max_length=120)
    user_phone = models.CharField(max_length=50)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name='bookings')
    seat_row = models.CharField(max_length=5)
    seat_col = models.PositiveIntegerField()
    booked_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    def __str__(self): return f"#{self.pk} {self.user_name} {self.seat_row}{self.seat_col} {self.status}"
