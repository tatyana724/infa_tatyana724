# Generated by Django 4.2.11 on 2024-06-04 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attraction_id', models.IntegerField()),
                ('attraction_name', models.CharField(max_length=50)),
                ('coord_1', models.FloatField()),
                ('coord_2', models.FloatField()),
                ('about', models.TextField()),
            ],
            options={
                'db_table': 'Attraction',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('favourites', models.BooleanField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.attraction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
            options={
                'db_table': 'Route',
            },
        ),
    ]