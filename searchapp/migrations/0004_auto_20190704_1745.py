# Generated by Django 2.1.9 on 2019-07-04 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_auto_20190704_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodstbl',
            old_name='categoryid',
            new_name='categoryname',
        ),
    ]
