from django import forms
from .models import Session, TutorSchedule

# The SessionForm class is a ModelForm that is used to create or update Session objects with specified
# fields.
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'students_attended', 'questions_answered', 'subject_area']

# The TutorScheduleForm class is a form that allows users to input information about a tutor's
# schedule.
class TutorScheduleForm(forms.ModelForm):
    class Meta:
        model = TutorSchedule
        fields = ['tutor_name', 'day_of_week', 'start_time', 'end_time']

