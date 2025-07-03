from django.db.models import Sum
from django.shortcuts import render
from django.utils.timezone import now

from .models import Appointment


def page_notes(request):
	notes = Appointment.objects.select_related(
		'client', 'salon', 'service', 'master'
	).order_by('-date', '-reception_time')

	total_unpaid = Appointment.objects.filter(status='not_paid').aggregate(total=Sum('price'))['total'] or 0

	now_date = now().date()
	now_time = now().time()

	upcoming = []
	past = []

	for appointment in notes:
		if appointment.date > now_date:
			upcoming.append(appointment)
		elif appointment.date == now_date and appointment.reception_time > now_time.strftime('%H:%M'):
			upcoming.append(appointment)
		else:
			past.append(appointment)

	context = {
		'upcoming_appointments': upcoming,
		'past_appointments': past,
		'total_unpaid': total_unpaid,
	}

	return render(request, 'notes.html', context)
