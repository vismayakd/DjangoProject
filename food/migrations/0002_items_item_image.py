# Generated by Django 4.2 on 2024-08-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6w-cm1vGXpLrYd-1fo0WViPNtk2DuhR-xBnfDl7l-ADoW6AWx1rX_Cw-mPw&s', max_length=200),
        ),
    ]
