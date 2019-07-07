# Generated by Django 2.2.1 on 2019-06-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DestinationName', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]