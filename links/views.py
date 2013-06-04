from django.shortcuts import render_to_response
from links.models import *
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from datetime import datetime

def index(request):
    links = Link.objects.all().order_by('-views')[:20]
    categories = Categories.objects.all()
    return render_to_response('index.html', {'links': links, 'categories':categories})

def view(request, link_id, up):
    link = get_object_or_404(Link, pk=int(link_id))
    link.views += up
    link.last_accessed = datetime.now()
    link.save()
    return HttpResponseRedirect(link.url)

def category(request, cat_name):
    Category = get_object_or_404(Categories, name__iexact=cat_name)
    return render_to_response('category.html',
        {'Category': Category, 'links': Category.link_set.all()})
