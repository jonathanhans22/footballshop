from django.shortcuts import render


def show_main(request):
    context = {
        'npm' : '2406414025',
        'name': 'Jonathan Hans Emanuelle',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)