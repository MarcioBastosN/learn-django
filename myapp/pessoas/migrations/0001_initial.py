# Generated by Django 2.2 on 2024-03-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=100)),
                ('person_genero', models.CharField(max_length=1)),
                ('person_bithday', models.DateField()),
            ],
        ),
    ]
