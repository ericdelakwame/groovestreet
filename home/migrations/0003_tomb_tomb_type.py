# Generated by Django 3.2 on 2022-10-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tomb_tombtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomb',
            name='tomb_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tombs', to='home.tombtype'),
        ),
    ]
