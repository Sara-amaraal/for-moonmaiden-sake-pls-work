# Generated by Django 4.1.2 on 2022-11-17 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_option_justification_remove_question_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tags',
            new_name='tag',
        ),
    ]
