from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from authentication.serializers import RegisterSerializer

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=201)
