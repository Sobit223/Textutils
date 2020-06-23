# this file is created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    Newlineremover = request.POST.get('Newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')


    if removepunc == "on":

        analyzed = ""
        punctuations = '''!()-[];:{}'"/\@@#$%^&*_'''
        for char in text:

            if char not in punctuations:

                analyzed = analyzed + char

        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        text = analyzed

    # analyze the text

    if(fullcaps == 'on'):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}

            # analyze the text
        text = analyzed
    if(Newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}
        text = analyzed
    if(extraspaceremover=='on'):
        analyzed=""
        for index , char in enumerate(text):
            if not (text[index] == " " and text[index +1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        text = analyzed

    elif(charcount=='on'):
        a = (len(text))
        params = {'purpose': 'charcount', 'analyzed_text': a}
    if(removepunc != "on" and Newlineremover!="on" and extraspaceremover!="on" and charcount!="on" and fullcaps!="on"):
        return  HttpResponse("Please select the operation")



    return render(request , 'analyze.html', params)














