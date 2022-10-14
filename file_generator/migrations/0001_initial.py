# Generated by Django 4.1.2 on 2022-10-14 21:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCeleryLog',
            fields=[
                ('log_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]