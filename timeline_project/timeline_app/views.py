from django.shortcuts import render
from .models import TimelineEvent

def timeline_view(request):
    events = TimelineEvent.objects.all()
    return render(request, 'timeline2.html', {'events': events})
