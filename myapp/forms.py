from myapp.models import User, Post
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "password", "email",
                  "first_name", "last_name", "user_img")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "user_img": forms.FileInput(attrs={"class": "form-control"}),
        }

    def clean_password(self):
        data = self.cleaned_data["password"]
        if len(data) < 8:
            raise forms.ValidationError("password must be more than 8 digits")
        return data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), required=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "img")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "img": forms.FileInput(attrs={"class": "form-control"}),
        }


class CommentFrom(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(), required=True)
