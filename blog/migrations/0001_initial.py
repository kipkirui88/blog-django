# Generated by Django 3.2.9 on 2022-12-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
    ]
