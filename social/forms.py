from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=20,label="Name",widget=forms.TextInput(attrs={'class':'form-input','placeholder':'Name'}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-input','placeholder':'example@gmail.com'}))
    subject = forms.CharField(max_length=20,label="Subject",widget=forms.TextInput(attrs={'class':'form-input','placeholder':'Subject'}))
    body = forms.CharField(label='Body',widget=forms.Textarea(attrs={'class':'form-input','placeholder':'Enter your message'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'): 
            raise forms.ValidationError("please just use gmail.")
        return email