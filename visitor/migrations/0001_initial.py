# Generated by Django 5.0.6 on 2024-07-31 17:03

import django.db.models.deletion
import visitor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForm',
            fields=[
                ('id', models.CharField(default=visitor.models.requestID, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=100, verbose_name='Fullname')),
                ('companyName', models.CharField(max_length=50, verbose_name='Company Name')),
                ('companyAddress', models.CharField(max_length=100, verbose_name='Company Address')),
                ('reasonOfRequest', models.TextField(blank=True, null=True, verbose_name='Reason For Request')),
                ('dateFrom', models.DateField(verbose_name='Start Date')),
                ('dateTo', models.DateField(verbose_name='End Date')),
                ('appointment', models.BooleanField()),
                ('noAppointment', models.BooleanField()),
                ('guard', models.CharField(max_length=200, verbose_name='SG in Charge')),
                ('placesVisited', models.CharField(max_length=200, verbose_name='Last Places Visited')),
                ('bdv', models.BooleanField()),
                ('soreThroat', models.BooleanField()),
                ('cold', models.BooleanField()),
                ('mumps', models.BooleanField()),
                ('skin', models.BooleanField()),
                ('styes', models.BooleanField()),
                ('jaundice', models.BooleanField()),
                ('cuts', models.BooleanField()),
                ('infection', models.BooleanField()),
                ('typhoid', models.BooleanField()),
                ('country', models.CharField(max_length=100, verbose_name='Last Countries Visited')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=4, max_length=4)),
                ('agreement', models.BooleanField(default=True)),
                ('dateSigned', models.DateField(verbose_name='Date Signed')),
                ('approved', models.CharField(choices=[('Review', 'Review'), ('Approve', 'Approve'), ('Denied', 'Denied')], default='Review', max_length=10, verbose_name='Review')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment here')),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('contactPerson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empname', verbose_name='ZFC Employee')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]