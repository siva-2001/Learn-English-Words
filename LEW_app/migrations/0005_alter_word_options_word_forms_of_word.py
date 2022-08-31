# Generated by Django 4.1 on 2022-08-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEW_app', '0004_word_translates_delete_translate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('word', 'word_verified_by_administrator'), 'verbose_name': 'Слово', 'verbose_name_plural': 'Слов'},
        ),
        migrations.AddField(
            model_name='word',
            name='forms_of_word',
            field=models.ManyToManyField(to='LEW_app.word'),
        ),
    ]