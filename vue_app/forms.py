from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post

class NewPost(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=10000)

    def create_post(self):
        post = Post(
            title=self.cleaned_data['title'],
            pub_date=timezone.now(),
            description=self.cleaned_data['description']
        )

        post.save()

        return post.id

class NewUserForm(UserCreationForm):
    email = forms.EmailField()


    gender = forms.ChoiceField(choices =
        (
            (1, "female"),
            (2, "male"),
            (3, "others"),
            (4, "prefer not to say")
        )
    )
    #studies # TODO

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



