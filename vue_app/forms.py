from django import forms
from django.utils import timezone

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

class NewUser(forms.Form):
    email = forms.EmailField()
    pwd = forms.PasswordInput()

    def create_user(self):
        pass  # TODO




