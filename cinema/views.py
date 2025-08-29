from __future__ import annotations
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.contrib import messages
from django.utils import timezone
from .models import Movie, Showtime, Seat, Booking
from .forms import BookingForm, CancelForm
from .utils import parse_seat_codes, make_row_labels

def home(request):
    movies = Movie.objects.all()
    
    return render(request, 'cinema/home.html', {'movies': movies})

def movie_detail(request, movie_id: int):
    movie = get_object_or_404(Movie, pk=movie_id)
    showtimes = movie.showtimes.order_by('start_time')
    return render(request, 'cinema/movie_detail.html', {'movie': movie, 'showtimes': showtimes})

def showtime_detail(request, showtime_id: int):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    rows = make_row_labels(showtime.rows)
    seat_lookup = {(s.row_label, s.col_number): s for s in showtime.seats.all()}
    grid = []
    for r in rows:
        row_cells = []
        for c in range(1, showtime.cols + 1):
            row_cells.append(seat_lookup[(r, c)])
        grid.append((r, row_cells))
    form = BookingForm()
    return render(request, 'cinema/showtime_detail.html', {'showtime': showtime, 'grid': grid, 'form': form})

@transaction.atomic
def book_seats(request, showtime_id: int):
    showtime = get_object_or_404(Showtime, pk=showtime_id)
    if request.method != 'POST':
        return redirect('cinema:showtime_detail', showtime_id=showtime_id)
    form = BookingForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Please correct the form errors.")
        return redirect('cinema:showtime_detail', showtime_id=showtime_id)
    user_name = form.cleaned_data['user_name']
    user_phone = form.cleaned_data['user_phone']
    try:
        requested = parse_seat_codes(form.cleaned_data['seats'])
        print(requested, type(requested))
    except ValueError as e:
        messages.error(request, str(e)); return redirect('cinema:showtime_detail', showtime_id=showtime_id)
    to_book = []
    for (r, c) in requested:
        try:
            seat = Seat.objects.select_for_update().get(showtime=showtime, row_label=r, col_number=c)
        except Seat.DoesNotExist:
            messages.error(request, f"Seat {r}{c} does not exist."); return redirect('cinema:showtime_detail', showtime_id=showtime_id)
        if seat.is_booked:
            messages.error(request, f"Seat {r}{c} is already booked."); return redirect('cinema:showtime_detail', showtime_id=showtime_id)
        to_book.append(seat)
    bookings = []
    for seat in to_book:
        seat.is_booked = True; seat.save(update_fields=['is_booked'])
        b = Booking.objects.create(user_name=user_name, user_phone=user_phone, showtime=showtime, seat_row=seat.row_label, seat_col=seat.col_number)
        bookings.append(b)
    total_cents = showtime.price_cents * len(bookings)
    return render(request, 'cinema/booking_success.html', {'showtime': showtime, 'bookings': bookings, 'total_cents': total_cents})

@transaction.atomic
def cancel_booking(request):
    if request.method == 'POST':
        # Step 1: User entered phone number
        if 'user_phone' in request.POST and 'booking_id' not in request.POST:
            form = CancelForm(request.POST)
            if form.is_valid():
                user_phone = form.cleaned_data['user_phone']
                bookings = Booking.objects.filter(user_phone=user_phone, status='ACTIVE')
                if not bookings.exists():
                    messages.error(request, "No active bookings found for this phone number.")
                    return redirect('cinema:cancel_booking')
                # Show user all their bookings to choose from
                return render(request, 'cinema/select_booking.html', {'bookings': bookings})

        # Step 2: User picked a specific booking
        elif 'booking_id' in request.POST:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id)

            with transaction.atomic():
                # free the seat
                seat = Seat.objects.filter(
                    showtime=booking.showtime,
                    row_label=booking.seat_row,
                    col_number=booking.seat_col
                ).first()
                if seat:
                    seat.is_booked = False
                    seat.save(update_fields=['is_booked'])

                booking.status = 'CANCELLED'
                booking.save(update_fields=['status'])

            messages.success(request, "Booking cancelled successfully.")
            return redirect('cinema:cancel_booking')

    else:
        form = CancelForm()

    return render(request, 'cinema/cancel.html', {'form': form})