# Generated by Django 4.2.1 on 2023-05-23 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymApp', '0003_material_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='package_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.packages'),
        ),
    ]
