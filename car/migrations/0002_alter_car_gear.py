# Generated by Django 4.2.2 on 2023-06-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gear',
            field=models.BooleanField(choices=[(1, 'Auto'), (0, 'Manual')], default=0),
        ),
    ]
