# Generated by Django 5.1.7 on 2025-03-16 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_savingsgoal_target_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavingsGoal',
        ),
    ]
