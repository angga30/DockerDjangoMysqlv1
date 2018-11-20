from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title':'Blog NeoTraveler',
        'heading':'Blog',
        'subheading':'Sepenggal kisah perjalanan'
    }
    return render(request,'blog/index.html',context)