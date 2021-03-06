# Generated by Django 2.1.3 on 2018-11-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiltroBAA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pessoas', models.IntegerField()),
                ('C', models.IntegerField()),
                ('contr_dia', models.IntegerField()),
                ('T', models.FloatField()),
                ('volume_util_L', models.FloatField()),
                ('volume_util_M', models.FloatField()),
                ('area', models.FloatField()),
                ('diametro', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TSeptico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_pessoas', models.IntegerField()),
                ('C', models.IntegerField()),
                ('contr_dia', models.IntegerField()),
                ('T', models.FloatField()),
                ('K', models.IntegerField()),
                ('Lf', models.IntegerField()),
                ('volume_util_L', models.FloatField()),
                ('volume_util_M', models.FloatField()),
                ('alt_adotada', models.FloatField()),
                ('area', models.FloatField()),
                ('diametro', models.FloatField()),
            ],
        ),
    ]
