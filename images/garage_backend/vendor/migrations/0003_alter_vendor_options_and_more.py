# Generated by Django 5.1.7 on 2025-03-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vendor', '0002_alter_vendor_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={},
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='contact_number',
            new_name='business_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='description',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='password',
        ),
        migrations.AddField(
            model_name='vendor',
            name='country_of_citizenship',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='country_of_issue',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='date_of_expiry',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='date_of_issue',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='identity_number',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone_number',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='vendor',
            table=None,
        ),
    ]
