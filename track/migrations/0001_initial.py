# Generated by Django 2.0.1 on 2018-01-22 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('is_bot', models.BooleanField(default=False)),
                ('referer', models.TextField(null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Property')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sponsor')),
                ('sponsorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sponsorship')),
            ],
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.TextField()),
                ('is_bot', models.BooleanField(default=False)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Property')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sponsor')),
                ('sponsorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Sponsorship')),
            ],
        ),
    ]
