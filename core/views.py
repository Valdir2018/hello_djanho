from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse(resultado)
