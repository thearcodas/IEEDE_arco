# Generated by Django 5.1.3 on 2024-11-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_educationprofile_email_educationprofile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationprofile',
            name='department',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]