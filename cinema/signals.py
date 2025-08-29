from __future__ import annotations
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Showtime, Seat
from .utils import make_row_labels

@receiver(post_save, sender=Showtime)
def create_seats_on_showtime_create(sender, instance: Showtime, created: bool, **kwargs):
    if not created:
        return
    rows = make_row_labels(instance.rows)
    bulk = []
    for r in rows:
        for c in range(1, instance.cols + 1):
            bulk.append(Seat(showtime=instance, row_label=r, col_number=c, is_booked=False))
    Seat.objects.bulk_create(bulk)
