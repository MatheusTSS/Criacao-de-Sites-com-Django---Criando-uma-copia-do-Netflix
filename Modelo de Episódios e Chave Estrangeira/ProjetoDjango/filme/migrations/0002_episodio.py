# Generated by Django 4.0 on 2021-12-16 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodios', to='filme.filme')),
            ],
        ),
    ]
