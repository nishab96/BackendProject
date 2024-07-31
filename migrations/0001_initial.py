# Generated by Django 4.1 on 2024-06-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('current_password', models.CharField(max_length=100, null=True)),
                ('new_password', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
