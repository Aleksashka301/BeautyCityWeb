from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from .models import Appointment, Service
from AppHome.models import Feedback


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

	services_images = list(Service.objects.all())

	context = {
		'upcoming_appointments': upcoming,
		'past_appointments': past,
		'total_unpaid': total_unpaid,
		'services': services_images,
	}

	return render(request, 'notes.html', context)

@csrf_exempt
def send_feedback(request):
	if request.method == 'POST':
		name = request.POST.get('fname')
		text = request.POST.get('popupTextarea')

		if name and text:
			Feedback.objects.create(
				author=name,
				text=text
			)
			return redirect('notes')

	return HttpResponse("Ошибка при отправке", status=400)
