# Generated by Django 5.1.2 on 2024-12-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_contact_name_contact_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allocated_spending', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estimated_cost_per_lead', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marketing_channels', models.CharField(max_length=200)),
                ('primary_communication_method', models.CharField(max_length=50)),
                ('campaign_source', models.CharField(max_length=100)),
                ('utm_parameters', models.CharField(max_length=200)),
                ('tracking_code', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Active', 'Active'), ('Completed', 'Completed')], default='Draft', max_length=20)),
                ('owner', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='owner',
        ),
    ]
