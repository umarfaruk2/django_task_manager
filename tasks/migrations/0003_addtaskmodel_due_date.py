# Generated by Django 4.2.5 on 2023-10-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_addtaskmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtaskmodel',
            name='due_date',
            field=models.DateTimeField(default=None),
        ),
    ]