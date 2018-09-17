from django.shortcuts import render

def index(request) :
    return render(request, 'personal/home.html')


def contact(request) :
    # takes request, what you're gonna render, and optionally a dict
    return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, please email me at ', 'douglas12219@gmail.com']})

