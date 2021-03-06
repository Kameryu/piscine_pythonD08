from django.shortcuts import render

from .forms import FileForm
from .models import File

# Create your views here.

def index(request):
	files = File.objects.all()
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = FileForm()
	return render(request, "ex00/index.html", {'form' : form, 'files': files})
