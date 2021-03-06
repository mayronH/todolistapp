# Generated by Django 3.0.7 on 2020-06-17 15:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('done_date', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todolist.Category')),
            ],
        ),
    ]
