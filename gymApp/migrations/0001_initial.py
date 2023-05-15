# Generated by Django 3.2.5 on 2023-05-15 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(default='', max_length=50)),
                ('weight', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cnic', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('email_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerPackages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('cnic', models.IntegerField()),
                ('phone_no', models.IntegerField()),
                ('email_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerMembers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
                ('member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.members')),
                ('trainer_package_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.trainerpackages')),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_category', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
                ('member_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.members')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('datetime', models.DateField(auto_now=True)),
                ('operator', models.CharField(max_length=100)),
                ('material_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gymApp.material')),
            ],
        ),
    ]
