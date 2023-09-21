# from django.http import HttpResponse
# from django.shortcuts import render
# from django.template import loader


# Create your views here.
# def brightBoostApp(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())
from django.shortcuts import render, redirect
from .models import Session, TutorSchedule
from .forms import SessionForm, TutorScheduleForm

def home(request):
    # You can customize this view to render the home page
    return render(request, 'base.html')

def add_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions_list')
    else:
        form = SessionForm()
    return render(request, 'add_session.html', {'form': form})

def display_timetable(request):
    tutor_schedules = TutorSchedule.objects.all()
    return render(request, 'timetable.html', {'tutor_schedules': tutor_schedules})


def sessions_list(request):
    sessions = Session.objects.all()  # Retrieve all session objects from the database
    return render(request, 'sessions_list.html', {'sessions': sessions})
