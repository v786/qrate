# Generated by Django 3.2.8 on 2021-11-08 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211101_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(upload_to='storage/'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='api.profile'),
        ),
    ]
