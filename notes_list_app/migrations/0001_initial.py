# Generated by Django 3.0.7 on 2020-07-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=1023)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
