from django.shortcuts import render_to_response
from links.forms import ContactForm
from links.models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    links = Link.objects.filter(current=True).order_by('last_accessed')[:10]
    categories = Categories.objects.all().order_by('name')
    return render_to_response('index.html', {'links': links, 'categories':categories})

def category(request, cat_name):
    Category = get_object_or_404(Categories, name__iexact=cat_name.replace("%20", ""))
    categories = Categories.objects.all().order_by('name')
    return render_to_response('category.html',
        {'Category': Category, 'links': Category.link_set.all().order_by('-views'), 'categories':categories})

def view(request, link_id, up):
	'''clicking on a link-viewingit:'''
	link = get_object_or_404(Link, pk=int(link_id))
	if link.last_accessed.date() < datetime.today().date():
		link.views += up
		link.last_accessed = datetime.now()
		link.save()
	return HttpResponseRedirect(link.url)
	
def current(request, link_id):
	'''toggle link.current'''
	link = get_object_or_404(Link, pk=int(link_id))
	if link.current == True:
		link.current = False
	else:
		link.current = True
	link.save()
	return HttpResponseRedirect("/")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'danhorton0@gmail.com'),
                ['danhorton0@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
	
def thanks(request):
	return render('thanks.html')
