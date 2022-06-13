# Generated by Django 4.0.4 on 2022-05-29 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe (Default)', max_length=200, null=True)),
                ('title', models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey, there this is a default text description about you that you can change on after clicking on "Edit" or going to your profile page.', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
