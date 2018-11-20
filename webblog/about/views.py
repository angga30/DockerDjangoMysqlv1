from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'About Me',
        'heading':'About Me',
        'subheading':'mengenal adalah jiwa-jiwa kesatria'
    }
    return render(request,"about/index.html",context)