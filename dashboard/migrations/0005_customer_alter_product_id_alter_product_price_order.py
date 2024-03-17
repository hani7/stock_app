# Generated by Django 4.2.9 on 2024-03-01 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birth_day', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='dashboard.product')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]