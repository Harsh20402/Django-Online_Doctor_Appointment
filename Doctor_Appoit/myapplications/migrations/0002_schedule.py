# Generated by Django 3.2 on 2022-11-02 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapplications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=255, verbose_name='Doctors Available')),
                ('time_slot', models.CharField(max_length=255, verbose_name='Timing')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='myapplications.doctor', verbose_name='Doctor')),
            ],
        ),
    ]