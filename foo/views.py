from django.shortcuts import render
from .models import Foo, FooForm
from django.forms.models import modelform_factory
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	list_of_foos = Foo.objects.all()
	form = FooForm()
	logged_in = True if request.user.is_authenticated() else False
	context = {'items': list_of_foos,
				'form': form,
				'logged_in': logged_in,}
	return render(request, 'foo/index.html', context)


@login_required
def add(request):
	# get data from POST
	bar = request.POST['bar']
	user = request.user
	now = timezone.now()
	new_foo = Foo(bar=bar,author=user,date_added=now)
	#instantiate bound model form
	f = FooForm({'bar': bar, 'author': user, 'date_added': now })
	if f.is_valid():
		new_foo.save()
	context = {'form':f, 'foo': new_foo}
	return render(request, 'foo/add.html', context)