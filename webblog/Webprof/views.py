from django.shortcuts import render


def index(request):
    context = {
        'title':'NeoTravler',
        'heading':'NeoTraveler',
        'subheading':'Pastikan Anda Tersesat di rencanakan'
    }
    return render(request,'index.html',context)