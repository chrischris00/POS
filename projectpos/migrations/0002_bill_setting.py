# Generated by Django 3.1.6 on 2021-03-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StoreName', models.TextField()),
                ('VAT', models.IntegerField()),
                ('SC', models.IntegerField()),
                ('EndTextBill', models.TextField()),
            ],
        ),
    ]
