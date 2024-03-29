# Generated by Django 2.2.2 on 2019-07-16 09:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendship', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendship',
            name='friends',
        ),
        migrations.AddField(
            model_name='friendship',
            name='friendships',
            field=models.ManyToManyField(related_name='_friendship_friendships_+', to='friendship.Friendship'),
        ),
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('accepted', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('to_user', 'from_user')},
            },
        ),
    ]
