# Generated by Django 3.2.6 on 2022-06-12 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localbank', '0002_bankitem_belongsto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankitem',
            options={'permissions': (('can_create_item', 'set field for a new item'),)},
        ),
    ]
