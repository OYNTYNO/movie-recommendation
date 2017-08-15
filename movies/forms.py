from django import forms

class MoviesForm(forms.Form):
    CHOICES = (
        ('1', '*',),
        ('2', '**',),
        ('3', '***',),
        ('4', '****',),
        ('5', '*****',),)
    post = forms.ChoiceField(widget=forms.RadioSelect,
        choices=CHOICES)
