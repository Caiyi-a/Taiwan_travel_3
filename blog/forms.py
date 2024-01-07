from django import forms
from .models import Comment

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        max_length=20, 
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    
class WriteForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ('projectName', 'location', 'image', 'article',)

        widgets = {
            'projectName': forms.TextInput(),
            'location': forms.TextInput(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'article': forms.TextInput(),
        }