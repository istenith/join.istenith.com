# Generated by Django 4.0.6 on 2022-07-31 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_template_insta_template_twitter_template_whatsapp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='insta',
            new_name='instagram',
        ),
    ]
