# Generated by Django 4.2.3 on 2023-07-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrtion',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Promise',
        ),
    ]
