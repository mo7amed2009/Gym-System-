from rest_framework.response import Response
from .models import (Equipment,SecondryMuscle,Split,ProgramDay,
                     ProgramTemlate,ProgramExersice,Exersice)
from .serializer import (EquipmentSerializer,SecondryMuscleSerializer,SpiltSerializer,
                         ProgramDaySerializer,ProgramTemlateSerializer,ProgramExrsiceSerializer,ExersiceSerializer)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import redirect

class SplitListView(generics.ListAPIView):
    """ TO View All Splits And Descrip It """
    
    
    queryset = Split.objects.all()
    
    serializer_class = SpiltSerializer


class CreateProgramExersiceView(generics.CreateAPIView):
    """ To Create Progarm Exersice """
    
    queryset = ProgramExersice.objects.all()
    
    serializer_class = ProgramExrsiceSerializer
    
    
class UpdateProgramExersiceView(APIView):
    """ To Custimize Program Exersice """
    
    def put (self , request , slug ,*warg , **kwars):
        """ This Method To Update It  """
        
        query = ProgramExersice.objects.get(slug=slug)
        
        serializer = ProgramExrsiceSerializer(query, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            # Massege if serializer Valid
            return Response({"Massege":"It Updated Successfuly"}, status=status.HTTP_202_ACCEPTED)
        
        # Massege if Not Valid
        return Response(serializer.errors)
    
    def delete (self , request , slug, *warg , **kwars):
        """ This Method To Delete It  """
        
        
        query = ProgramExersice.objects.get(slug = slug)
        
        query.delete()
        
        return Response({"massege":"It Deleted Successfuly"}, status=status.HTTP_200_OK)
    


class ExersicesListView(generics.ListAPIView):
    """ For View All Exersices in System And Show The Details Of Every One Exersice """
    
    queryset = Exersice.objects.all()
    
    serializer_class = ExersiceSerializer


class EquipmentListView(generics.ListAPIView):
    """ To View All Equipments """
    
    queryset = Equipment.objects.all()
    
    serializer_class = EquipmentSerializer