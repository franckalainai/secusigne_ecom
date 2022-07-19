# Generated by Django 3.2.14 on 2022-07-14 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secusigne', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('alt_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveBigIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secusigne.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secusigne.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secusigne.size')),
            ],
        ),
    ]
