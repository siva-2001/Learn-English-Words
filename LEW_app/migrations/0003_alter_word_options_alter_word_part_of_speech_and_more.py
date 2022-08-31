# Generated by Django 4.1 on 2022-08-30 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LEW_app', '0002_rename_image_word_image_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ('word', 'word_verified_by_administrator')},
        ),
        migrations.AlterField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(choices=[('N', 'Существительное | Noun'), ('ADJ', 'Прилагательное | Adjective'), ('NUM', 'Числительное | Numeral'), ('PRN', 'Местоимение | Pronoun'), ('V', 'Глагол | Verb'), ('ADV', 'Наречие | Adverb'), ('PRT', 'Причастие | Participle'), ('PT', 'Предлог | Pretext'), ('U', 'Союз | Union'), ('I', 'Междометие | Interjection'), ('PRE', 'Предикатив'), ('DEP', 'Деепричастие'), ('CH', 'Частица'), ('MOD', 'Модальные слова')], max_length=3),
        ),
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='english_word', to='LEW_app.word')),
                ('ru_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='russian_word', to='LEW_app.word')),
            ],
        ),
    ]
