# Generated by Django 4.0.4 on 2022-09-03 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userrole'),
        ),
    ]
