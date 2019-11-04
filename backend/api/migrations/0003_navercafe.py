# Generated by Django 2.2.6 on 2019-10-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navercafe',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('model_name', models.CharField(blank=True, max_length=100, null=True)),
                ('generation', models.CharField(blank=True, max_length=10, null=True)),
                ('display', models.CharField(blank=True, max_length=10, null=True)),
                ('cellular', models.CharField(blank=True, max_length=10, null=True)),
                ('storage', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('img_src', models.CharField(blank=True, max_length=100, null=True)),
                ('is_sell', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'navercafe',
                'managed': False,
            },
        ),
    ]
