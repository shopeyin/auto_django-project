# Generated by Django 2.2.2 on 2019-08-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phonenumber', models.BigIntegerField(verbose_name='phonenumber')),
            ],
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phonenumber', models.BigIntegerField(verbose_name='phonenumber')),
                ('message', models.TextField(max_length=450)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
