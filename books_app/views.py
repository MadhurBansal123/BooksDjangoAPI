import json
from datetime import datetime, timezone

import requests
from django.http import JsonResponse, HttpResponseNotFound
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
def books_operation(request):
    if request.method == 'GET':
        result = {"status_code": 200, "status": "success", "data": list(Book.objects.all().values())}
        return JsonResponse(result)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        new_book_body = json.loads(body_unicode)
        new_book = Book(**new_book_body)
        new_book.save()
        result = {"status_code": 201, "status": "success", "data": new_book_body}
        return JsonResponse(result)
    else:
        return HttpResponseNotFound(JsonResponse({"status_code": 404, "status": "failure", "data": {}}))


@csrf_exempt
def book_operation_by_id(request, bookId):
    try:
        book = Book.objects.get(pk=bookId)
        if request.method == 'GET':
            result = {"status_code": 200, "status": "success", "data": model_to_dict(book)}
            return JsonResponse(result)
        elif request.method == 'PATCH' or request.method == 'PUT':
            body_unicode = request.body.decode('utf-8')
            updated_book_body = json.loads(body_unicode)
            for key, value in updated_book_body.items():
                setattr(book, key, value)
            book.save()
            book_dict = model_to_dict(book)
            result = {"status_code": 200, "status": "success",
                      "message": "The book " + book_dict['name'] + " was updated successfully", "data": book_dict}
            return JsonResponse(result)
        elif request.method == 'DELETE':
            book_dict = model_to_dict(book)
            book.delete()
            result = {"status_code": 200, "status": "success",
                      "message": "The book " + book_dict['name'] + " was deleted successfully", "data": {}}
            return JsonResponse(result)
        else:
            return HttpResponseNotFound(JsonResponse({"status_code": 404, "status": "failure", "data": {}}))
    except Book.DoesNotExist:
        return JsonResponse(
            {"status_code": 200, "status": "success", "message": "book not found for id:" + str(bookId), "data": {}}
        )


@csrf_exempt
def external_api_operations(request):
    fire_and_ice_api = 'https://www.anapioficeandfire.com/api/books'
    name = request.GET.get('name', '')
    if name != '':
        fire_and_ice_api += ('/?name=' + name)
    response = requests.get(fire_and_ice_api).json()

    for i in range(len(response)):
        response[i]['number_of_pages'] = response[i]['numberOfPages']
        response[i]['release_date'] = datetime.fromisoformat(response[i]['released']).astimezone(timezone.utc).date()
        del response[i]['url']
        del response[i]['characters']
        del response[i]['mediaType']
        del response[i]['povCharacters']
        del response[i]['released']
        del response[i]['numberOfPages']

    result = {"status_code": 200, "status": "success", "data": response}
    return JsonResponse(result, safe=False)
