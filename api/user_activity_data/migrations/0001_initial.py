# Generated by Django 4.0.4 on 2022-04-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivityData',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('activity_type', models.TextField()),
                ('value', models.IntegerField()),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
                ('points', models.IntegerField()),
            ],
            options={
                'db_table': 'user_activity_data',
            },
        ),
    ]