# Generated by Django 3.0.7 on 2020-07-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_health', '0013_auto_20200719_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='build_commit_url_github',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='build_name',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='build_source',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='build_version',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='nvr',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
