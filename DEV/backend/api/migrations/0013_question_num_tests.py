# Generated by Django 4.1.2 on 2022-11-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_test_tags_test_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='num_tests',
            field=models.IntegerField(default=0),
        ),
    ]
