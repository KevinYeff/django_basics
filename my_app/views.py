from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about(request):
    return HttpResponse("about")

@csrf_exempt
def projects(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name_of_project = data.get('name')

            if not name_of_project:
                return JsonResponse({
                    'error': 'Name for project missing'
                    }, safe=False, status=400)
            elif name_of_project == '':
                return JsonResponse({
                    'error': 'Name of project cannot be empty'
                    }, safe=False, status=400)
            elif not isinstance(name_of_project, str):
                return JsonResponse({
                    'error': 'Name of project must be a string'
                    }, safe=False, status=400)

            projects = Project(name=name_of_project)
            projects.save()
            dict_of_Project_object = model_to_dict(projects)
            return JsonResponse(dict_of_Project_object, safe=False, status=200)

        except DatabaseError as e:
            return JsonResponse({
                'error': 'Data base error: ' + str(e)
                }, safe=False, status=500)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
                }, safe=False, status=500)

    elif request.method == 'GET':
        try:
            projects = Project.objects.all()
            if not projects:
                return JsonResponse({
                    'message': 'First look, DataBase is empty'
                    }, safe=False, status=204)

            list_of_projects = list(projects.values())
            return JsonResponse(list_of_projects, safe=False, status=200)

        except DatabaseError as e:
            return JsonResponse({
                'error': 'Data base Error: ' + str(e)
                }, safe=False, status=500)

        except ObjectDoesNotExist:
            return JsonResponse({
                'error': 'No projects found'
                }, safe=False, status=404)

        except Exception as e:
            return JsonResponse({
                'error': str(e)
                }, safe=False, status=500)
    else:
        return JsonResponse({
            'error': 'Method not allowed, GET or POST requests only'
            }, safe=False, status=405)
