# Generated by Django 4.0.4 on 2023-04-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flows',
            name='name',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flows',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
