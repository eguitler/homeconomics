from django import forms

OPT_CHOICES = (
    ('1', 'opt 1'),
    ('2', 'opt 2'),
    ('3', 'opt 3'),
)

class myForm(forms.Form):
    text = forms.CharField(label="", initial="Enter text")
    option = forms.ChoiceField(choices=OPT_CHOICES)
