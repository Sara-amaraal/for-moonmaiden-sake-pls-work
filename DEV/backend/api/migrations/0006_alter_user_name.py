# Generated by Django 4.1.2 on 2022-10-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_vote_justification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]