from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    from start import nltkProcessing
    from GSearch import peopleAskFor
    from extraction import aboutInfo

    name = 'Lewis Hamilton'
    image_url = nltkProcessing(name)
    about = aboutInfo(name)
    people_Ask_For = peopleAskFor(name)
    context = {
        'names': name,
        'about': about,
        'img': image_url,
        'people_ask_for': people_Ask_For
    }
    return render(request, "home.html", context)


def google_view(request, *args, **kwargs):
    context = []
    return render(request, "google.html", context)
