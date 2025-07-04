# Generated by Django 4.2.22 on 2025-07-03 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', unique=True, verbose_name='Телефон')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', unique=True, verbose_name='Телефон')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Вопрос')),
                ('status', models.CharField(choices=[('new', 'новая'), ('work', 'в работе'), ('completed', 'завершена')], default='new', max_length=10, verbose_name='Статус заявки')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки на консультацию',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='AppHome.client', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
