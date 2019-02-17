from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
# Create your views here.
def home(request):
	all_posts = Post.objects.all()
	return render(request, "home.html",{'all_posts': all_posts})

def create_post(request):
	if request.method == "POST":
		form_title = request.POST['title']
		form_body = request.POST['body']
		new_post = Post.objects.create(title = form_title, body = form_body)
		return redirect(f"/post/{new_post.id}/")


	return render(request, "create_post.html")


def post_page(request, post_id):
	post = Post.objects.get(id = post_id)	
	return render(request, "page.html", {"post":post})	


 