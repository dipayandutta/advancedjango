# Generated by Django 3.0 on 2020-06-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('MERCEDES', 'Mercedes'), ('TESLA', 'Tesla'), ('BMW', 'Bmw'), ('AUDI', 'Audi')], max_length=100)),
                ('model', models.CharField(max_length=200)),
                ('max_speed', models.PositiveIntegerField()),
                ('country', models.CharField(blank=True, max_length=200)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]