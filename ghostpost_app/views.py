from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost_app.models import GhostPost
from ghostpost_app.forms import GhostPostForm

def index(request):
    data = GhostPost.objects.all()
    return render(request, 'index.html', {"data": data})

def postadd(request):
    if request.method == 'POST':
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                is_boast = data['is_boast'],
                post = data['post']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = GhostPostForm()
    return render(request, "form.html", {"form": form})

def boast(request):
    data = GhostPost.objects.filter(is_boast=True)
    return render(request, "index.html", {"data": data})

def roast(request):
    data = GhostPost.objects.filter(is_boast=False)
    return render(request, "index.html", {"data": data})

def upvote(request, id):
    post = GhostPost.objects.get(id=id)
    post.up_votes += 1
    post.save()
    # https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def downvote(request, id):
    post = GhostPost.objects.get(id=id)
    post.down_votes += 1
    post.save()
    # https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def pop_vote(request):
    posts = list(GhostPost.objects.all())
    posts.sort(key=lambda p: p.total_votes, reverse=True)
    return render(request, "index.html", {"data": posts})

def boastview(request, id):
    post = GhostPost.objects.get(id=id)
    boasts = GhostPost.objects.filter(is_boast=True)
    return render(request, "boasts.html", {"boasts": boasts, "post": post})

def roastview(request, id):
    post = GhostPost.objects.get(id=id)
    roasts = GhostPost.objects.filter(is_boast=False)
    return render(request, "roasts.html", {"roasts": roasts})


