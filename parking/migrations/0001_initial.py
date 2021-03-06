# Generated by Django 2.2 on 2020-03-22 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('slot_no', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('car_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('in_time', models.DateTimeField()),
                ('out_time', models.DateTimeField()),
                ('date', models.DateField()),
                ('slot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parking.ParkingSlot')),
            ],
        ),
    ]
