# Generated by Django 4.1.2 on 2022-10-23 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_vote_justification'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('user', 'question'), name='unique question-user'),
        ),
    ]
