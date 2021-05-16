from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from . models import *
from . forms  import *

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request,'blog/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})



def post_list(request, tag_slug=None):
       posts = Post.objects.all()
       tag = None
       if tag_slug:
              tag = get_object_or_404(Tag, slug = tag_slug)
              posts = posts.filter(tags__in=[tag])

       paginator = Paginator(posts, 2)
       page_number = request.GET.get('page')
       page_obj = paginator.get_page(page_number)       
       context={'posts' : posts,
                'page_obj': page_obj,
                'tag':tag }
       return render(request,'blog/home.html',context)

def same_post_tag(request, tag_slug=None):
       posts = Post.objects.all()
       tag = None
       if tag_slug:
              tag = get_object_or_404(Tag, slug = tag_slug)
              posts = posts.filter(tags__in=[tag])
       context = {'posts':posts}       
       return render(request,'blog/SamePostTag.html' ,context)      



def post_detail(request, slug):
       post = get_object_or_404(Post, slug=slug)
       return render(request,'blog/post_detail.html',{'post':post})


def shar_post(request, post_id):
       post = get_object_or_404(Post, id=post_id)
       sent = False
       if request.method == 'POST':
              form = EmailPostForm(request.POST)
              if form.is_valid():
                     cd = form.cleaned_data
                     subject = "Recommanded to read this post" f"{post.title}"
                     message = f"{ post.body }" 
                     send_mail (subject, message,'mohammedalihamza77@gmail.com',[cd['to']])    
                     sent = True
       else:
              form = EmailPostForm()
              return render(request, 'blog/share.html', {'post': post,'form': form ,'sent': sent})                

def ContactUs(request):
       form  =ContactForm(request.POST or None)
       sent = False
       if form.is_valid():
              cd = form.cleaned_data
              name = form.cleaned_data.get('name')
              subject = f' Message from {name} '
              message = form.cleaned_data.get('message')
              fromm = form.cleaned_data.get('email')
              send_mail (subject, message,fromm,['mohammedalihamza77@gmail.com'])    
              sent = True
       return render(request, 'blog/contact.html', {'form': form ,'sent': sent})        
              
    
    
    
