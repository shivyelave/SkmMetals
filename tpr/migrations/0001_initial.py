# Generated by Django 5.0.1 on 2024-01-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TPR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TPR_NO', models.CharField(max_length=50)),
                ('segment', models.CharField(max_length=50)),
                ('customer', models.CharField(max_length=50)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
