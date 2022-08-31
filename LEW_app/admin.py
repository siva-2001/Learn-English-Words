from django.contrib import admin
from django.urls import reverse
from .models import Word
from django.utils.html import format_html
from django.utils.http import urlencode



@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('view_word', 'view_language', 'view_word_verified', 'view_translate', 'view_forms')
    list_filter =  ('word_verified_by_administrator',)

    @admin.display(description='Переводы', ordering='translates')
    def view_translate(self, obj):
        count = obj.translates.count()
        url = (
            reverse('admin:LEW_app_word_changelist')
            + "?"
            + urlencode({"translates__id":f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} {}</a>', url, count, obj.get_plural(count))

    @admin.display(description='Формы', ordering='forms_of_word')
    def view_forms(self, obj):
        count = obj.forms_of_word.count()
        url = (
            reverse('admin:LEW_app_word_changelist')
            + "?"
            + urlencode({"forms_of_word__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {} {}</a>', url, count, obj.get_plural(count))

    @admin.display(description='Слово', ordering='word')
    def view_word(self, obj):
        return obj.word

    @admin.display(description='Язык', ordering='language')
    def view_language(self, obj):
        return obj.get_language_display()

    @admin.display(description='Слово подтверждено администратором', ordering='word_verified_by_administrator')
    def view_word_verified(self, obj):
        return  obj.word_verified_by_administrator


    #   https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    #   Создание сложных фильтров



