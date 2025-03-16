from django.db import models

class Week(models.Model):
    number = models.PositiveIntegerField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    weekly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Daily expenses
    sunday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tuesday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    wednesday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    thursday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    friday = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saturday = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_spent(self):
        return (
            self.sunday + self.monday + self.tuesday +
            self.wednesday + self.thursday + self.friday + self.saturday
        )

    def total_saved(self):
        return self.weekly_budget - self.total_spent()

    def __str__(self):
        return f"Week {self.number} ({self.start_date} - {self.end_date})"
