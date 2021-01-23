# Generated by Django 3.1.4 on 2021-01-06 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210106_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='store', to='users.address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='store', to='users.company')),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at', '-updated_at'),
                'abstract': False,
            },
        ),
    ]