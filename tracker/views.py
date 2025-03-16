from django.shortcuts import render, redirect, get_object_or_404
from .models import Week
from .forms import WeekForm

def home(request):
    weeks = Week.objects.all()
    total_spent = sum(week.total_spent() for week in weeks)
    total_saved = sum(week.total_saved() for week in weeks)
    
    
    return render(request, 'tracker/home.html', {
        'weeks': weeks,
        'total_spent': total_spent,
        'total_saved': total_saved,
         
    })

def create_week(request):
    if request.method == 'POST':
        form = WeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeekForm()
    return render(request, 'tracker/week_form.html', {'form': form})

def edit_week(request, week_id):
    week = get_object_or_404(Week, id=week_id)
    if request.method == 'POST':
        form = WeekForm(request.POST, instance=week)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WeekForm(instance=week)
    return render(request, 'tracker/week_form.html', {'form': form})

def delete_week(request, week_id):
    week = get_object_or_404(Week, id=week_id)
    if request.method == 'POST':
        week.delete()
        return redirect('home')
    return render(request, 'tracker/confirm_delete.html', {'week': week})
