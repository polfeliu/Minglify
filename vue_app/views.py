from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import login as user_login
from django.contrib import messages

from vue_app.models import Post
from vue_app.forms import NewPost, NewUserForm, AuthenticationForm, NewBoarding

# TODO Protect view from unauthenticated users

def feed(request):
    context = {
        "posts": Post.objects.order_by('-pub_date').all()
    }

    return render(request, 'app/feed.html', context)

def profile(request):
    return render(request, 'registration/profile.html')

def new_user(request):

    context = {

    }

    return render(request, 'app/new_user.html', context)

def register_FORM(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
            return redirect("/feed")
        messages.error(request, form.error_messages)
    form = NewUserForm
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def post(request, post_id):

    if Post.objects.filter(id=post_id).exists():
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
            'is_user_boarded': post.is_user_boarded(request.user)
        }

        if request.method == "POST":
            form = NewBoarding(request.POST)
            if form.is_valid():
                form.create_boarding(
                    post=context['post'],
                    user=request.user
                )

                context = {
                    'post': post,
                    'is_user_boarded': post.is_user_boarded(request.user)
                }

        return render(request, 'app/post.html', context)
    else:
        return HttpResponseRedirect('/Error')

def new_post(request):
    return render(request, 'app/new_post.html')


def landing(request):
    return render(request, 'landing.html')

def new_post_FORM(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPost(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post_id = form.create_post()
            # redirect to a new URL:
            return HttpResponseRedirect(f'/post/{post_id}')

        else:
            return HttpResponseRedirect('/Error/')

    else:
        return HttpResponseRedirect('/Error/')
        # TODO Return Error View

