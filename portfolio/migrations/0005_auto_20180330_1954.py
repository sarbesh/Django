# Generated by Django 2.0.3 on 2018-03-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20180330_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='Photo',
            field=models.ImageField(null=True, upload_to='media/Image/%Y/%m'),
        ),
    ]
