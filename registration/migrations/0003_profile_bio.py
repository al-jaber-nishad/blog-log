# Generated by Django 4.0.1 on 2022-02-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur numquam non nobis fuga ut commodi minus mollitia consectetur, praesentium, optio laudantium, beatae impedit deleniti sed repellendus natus distinctio doloribus nam!', max_length=200),
            preserve_default=False,
        ),
    ]
