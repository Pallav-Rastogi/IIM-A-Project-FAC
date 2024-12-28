# Generated by Django 4.2.17 on 2024-12-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeSummary',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('buy_id', models.CharField(max_length=50)),
                ('sell_id', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]