# Generated by Django 3.0.6 on 2020-05-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CowUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('say', models.CharField(max_length=120)),
            ],
        ),
    ]
