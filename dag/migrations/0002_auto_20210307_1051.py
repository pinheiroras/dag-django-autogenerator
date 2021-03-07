# Generated by Django 2.2.19 on 2021-03-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dag', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fields',
            old_name='type',
            new_name='fieldtype',
        ),
        migrations.RemoveField(
            model_name='apps',
            name='is_verify',
        ),
        migrations.AddField(
            model_name='fields',
            name='bootstrap_columns',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='fields',
            name='fieldtype_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fields',
            name='foreignkey_model_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fields',
            name='model_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='models',
            name='app_slug',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='models',
            name='django_inline_models',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='models',
            name='quant',
            field=models.IntegerField(default=0),
        ),
    ]
