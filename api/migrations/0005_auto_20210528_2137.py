# Generated by Django 3.1.4 on 2021-05-28 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_studentmarks_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentMarks',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]