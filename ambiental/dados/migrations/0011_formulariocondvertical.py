# Generated by Django 3.0.2 on 2020-01-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0010_auto_20190404_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioCondVertical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_lotes', models.IntegerField()),
                ('num_predios', models.IntegerField()),
            ],
        ),
    ]
