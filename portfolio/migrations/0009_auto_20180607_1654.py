# Generated by Django 2.0.5 on 2018-06-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20180607_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
