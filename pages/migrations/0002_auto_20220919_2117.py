# Generated by Django 3.0 on 2022-09-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Names', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Pay',
        ),
    ]