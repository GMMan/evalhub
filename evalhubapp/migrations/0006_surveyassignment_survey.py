# Generated by Django 2.2.7 on 2019-11-25 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_survey_editable_answers'),
        ('evalhubapp', '0005_auto_20191124_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyassignment',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
            preserve_default=False,
        ),
    ]
