from django import forms

from .models import Word

class newWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'language', 'part_of_speech']#, 'image']
        widgets = {
            "word":forms.widgets.TextInput(attrs={
                "word_id":"word_id",
                'placeholder':"Слово",
                "class":"form-control"


            }),
            "language":forms.widgets.RadioSelect(attrs={
                "id":"language_id",
                "class": "form-control"

            },
                choices= Word.LANGS
            ),
            "part_of_speech": forms.widgets.RadioSelect(attrs={
                "id": "part_id",
                "class": "form-control"
            },
                choices=Word.PARTS
            ),
        }

