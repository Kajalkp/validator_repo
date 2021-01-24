from django import forms
class Feedback(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField()
    comments=forms.CharField()
    def clean_name(self):
        n=self.cleaned_data['name']
        if(len(n)>10):
            raise forms.ValidationError("Reenter name")
        return n
        