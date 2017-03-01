from django.core.files.storage import FileSystemStorage
from django.db import transaction

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from FileUpload.models import Details


# Download image url will be:
# http://127.0.0.1:8000/images/file_image.png

class UploadFile(APIView):
    def post(self, request):
        for key in request.FILES:
            print(key, request.FILES[key])
        with transaction.atomic():
            image = request.FILES['image']
            filesystem = FileSystemStorage()
            filename = filesystem.save(image.name, image)
            uploaded_file_url = filesystem.url(filename)
            Details(name=request.data.get("name"), image=uploaded_file_url).save()
            return Response(status=200, data={"success": True, "image": uploaded_file_url})
