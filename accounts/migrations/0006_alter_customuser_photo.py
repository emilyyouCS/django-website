# Generated by Django 4.1.2 on 2022-11-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='account/%Y/%m/%d/'),
        ),
    ]
