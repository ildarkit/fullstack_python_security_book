# Generated by Django 4.2.7 on 2023-11-19 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authenticatedmessage',
            options={'permissions': [('send_authenticatedmessage', 'Can send msgs'), ('receive_authenticatedmessage', 'Can receive msgs')]},
        ),
    ]
