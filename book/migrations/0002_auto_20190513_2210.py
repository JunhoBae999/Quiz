# Generated by Django 2.2.1 on 2019-05-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving1', models.CharField(max_length=200)),
                ('saving2', models.CharField(max_length=200)),
                ('saving3', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
