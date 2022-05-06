# Generated by Django 3.2.12 on 2022-04-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photo')),
                ('desc', models.TextField()),
            ],
        ),
    ]