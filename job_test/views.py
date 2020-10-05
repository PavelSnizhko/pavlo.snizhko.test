from django.http import JsonResponse

from job_test.api_service import APIHandler


def get(request):
    api_obj = APIHandler(url='https://www.magetic.com/c/test?api=1&amp;name=', token='pavel_snizhko')
    data = api_obj.build_jason(api_obj.get_all_games())
    return JsonResponse(data, status=200, safe=False)