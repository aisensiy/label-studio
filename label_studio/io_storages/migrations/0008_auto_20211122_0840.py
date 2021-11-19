# Generated by Django 3.1.13 on 2021-11-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('io_storages', '0007_auto_20210928_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='azureblobexportstorage',
            name='export_type',
            field=models.CharField(choices=[('task', 'Task'), ('annotation', 'Annotation')], default='task', help_text='Export task or annotation', max_length=128, verbose_name='export type'),
        ),
        migrations.AddField(
            model_name='gcsexportstorage',
            name='export_type',
            field=models.CharField(choices=[('task', 'Task'), ('annotation', 'Annotation')], default='task', help_text='Export task or annotation', max_length=128, verbose_name='export type'),
        ),
        migrations.AddField(
            model_name='localfilesexportstorage',
            name='export_type',
            field=models.CharField(choices=[('task', 'Task'), ('annotation', 'Annotation')], default='task', help_text='Export task or annotation', max_length=128, verbose_name='export type'),
        ),
        migrations.AddField(
            model_name='redisexportstorage',
            name='export_type',
            field=models.CharField(choices=[('task', 'Task'), ('annotation', 'Annotation')], default='task', help_text='Export task or annotation', max_length=128, verbose_name='export type'),
        ),
        migrations.AddField(
            model_name='s3exportstorage',
            name='export_type',
            field=models.CharField(choices=[('task', 'Task'), ('annotation', 'Annotation')], default='task', help_text='Export task or annotation', max_length=128, verbose_name='export type'),
        ),
    ]
