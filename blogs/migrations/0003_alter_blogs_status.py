# Generated by Django 5.2.3 on 2025-06-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('hide', 'Archived')], default='draft', max_length=100),
        ),
    ]
