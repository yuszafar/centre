# Generated by Django 3.1.5 on 2021-02-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210209_1207'),
        ('events', '0002_auto_20210116_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentgroup'),
        ),
    ]