# Generated by Django 4.2 on 2023-04-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Наименование')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Изображение')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альтернативный текст')),
            ],
        ),
    ]
