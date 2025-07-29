from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import F1ManSerializer

class F1ManList(APIView):

    def get(self, request):
        f1man = F1Man.objects.all()
        serializer = F1ManSerializer(f1man, many=True)
        return Response(serializer.data)