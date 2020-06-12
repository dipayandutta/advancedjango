# Generated by Django 3.0 on 2020-06-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('WHITE', 'white'), ('BLUE', 'Blue'), ('BLACK', 'Black'), ('GREEN', 'Green')], max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
