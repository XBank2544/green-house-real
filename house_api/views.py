from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.status import (
    HTTP_200_OK
)

from webapp.models import Schedule


@csrf_exempt
@api_view(["POST","GET"])
@permission_classes((AllowAny,))
def updateSchedule(request):
    data = {}
    msg = 'Success'
    http_status = HTTP_200_OK

    if request.data.get('fan_start') != "" and request.data.get('fan_start') != None:
        Schedule.objects.create(
            fan_start=request.data.get('fan_start'),
            fan_stop=request.data.get('fan_stop'),
            start_at=request.data.get('start_at'),
            end_at=request.data.get('end_at'),
            temp=request.data.get('temp'),
        )

    return Response({'status': True, 'message': msg, 'data': data}, status=http_status)
