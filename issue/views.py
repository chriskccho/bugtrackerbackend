from django.shortcuts import render
from .serializers import IssueSerializer, ProjectSerializer, SignupSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, mixins
from .models import User, Project, Issue

# Create your views here.

@api_view(['POST'])
def signup_view(request):

    if request.method =='POST':
        serializer = SignupSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
            data['user_id'] = user.id
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

class UserListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self,request):
        return self.list(request)

class ProjectAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self,request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class IssueAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def get(self,request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self, request, pk):
        return self.update(request,id)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request,*args,**kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token':token.key, 'username': token.user.username, 'user_id':token.user.id})

