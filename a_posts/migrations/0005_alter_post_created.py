# Generated by Django 4.2 on 2023-05-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0004_alter_post_artist_alter_post_id_alter_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
