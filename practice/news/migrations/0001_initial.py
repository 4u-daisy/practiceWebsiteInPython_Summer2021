# Generated by Django 3.2.6 on 2021-09-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Статья', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='Анонс статьи!', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(default='Ничего нет', verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
