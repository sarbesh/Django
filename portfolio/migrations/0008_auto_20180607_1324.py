# Generated by Django 2.0.5 on 2018-06-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20180607_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]