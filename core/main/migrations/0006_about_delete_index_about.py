# Generated by Django 5.0.4 on 2024-04-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_index_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='about/', verbose_name='Aboout image')),
                ('name', models.CharField(max_length=250, verbose_name='About name')),
                ('text', models.TextField(verbose_name='About text')),
                ('but_name', models.CharField(max_length=250, verbose_name='Button name')),
            ],
        ),
        migrations.DeleteModel(
            name='index_about',
        ),
    ]
