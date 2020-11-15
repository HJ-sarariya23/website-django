from django.shortcuts import render, HttpResponse , redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post, Category
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.utils import timezone



def home(request):
    # allPosts = Post.objects.all()
    # context = {'allPosts' : allPosts}
    lts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-timestamp')[0:8]
    top_five_post = Post.objects.all().order_by('-views')[0:5]
    context = {'allPosts' :top_five_post, 'lts':lts}
    return render(request, "home/home.html",context)

def contact(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            content = request.POST['content']
            if len(name)<3 or len(email)<5 or len(phone)<6 or len(content)<4:
                messages.error(request, "Please fill form correctly")   
            else:    
                contact =  Contact(name=name , email = email , phone=phone , content=content)
                contact.save()
                messages.success(request, "Your massage has been successfully sent!")
        return render(request, 'home/contact.html')

def privacy(request):
    return render(request, 'home/privacy.html')
def termandconditions(request):
    return render(request, 'home/term&conditions.html')
def disclaimer(request):
    return render(request, 'home/disclaimer.html')

def search(request):
    query = request.GET['query']
    if len(query)<1:
        allPosts= Post.objects.none() 
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent  = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent).order_by('-published_date')

    if allPosts.count() == 0:
         messages.warning(request, "No results found. Please refine your query!")
    params = {'allPosts' : allPosts, 'query' : query}
    return render(request, "home/search.html", params) 



def handlesignup(request):
    if request.method == 'POST':
        # Get the post perameter
        username =  request.POST['username']
        email = request.POST['email']
        if len(username) > 8:
            messages.error(request, "Username must be under 8 characters.")
            return redirect('home')


        if not username.isalnum():
            messages.error(request , "Username shoud only contain letters and numbers.")
            return redirect('home')

        myuser = User.objects.create_user(username , email)
        myuser.save()
        messages.success(request, "Your  account has been successfully created !")
        return redirect('home')
    else :
        return HttpResponse("404 = Not found Error")    


    