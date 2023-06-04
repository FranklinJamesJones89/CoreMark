from django.shortcuts import render, get_object_or_404
from .models import Day


def index(request):
    days = Day.objects.all()
    return render(request, 'coremarks/index.html', {'days': days})


def day_detail(request, pk):
    day = get_object_or_404(Day, pk=pk)
    return render(request, 'coremarks/day_detail.html', {'day': day})

    


