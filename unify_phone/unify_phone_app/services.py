import re
import json


class IncorrectRequestException(Exception):
    """Occurs when request incorrect"""
    pass


def unify_phone(phone):
    numbers = re.findall('\d', phone)
    if not len(numbers):
        raise IncorrectRequestException 
    if len(numbers) > 11 or len(numbers) < 10 or numbers[-10] != '9':
        return "".join(numbers)       
    format_phone = '8 (9{}{}) {}{}{}-{}{}-{}{}'.format(*numbers[-9:])
    return format_phone


def get_phone_from_json(request):
    try:
        phone = json.loads(request.body.decode('utf-8'))["phone"]
        return phone
    except KeyError:
        raise IncorrectRequestException


def get_phone_from_query(request):
    try:
        phone = request.GET.get("phone")
        if phone:
            return phone
        else:
            raise IncorrectRequestException
    except KeyError:
        raise IncorrectRequestException


def get_phone_from_cookies(request):
    try:
        phone = request.COOKIES["phone"]
        if phone:
            return phone
        else:
            raise IncorrectRequestException
    except KeyError:
        raise IncorrectRequestException