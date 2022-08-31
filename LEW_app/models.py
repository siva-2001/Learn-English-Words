from django.db import models

class Word(models.Model):
    class Meta:
        ordering = ('word', 'word_verified_by_administrator')
        verbose_name = "Word"
        verbose_name_plural = "Words"

    def __str__(self):
        return self.word

    def get_plural(self, num):
        if num % 10 == 1:
            return 'слово'
        elif num % 10 in (2, 3, 4):
            return 'слова'
        else:
            return 'слов'

    RU = 'RU'
    ENG = 'ENG'
    VERBOSE_NAMES = {
        "ONE":"Слово",
        "FP": "Слова",
        "SP": "Слов",
    }

    LANGS = [
        (RU, "Русский"),
        (ENG, 'English')
    ]
    PARTS = [
        ("N", "Существительное | Noun"),
        ("ADJ","Прилагательное | Adjective"),
        ("NUM", "Числительное | Numeral"),
        ("PRN", "Местоимение | Pronoun"),
        ("V", "Глагол | Verb"),
        ("ADV", "Наречие | Adverb"),
        ("PRT", "Причастие | Participle"),
        ("PT", "Предлог | Pretext"),
        ("U", "Союз | Union"),
        ("I", "Междометие | Interjection"),

        ("PRE", "Предикатив"),
        ("DEP", "Деепричастие"),
        ("CH","Частица"),
        ("MOD", "Модальные слова"),
    ]
    word = models.CharField(max_length=128)
    language = models.CharField(max_length=3, choices=LANGS)
    part_of_speech = models.CharField(max_length=3, choices=PARTS)
    image_file = models.FileField(upload_to="images/", blank=True)
    voice_file = models.FileField(upload_to="voices/", blank=True)
    word_verified_by_administrator = models.BooleanField(default=False)
    image_verified_by_administrator = models.BooleanField(default=False)
    translates = models.ManyToManyField("self")
    forms_of_word = models.ManyToManyField("self")



