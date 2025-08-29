from django import forms
class BookingForm(forms.Form):
    user_name = forms.CharField(max_length=120, label='Your name')
    user_phone = forms.CharField(max_length=50, label='Phone')
    seats = forms.CharField(label='Seats (A1, A2, ...)', help_text='Use row letter + number, e.g., A1, B10')

class CancelForm(forms.Form):
    user_phone = forms.CharField(max_length=50, label='Phone')
