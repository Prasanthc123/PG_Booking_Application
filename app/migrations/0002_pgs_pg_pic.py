# Generated by Django 5.0.2 on 2024-02-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pgs',
            name='pg_pic',
            field=models.ImageField(default='ntr.jpg', upload_to=''),
        ),
    ]
