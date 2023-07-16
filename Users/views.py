from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

from . serializers import UserSerializer, ChangePasswordSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from . models import User


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Not Found.'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'Message: Logged out Successful'}, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def change_password(request):
#     serializer = ChangePasswordSerializer(data = request.data)
#     if serializer.is_valid():
#         user = User.objects.get(username= request.data['username'])
#         if not user.check_password(serializer.data.get("old_password")):
#             return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

#         user.set_password(serializer.data.get("new_password"))
#         user.save()

#         return Response(status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        user = request.user

        # Check old password
        if not user.check_password(serializer.data.get("old_password")):
            print(user.old_password)
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # set_password also hashes the password that the user will get
        user.set_password(serializer.data.get("new_password"))
        user.save()

        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def change_password(request):
#     queryset = User.objects.all()
#     serializer_class = ChangePasswordSerializer

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def change_password(self, request):
#    serializer = self.get_serializer(data = request.data)
#    serializer.is_valid(raise_exception=True)
#    request.user.set_password(serializer.validated_data['new_password'])
#    request.user.save()

#    return Response(status=status.HTTP_204_NO_CONTENT)

# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def reset_password(request):
#     serializer = 

