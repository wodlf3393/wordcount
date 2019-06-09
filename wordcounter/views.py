from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1

    return render(request, 'count.html', {'full': text, 'total':len(words), 'words':word_dictionary.items})

def home2(request):
    full = request.GET['full']
    return render(request, 'home2.html', {'fulll': full})