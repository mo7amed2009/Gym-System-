from rest_framework.response import Response
from .models import  *
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import redirect
from rest_framework.permissions import BasePermission ,IsAdminUser, IsAuthenticated
from users.views import IsCoach

    


class CreateListSplitVIew(APIView):
    
    # permission_classes = [IsAdminUser | IsCoach]
    
    def get (self , request , *wargs , **kwargs):
        
        splits = Split.objects.all()
        serialize = SpiltSerializer(splits,many=True)
       
        return Response(serialize.data,status=status.HTTP_200_OK)
    
    def post(self , request , *wargs , **kwargs):
        
        serialize = SpiltSerializer(data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            
            return Response({"Massege":"The Split Created Successfuly"},status.HTTP_201_CREATED)
        
        return Response({"massege":"Error This Is Not Valid"},status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
class UpdateDeleteSplitView(APIView):
    
    # permission_classes = [IsAdminUser]
    
    def put (self , request , split ,*wargs , **kwargs):
        try:
            
            split = Split.objects.get(split_type__icontains=split)
            
        except:
            return Response({"massege":"The Split Not Found"})
        serializer = SpiltSerializer(split , data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response({"Massege":"The Split Updated Successfuly"},status.HTTP_202_ACCEPTED)
            
        return Response({"massege":"Error This Is Not Valid"},status=status.HTTP_400_BAD_REQUEST)
      
    def delete (self , request , split ,*wargs , **kwargs):       
        try:
            
            split = Split.objects.get(split_type__icontains=split)
            
        except:
            return Response({"massege":"The Split Not Found"})
        
        split.delete()
        
        return Response({"massege":"The Split Deleted Successfuly"},status=status.HTTP_200_OK)
        
        
class SecondryMuscleListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser , IsCoach]  
    
    queryset = SecondryMuscle.objects.all()
    
    serializer_class = SecondryMuscleSerializer 

class SecondryMusclePutDelete(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAdminUser]
    
    queryset = SecondryMuscle.objects.all()
    
    serializer_class = SecondryMuscleSerializer
    
    lookup_field = 'name'
    


        
class ExersiceListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser , IsCoach]  
    
    queryset = Exersice.objects.all()
    
    serializer_class = ExersiceSerializer 
    
class ExersicePutDelete(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAdminUser]
    
    queryset = Exersice.objects.all()
    
    serializer_class = ExersiceSerializer
    
    lookup_field = 'name'
    
    

    
class ProgramTempleteListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser , IsCoach]  
    
    queryset = ProgramTemlate.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProgramTemlateSerializerCreate
        
        return ProgramTemlateSerializer
    
class ProgramTempletePutDelete(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAdminUser]
    
    queryset = ProgramTemlate.objects.all()
    
    serializer_class = ProgramTemlateSerializerCreate
    
    lookup_field = 'name'
    
    
    
    
class ProgramDayteListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser , IsCoach]  
    
    queryset = ProgramDay.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProgramDaySerializerCreate
        
        return ProgramDaySerializer
    
class ProgramDayPutDelete(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAdminUser]
    
    queryset = ProgramDay.objects.all()
    
    serializer_class = ProgramDaySerializerCreate
    
    lookup_field = 'name'



    
class ProgramExersiceteListCreateView(generics.ListCreateAPIView):
    
    # permission_classes = [IsAdminUser , IsCoach]  
    
    queryset = ProgramExersice.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProgramExrsiceSerializerCreate
        
        return ProgramExrsiceSerializer    
class ProgramExersicePutDelete(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = [IsAdminUser]
    
    queryset = ProgramExersice.objects.all()
    
    serializer_class = ProgramExrsiceSerializerCreate
    
    lookup_field = 'slug'
    

    