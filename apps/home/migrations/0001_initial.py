# Generated by Django 3.2.16 on 2024-02-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('price_eur', models.IntegerField()),
                ('date_posted', models.DateField()),
                ('timestamp', models.DateTimeField()),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
