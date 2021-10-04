# Generated by Django 3.1.4 on 2021-06-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SlaGenerator', '0028_tareplycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='threat',
            name='Compromised',
            field=models.CharField(default='self', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='threatagentattribute',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
