# Generated by Django 4.2.17 on 2025-02-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0005_alter_admin_id_alter_trainer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.UUIDField(default=155789, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='id',
            field=models.UUIDField(default=155789, editable=False, primary_key=True, serialize=False),
        ),
    ]
