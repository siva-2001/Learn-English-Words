from django.db import models

class Word(models.Model):
    LANGS = [
        ('RU', "Русский"),
        ("ENG", 'English')
    ]
    PARTS = [
        ("N", "Существительное | Noun"),
        ("ADJ","Прилагательное | Adjective"),
        ("NUM", "Числительное | Numeral"),
        ("PRN", "Местоимение | Pronoun"),
        ("V", "Глагол | Verb"),
        ("ADV", "Наречие | Adverb"),
        ("PRT", "Причастие | Participle"),

        ("PRE", "Предикатив"),
        ("DEP", "Деепричастие"),

        ("PT", "Предлог | Pretext"),
        ("U", "Союз | Union"),
        ("I", "Междометие | Interjection"),

        ("CH","Частица"),
        ("MOD", "Модальные слова"),


    ]
    word = models.CharField(max_length=128)
    language = models.CharField(max_length=3, choices=LANGS)
    part_of_speech = models.CharField(max_length=3, choices=PARTS, blank=True)
    image = models.FileField(upload_to="images/", blank=True)