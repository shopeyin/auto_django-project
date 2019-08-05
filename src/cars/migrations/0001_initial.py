# Generated by Django 2.2.2 on 2019-08-01 05:44

import cars.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('cars_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1984), cars.models.max_value_current_year], verbose_name='year')),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('condition', models.CharField(choices=[('N', 'New'), ('T', 'Tokunbo'), ('NU', 'Nigerian Use')], max_length=2)),
                ('fuel_type', models.CharField(choices=[('P', 'Petrol'), ('D', 'Diesel'), ('E', 'Electric')], max_length=1, verbose_name='fuel type')),
                ('image', models.ImageField(blank=True, null=True, upload_to=cars.models.upload_location)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]