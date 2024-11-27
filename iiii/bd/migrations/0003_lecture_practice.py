# Generated by Django 5.1.3 on 2024-11-26 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name of the lecture')),
                ('date', models.DateField(verbose_name='Date of the lecture')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='bd.course')),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name of the practice')),
                ('date', models.DateField(verbose_name='Date of the practice')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practice', to='bd.lecture')),
            ],
        ),
    ]