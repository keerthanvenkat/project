from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage
from mysite.settings import BASE_DIR
from .models import Post
from .forms import ContactForm,PostForm
# Create your views here.
#def hello_world(request):
#	return HttpResponse("hello world \n")
	#day3
#def test_html(request):
#	f = open( BASE_DIR + '/blog/templates/test.html')
#	content = f.read()
#	return HttpResponse(content)
	#passing content
#def test_html(request):
#		context = {}
#		return render(request,'test.html',context)

#day4
#def address(request):
#	context = {}
#	return render(request,'address/address.html',context)
#day4
#def address1(request):
#	context = {'namesdb':[{'name':'student11','email':''},{'name':'student12','email':'student12@gmail.com'}]}
#	return render(request,'address/address1.html',context)

#day6(url settings)
def post_list(request):
	posts = Post.objects.all()
	#print posts
	context = {'namesdb' : posts}
	return render(request,'blog/post_list.html',context)

#day7
#def address_test(request):
#	context = {}
#	return render(request,'address/new_address.html',context)
def home(request):
	context = {}
	return render(request,'blog/home.html',context)

def home(request):
	posts = Post.objects.all()
	#print posts
	context = {'namesdb' : posts}
	#context = {}
	return render(request,'blog/home.html',context)


def contact(request):
	form = ContactForm
	context = {'form':form}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		print dir(form)
		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			subject = ' A new lead - Contact Information {}'.format(contact_name)
			contact_email = form.cleaned_data['contact_email']
			content = form.cleaned_data['content']
			email = EmailMessage(subject,contact_name + '\n' + contact_email + '\n' + content, to=['tuxfux.hlp@gmail.com'])
			email.send()
			return HttpResponseRedirect('/blog/thanks/')

## what if form is not valid
		else:
			context = {'form':form}
			return render(request,"blog/ContactForm.html",context)

	return render(request,'blog/ContactForm.html',context)

def thanks(request):
	return HttpResponse("Thank you and Have a great day !!!")

# def modular views
def Postview(request):
	form = PostForm()
	context = {'form':form}
	if request.method == 'POST':
		form = PostForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			author = form.cleaned_data['author']
			email  = form.cleaned_data['email']
			title  = form.cleaned_data['title']
			text   = form.cleaned_data["text"]
			created_date = form.cleaned_data['created_date']
			print author,email,title,text,created_date
			Post.objects.create(author=author,email=email,title=title,text=text,created_date=created_date)
			#print title,text
			return HttpResponseRedirect('/blog/thanks/')

				## what if form is not valid
		else:
			context = {'form':form}
			return render(request,"blog/PostForm.html",context)

	return render(request,"blog/PostForm.html",context)

def thanks(request):
	return HttpResponse("Thank you and Have a great day !!!")