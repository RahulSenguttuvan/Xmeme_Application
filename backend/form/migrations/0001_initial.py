# Generated by Django 2.2.18 on 2021-02-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('caption', models.CharField(max_length=250)),
                ('url', models.URLField()),
            ],
        ),
    ]