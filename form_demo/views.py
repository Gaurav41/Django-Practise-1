from django.http.response import HttpResponse
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            name = form.cleaned_data['your_name']
            # redirect to a new URL:
            # name="sd"
            return HttpResponse(f'thanks {name}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form_demo/name.html', {'form': form})