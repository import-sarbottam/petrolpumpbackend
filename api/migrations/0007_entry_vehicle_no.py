# Generated by Django 4.0.5 on 2022-07-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_partyname_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='vehicle_no',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]