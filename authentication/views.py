from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
import requests

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
        response = self._get_token(request, data)
        return Response(response, status=201)

    def _get_token(self, request, data):
        path = reverse('token_obtain_pair')
        url = request.build_absolute_uri(path)
        response = requests.post(url, data)
        return response.json()
