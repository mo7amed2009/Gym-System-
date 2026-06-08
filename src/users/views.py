from django.shortcuts import render
from rest_framework import generics
from .models import User , UserInfo , UserProfile
from .serializer import UserSerializer , UserProfileSerializer , UserInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    
    serializer_class = UserSerializer
    
    
    
class UserProfileView(APIView):
    
    def put(self , request , username , *wargs , **kwargs):
        
        try:
        
            query = UserProfile.objects.get(user__username__exact=username)
        
        except:
            return Response({"Massege":"Not Found"} ,status=status.HTTP_404_NOT_FOUND)    
            
        
        serializer = UserProfileSerializer(query,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"Massege":"The Profile Of You Updated Successfuly"},
                            status=status.HTTP_202_ACCEPTED)
            
        return Response(serializer.errors)    
    
    
    
class UserInfoView(APIView):
    
    def put(self , request , username , *wargs , **kwargs):
        
        try:
        
            query = UserInfo.objects.get(profile__user__username__exact=username)
        
        except:
            return Response({"Massege":"Not Found"} ,status=status.HTTP_404_NOT_FOUND)    
            
        serializer = UserInfoSerializer(query,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"Massege":"The Profile Info Of You Updated Successfuly"},
                            status=status.HTTP_202_ACCEPTED)
            
        return Response(serializer.errors)    
        
