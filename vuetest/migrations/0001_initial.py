# Generated by Django 3.1.6 on 2021-02-18 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(default='', max_length=200, verbose_name='Last name')),
                ('description', models.TextField()),
                ('expertise', models.CharField(choices=[('math', 'Math'), ('arts', 'Arts'), ('other', 'Other')], default='', max_length=200, verbose_name='First name')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vuetest.coach')),
            ],
        ),
    ]
