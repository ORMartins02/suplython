# Generated by Django 4.0.7 on 2023-01-10 22:43


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('tel', models.CharField(max_length=20, unique=True)),
                ('cnpj', models.CharField(max_length=15)),
            ],
        ),
    ]
