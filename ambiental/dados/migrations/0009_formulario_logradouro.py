# Generated by Django 2.1.3 on 2018-11-28 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0008_auto_20181127_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='logradouro',
            field=models.TextField(default=10),
            preserve_default=False,
        ),
    ]
