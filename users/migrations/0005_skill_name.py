# Generated by Django 4.2.3 on 2023-07-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]