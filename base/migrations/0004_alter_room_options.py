# Generated by Django 4.2.6 on 2023-10-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_room_host_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]