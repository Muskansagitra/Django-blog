# Generated by Django 5.0.3 on 2024-07-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_rename_descr_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
