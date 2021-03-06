# Generated by Django 2.0.1 on 2018-01-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(db_index=True, max_length=10)),
                ('url', models.CharField(max_length=500)),
                ('views', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['views', 'created'],
            },
        ),
    ]
