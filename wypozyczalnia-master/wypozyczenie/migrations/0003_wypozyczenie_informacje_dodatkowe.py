# Generated by Django 3.1.3 on 2021-03-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczenie', '0002_wypozyczenie_data_platnosci'),
    ]

    operations = [
        migrations.AddField(
            model_name='wypozyczenie',
            name='informacje_dodatkowe',
            field=models.CharField(default='Brak informacji dodatkowych', max_length=150),
        ),
    ]
