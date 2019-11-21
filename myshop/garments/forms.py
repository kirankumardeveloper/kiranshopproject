from django import forms
class ContactForm(forms.Form):
    contact_name=forms.CharField(label='enter your name',required = True)
    contact_email=forms.EmailField(label='enter email id',required = True)
    content=forms.CharField(label='your message here',required=True,widget=forms.Textarea)