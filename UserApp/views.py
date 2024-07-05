from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyModel
from .serializers import MyModelSerializer


class MyModelListUpdateView(APIView):
    def get(self, request):
        mymodels = MyModel.objects.all()

        # Update each instance of MyModel with fixed values
        for model in mymodels:
            model.name = "omon"
            model.value = 21112
            model.save()


        serializer = MyModelSerializer(mymodels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


