# Generated by Django 4.0.4 on 2022-05-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MortgageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('initial_fee', models.IntegerField()),
                ('years', models.IntegerField()),
            ],
        ),
    ]
