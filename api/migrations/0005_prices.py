# Generated by Django 4.0.5 on 2022-07-04 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_alter_partyname_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=100)),
                ('p_price', models.TextField(default=0, max_length=10)),
                ('d_price', models.TextField(default=0, max_length=10)),
                ('xp_price', models.TextField(default=0, max_length=10)),
                ('s_price', models.TextField(default=0, max_length=10)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
