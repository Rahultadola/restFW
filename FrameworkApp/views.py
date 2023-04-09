from django.shortcuts import render
from django.http import HttpResponse


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


# Create your views here.

def home(request):
	return HttpResponse('''
		<h1>See, Its working</h1>
		''')



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permissions_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permissions_classes = [permissions.IsAuthenticated]