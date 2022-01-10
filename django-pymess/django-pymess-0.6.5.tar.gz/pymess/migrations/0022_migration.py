# Generated by Django 3.1.4 on 2020-12-21 18:49

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pymess', '0021_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialermessage',
            name='extra_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra data'),
        ),
        migrations.AlterField(
            model_name='dialermessage',
            name='extra_sender_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra sender data'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='extra_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra data'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='extra_sender_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra sender data'),
        ),
        migrations.AlterField(
            model_name='outputsmsmessage',
            name='extra_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra data'),
        ),
        migrations.AlterField(
            model_name='outputsmsmessage',
            name='extra_sender_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra sender data'),
        ),
        migrations.AlterField(
            model_name='pushnotificationmessage',
            name='extra_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra data'),
        ),
        migrations.AlterField(
            model_name='pushnotificationmessage',
            name='extra_sender_data',
            field=models.JSONField(blank=True, editable=False, encoder=django.core.serializers.json.DjangoJSONEncoder,
                                   null=True, verbose_name='extra sender data'),
        ),
    ]
