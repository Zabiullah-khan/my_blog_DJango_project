# Generated by Django 3.2.16 on 2022-12-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('postarea', models.TextField(max_length=5000)),
            ],
        ),
    ]
