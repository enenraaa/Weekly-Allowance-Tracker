from django.contrib import admin
from .models import Week

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_date', 'end_date', 'weekly_budget', 'total_spent', 'total_saved')
    list_filter = ('start_date', 'end_date')
    search_fields = ('number',)

