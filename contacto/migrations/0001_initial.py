# Generated by Django 3.0.8 on 2020-11-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
