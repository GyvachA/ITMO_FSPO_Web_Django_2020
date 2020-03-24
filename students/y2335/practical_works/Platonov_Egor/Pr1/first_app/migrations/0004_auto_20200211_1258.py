# Generated by Django 3.0.3 on 2020-02-11 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_users_drivers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='drivers',
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_buy', models.DateField()),
                ('date_Sell', models.DateField()),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.auto')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.users')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='driver',
            field=models.ManyToManyField(through='first_app.Drivers', to='first_app.auto'),
        ),
    ]