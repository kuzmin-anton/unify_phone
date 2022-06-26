from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .forms import PhoneForm

from .services import IncorrectRequestException, unify_phone, get_phone_from_json,\
    get_phone_from_cookies, get_phone_from_query


@csrf_exempt 
def unify_phone_from_json(request):
    if request.method == 'POST':
        try:
            phone = get_phone_from_json(request)
            formatted_phone = unify_phone(phone)
            return HttpResponse(formatted_phone)
        except IncorrectRequestException:
            return HttpResponseBadRequest('Bad Request')
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt 
def unify_phone_from_form(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            try:
                phone = form.cleaned_data['phone']
                formatted_phone = unify_phone(phone)
                return HttpResponse(formatted_phone)
            except IncorrectRequestException:
                return HttpResponseBadRequest('Bad Request')
        else:
            return HttpResponseBadRequest('Bad Request')
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt 
def unify_phone_from_query(request):
    if request.method == 'GET':
        try:
            phone = get_phone_from_query(request)
            formatted_phone = unify_phone(phone)
            return HttpResponse(formatted_phone)
        except IncorrectRequestException:
            return HttpResponseBadRequest('Bad Request')
    else:
        return HttpResponseNotAllowed(['GET'])


@csrf_exempt
def unify_phone_from_cookies(request):
    if request.method == 'GET':
        try:
            phone = get_phone_from_cookies(request)
            formatted_phone = unify_phone(phone)
            return HttpResponse(formatted_phone)
        except IncorrectRequestException:
            return HttpResponseBadRequest('Bad Request')
    else:
        return HttpResponseNotAllowed(['GET'])
    
