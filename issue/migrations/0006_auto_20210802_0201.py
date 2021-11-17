# Generated by Django 3.2.5 on 2021-08-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0005_auto_20210731_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]