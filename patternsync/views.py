from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt  

from syncapp.models import *
import json

def home(request):
	pattern = Pattern.objects.get(pk=1).pattern
	data = {
		'pattern': pattern
	}
	data = json.dumps(data)
	return HttpResponse(data)


@require_http_methods(["POST",])
@csrf_exempt
def update_pattern(request):
	code = request.POST['code']
	pattern = request.POST['pattern']

	code_exists = Code.objects.filter(code=code)
	if code_exists:
		pattern_obj = Pattern.objects.get(pk=1)
		pattern_obj.pattern = pattern
		pattern_obj.save()

		data = {
			'status': 'success',
			'pattern': pattern 
		}
		return HttpResponse(json.dumps(data))

	else:
		pattern = Pattern.objects.get(pk=1).pattern
		data = {
			'status': 'failure',
			'pattern': pattern 
		}
		return HttpResponse(json.dumps(data))