from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from taggit.models import Tag

#using class based view
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

#views for urls
def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug )
        object_list = object_list.filter(tag__in=[tag])
    paginator = Paginator(object_list, 3) #3 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render (request, 'blog/post/list.html',{'page':page,'posts':posts,'tag':tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',publish__year=year,publish__month=month,publish__day=day)
    #List of active comments for the post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        #a comment was submitted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #create comment object but dont save to databaase
            new_comment = comment_form.save(commit=False)
            #assign the current comment to post
            new_comment.post = post
            #save the comment to database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'blog/post/detail.html',{'post':post, 'comments': comments, 'comment_form' : comment_form})

#sending email
from django.core.mail import send_mail

def post_share(request,post_id):
    #retreive post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        #form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #form field passed validation
            cd = form.cleaned_data
            post_url= request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
            #....send mail
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',{'post':post,'form':form,'sent':sent, 'cd':cd}) 