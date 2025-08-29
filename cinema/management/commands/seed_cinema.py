from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime as dt
from cinema.models import Movie, Showtime

class Command(BaseCommand):
    help = "Seed sample movies and showtimes"

    def handle(self, *args, **options):
        Movie.objects.all().delete()
        m1 = Movie.objects.create(title="Inception", duration_min=148, rating="PG-13", description="A thief enters dreams to steal secrets.")
        m2 = Movie.objects.create(title="Interstellar", duration_min=169, rating="PG-13", description="A team travels through a wormhole to save humanity.")
        m3 = Movie.objects.create(title="Spirited Away", duration_min=125, rating="U", description="A girl enters a mysterious spirit world.")
        today = timezone.localdate()
        t1 = timezone.make_aware(dt.datetime.combine(today, dt.time(18,30)))
        t2 = timezone.make_aware(dt.datetime.combine(today, dt.time(21,15)))
        t3 = timezone.make_aware(dt.datetime.combine(today+dt.timedelta(days=1), dt.time(17,0)))
        Showtime.objects.create(movie=m1, start_time=t1, auditorium="Audi-1", rows=8, cols=12, price_cents=45000)
        Showtime.objects.create(movie=m1, start_time=t2, auditorium="Audi-1", rows=8, cols=12, price_cents=45000)
        Showtime.objects.create(movie=m2, start_time=t3, auditorium="Audi-2", rows=10, cols=14, price_cents=55000)
        self.stdout.write(self.style.SUCCESS("Seeded movies & showtimes. Seats auto-generated."))
