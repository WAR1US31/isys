# Generated by Django 3.2.8 on 2021-10-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_messages_date_of_execution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date_of_execution',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата исполнения'),
        ),
    ]
