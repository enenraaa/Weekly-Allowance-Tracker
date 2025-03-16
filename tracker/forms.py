from django import forms
from .models import Week  

class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = [
            'number', 'start_date', 'end_date', 'weekly_budget',
            'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
        ]
