# Generated by Django 3.2.6 on 2023-03-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentRegister', '0003_auto_20230316_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Admission_Number',
            field=models.CharField(max_length=50, null=True, verbose_name='Admission Number'),
        ),
    ]