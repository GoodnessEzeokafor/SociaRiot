# Generated by Django 3.0.4 on 2020-03-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200323_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='<built-in function id>'),
        ),
    ]
