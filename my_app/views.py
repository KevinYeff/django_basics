from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about(request):
    return HttpResponse("about")

def projects(request):
    if request.method == 'GET':
        try:
            p = list(Project.objects.values())

            if not p:
                return JsonResponse({'message': 'First look, DataBase is empty'}, safe=False, status=204)
            return JsonResponse(p, safe=False)

        except DatabaseError as e:
            return JsonResponse({'error': 'Data base Error: ' + str(e)}, status=500)

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'No projects found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed, GET requests only'}, status=405)
