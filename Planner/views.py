from django.http import FileResponse, Http404
import os
from conf import BASE_DIR
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import ItemsToPlanSerializer
# from Scheduler.views import F1ManList


class ItemsToPlanList(APIView):

    def get(self, request):
        f1man = ItemsToPlan.objects.all()
        serializer = ItemsToPlanSerializer(f1man, many=True)
        return Response(serializer.data)


def pdf_view(request, filename):

    nfn = f'{filename[0:7]} {filename[7:]}.pdf'
    filepath = os.path.join(BASE_DIR, filename[0:7], nfn)

    if os.path.exists(filepath):
        return FileResponse(open(filepath, 'rb'), as_attachment=False, content_type='application/pdf')
    raise Http404()

def main():
    pass

if __name__ == '__main__':
    main()
