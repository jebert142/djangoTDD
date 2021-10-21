from django.shortcuts import redirect, render
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash=text_hash)
           
    form = HashForm()
    return render(request, 'hashing/home.html', {'form':form})


def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request, 'hashing/hash.html', {'hash':hash})


def quickhash(request):
    text = request.GET.get('text')  #had to update this from 'request.GET' to 'request.GET.get' since the newest version of Django changed
    return JsonResponse({'hash':hashlib.sha256(text.encode('utf-8')).hexdigest()})