from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306226914',
        'name': 'William Alexander',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)