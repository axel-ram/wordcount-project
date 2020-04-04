from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request, 'home.html')

def count(request):
    recievedText = request.GET['fulltext']
    wordlist = recievedText.split()

    wordDictionary = {}
    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    return render(request, 'count.html', {
        'recievedText' : recievedText,
        'wordscount' : len(recievedText.split()),
        'sortedDictionary' : sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True),
    })

def about(request):
    return render(request, 'about.html')
