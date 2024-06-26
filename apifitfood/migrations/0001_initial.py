# Generated by Django 5.0.6 on 2024-06-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('calories', models.IntegerField()),
                ('proteins', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carbohydrate', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField(max_length=500)),
            ],
        ),
    ]
