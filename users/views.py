from urllib import response
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import EmployeeSerializer, RegisterSerializer, ChangePasswordSerializer
from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from .models import Employee

# Register API


class RegisterAPI(generics.GenericAPIView):  # only superuser(me)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                "user": EmployeeSerializer(user, context=self.get_serializer_context()).data,
                "token": str(token),
            })
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LoginAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    serializer_class = AuthTokenSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get_or_create(user=user)
        if user:
            if user.is_active:
                login(request, user)
                return Response({
                    "user": EmployeeSerializer(user, context=self.get_serializer_context()).data,
                    "token": str(token[0]),
                })
            else:
                raise ValidationError({"400": f'Account not active'})
        else:
            raise ValidationError({"400": f'Account doesnt exist'})


class LogoutAPI(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()

        logout(request)

        return Response('User Logged out successfully')


class GetUser(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request, format=None):

        try:
            token = request.user.auth_token
            serializer = EmployeeSerializer(request.user)
            res = {
                'user': serializer.data,
                'token': str(token)
            }
            return Response(res, status=status.HTTP_200_OK)
        except:
            return Response('No user logged in', status=status.HTTP_400_BAD_REQUEST)


class ChangeEmpPasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = Employee

    def get_object(self, pk, query_set=None):
        try:
            obj = Employee.objects.get(username=pk)
            return obj
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk, *args, **kwargs):
        self.object = self.get_object(pk)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if(EmployeeSerializer(request.user).data.get('shift') == 'zero' and EmployeeSerializer(request.user).data.get('company') == EmployeeSerializer(self.object).data.get('company')):
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                return Response(response)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = Employee

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if EmployeeSerializer(request.user).data.get('shift') == 'zero':
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
