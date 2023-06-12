# Generated by Django 4.2.1 on 2023-06-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_borrow_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('r', 'reserved'), ('m', 'maintenance'), ('o', 'on lone'), ('a', 'available')], default='m', help_text='book status', max_length=1),
        ),
    ]
