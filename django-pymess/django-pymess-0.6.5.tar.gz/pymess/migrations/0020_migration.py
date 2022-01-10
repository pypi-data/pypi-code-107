# Generated by Django 2.2.12 on 2020-07-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pymess', '0019_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialermessage',
            name='retry_sending',
        ),
        migrations.RemoveField(
            model_name='emailmessage',
            name='retry_sending',
        ),
        migrations.RemoveField(
            model_name='outputsmsmessage',
            name='retry_sending',
        ),
        migrations.RemoveField(
            model_name='pushnotificationmessage',
            name='retry_sending',
        ),
        migrations.AlterField(
            model_name='dialermessage',
            name='state',
            field=models.IntegerField(
                choices=[(-1, 'waiting'), (0, 'not assigned'), (1, 'ready'), (2, 'rescheduled by dialer'),
                         (3, 'call in progress'), (4, 'hangup'), (5, 'done'), (6, 'rescheduled'),
                         (7, 'listened up complete message'), (8, 'listened up partial message'), (9, 'unreachable'),
                         (10, 'declined'), (11, 'unanswered'), (12, 'unanswered - hangup by dialer'),
                         (13, 'answered - hangup by customer'), (66, 'error message update'), (77, 'debug'),
                         (88, 'error'), (99, 'error retry')], db_index=True, editable=False, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='emailmessage',
            name='state',
            field=models.IntegerField(
                choices=[(1, 'waiting'), (2, 'sending'), (3, 'sent'), (4, 'error'), (5, 'debug'), (6, 'error retry')],
                db_index=True, editable=False, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='outputsmsmessage',
            name='state',
            field=models.IntegerField(
                choices=[(1, 'waiting'), (2, 'unknown'), (3, 'sending'), (4, 'sent'), (5, 'error message update'),
                         (6, 'debug'), (7, 'delivered'), (8, 'error'), (9, 'error retry')], db_index=True,
                editable=False, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='pushnotificationmessage',
            name='state',
            field=models.PositiveIntegerField(choices=[(1, 'waiting'), (2, 'sent'), (3, 'error'), (4, 'debug'),
                                                       (5, 'error retry')],
                                              db_index=True, editable=False, verbose_name='state'),
        ),
    ]
