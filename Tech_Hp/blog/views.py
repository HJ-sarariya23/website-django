from django.shortcuts import render, HttpResponse , redirect
from .models import Post, BlogComment   
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
from django.utils import timezone

def bloghome(request):
    allPosts = Post.objects.all().order_by('-published_date')
    context = {'allPosts':allPosts}
    return render(request , 'blog/bloghome.html',context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views=post.views + 1
    post.save()

    lts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-timestamp')[0:5]
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}

    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    
    context = {'post':post , 'comments':comments, 'user': request.user, 'replyDict': replyDict, 'lts':lts}
    return render(request , 'blog/blogpost.html',context)

def Category(request,cats):

    category_posts = Post.objects.filter(category=cats).order_by('-published_date')
    context = {'cats': cats, 'category_posts':category_posts}
    return render(request, 'blog/category.html',context)



def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user,post=post)
            comment.save()
            # messages.success(request, "Your comment has been posted successfully")

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user,post=post, parent=parent)
            comment.save()
            # messages.success(request, "Your reply  has been posted successfully")



        return redirect(f"/blog/{post.slug}")
