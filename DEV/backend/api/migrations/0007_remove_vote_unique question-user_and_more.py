# Generated by Django 4.1.2 on 2022-10-23 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_vote_unique_together_alter_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='vote',
            name='unique question-user',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('user', 'question')},
        ),
    ]
