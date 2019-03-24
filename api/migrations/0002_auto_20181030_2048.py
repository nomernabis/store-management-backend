# Generated by Django 2.1 on 2018-10-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'moderator'), (3, 'user')], default=3),
        ),
    ]