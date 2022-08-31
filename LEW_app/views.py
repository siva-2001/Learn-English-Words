from django.shortcuts import render
from .forms import newWordForm
from .models import Word
from .exception import WordIsExistException, WrongStringException
from .functions import stringConsistEngOnly, stringConsistRusOnly
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


def homeView(request):
    return render(request, "homePage.html")

@login_required
def createWordView(request):
    form = newWordForm()
    if request.method == "GET":
        return render(request, "createWord.html", {"form":form})
    else:
        try:
            form = newWordForm(request.POST)
            if form.is_valid():
                all_words_str = [word.word for word in Word.objects.all()]
                if form['word'].value().title() in all_words_str:
                    raise WordIsExistException
                if ' ' in form['word'].value():
                    raise WrongStringException("too many words")
                if (form['language'].value() == Word.ENG and \
                    not stringConsistEngOnly(form['word'].value())) \
                    or (form['language'].value() == Word.RU and \
                    not stringConsistRusOnly(form['word'].value())):
                    raise WrongStringException("incorrect characters are used")
                new_word = form.save(commit=False)
                new_word.word = new_word.word.title()
                new_word.save()
        except WordIsExistException:
            return render(request, "createWord.html", {"form": form, 'error': "word_is_exist"})
        except WrongStringException:
            return render(request, "createWord.html", {"form": form, 'error': "wrong string"})
        else:
            return render(request, "createWord.html", {"form":form, 'error':"form saved"})

