# Generated by Django 3.1.4 on 2021-01-06 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('addresses', models.ManyToManyField(blank=True, related_name='customer', to='users.Address')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
    ]