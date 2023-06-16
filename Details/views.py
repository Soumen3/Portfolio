from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'activeHome':'active-tab'
    }
    return render(request, 'home.html', context)


def about(request):
    context={
        'activeAbout':'active-tab'
    }
    return render(request, 'about.html', context)


def skill(request):
    context={
        'activeSkills':'active-tab'
    }
    return render(request, 'skills.html', context)


def project(request):
    context={
        'activeProjects':'active-tab'
    }
    return render(request, 'project.html', context)


def contact(request):
    context={
        'activeContact':'active-tab'
    }
    return render(request, 'contact.html', context)