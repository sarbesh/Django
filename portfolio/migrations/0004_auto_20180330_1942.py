# Generated by Django 2.0.3 on 2018-03-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_name_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='Photo',
            field=models.ImageField(null=True, upload_to='user/Image/%Y/%m'),
        ),
    ]
