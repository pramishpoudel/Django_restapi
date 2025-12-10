from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#concept of serialization
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from blog.models import Blog,Comment
from blog.serializers import  CommentSerializer,BlogSerializer
@api_view(['GET','POST'])
def student_view(request):
    if request.method == 'GET':
          #get all students data
          students = Student.objects.all()
          serializer = StudentSerializer(students, many=True)#sinece many students data are serialized so many=True
          return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
            #create a new student
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
    
@api_view(['GET','PUT','DELETE'])
def studentdetailview(request,pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

#class based views

class Employees(APIView):

    def get(self,request):
          employeeing = Employee.objects.all()
          serializer = EmployeeSerializer(employeeing, many=True)
          return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):

#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
    #         # return Response(status=status.HTTP_404_NOT_FOUND)
    #         raise Http404
    
    # def get(self,request,pk):
    #      employee = self.get_object(pk)
    #      serializer = EmployeeSerializer(employee)
    #      return Response (serializer.data,status=status.HTTP_200_OK)
    
    # def put(self,request,pk):
    #     employee = self.get_object(pk)
    #     serializer = EmployeeSerializer(employee,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_200_OK)
   
    # def delete(self,request,pk):
    #      employees = self.get_object(pk)
    #      employees.delete()
    #      return  Response(status=status.HTTP_200_OK)





#Mixins

"""

# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request):
#           return self.list(request)
    
#     def post(self,request):
#          return self.create(request)
    
# #primary key operation
# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView,mixins.DestroyModelMixin):
#     queryset=Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request,pk):
#          return self.retrieve(request,pk)
    
#     def put(self,request,pk):
#          return self.update(request,pk)
    
#     def delete(self,request,pk):
#          return self.destroy(request,pk)
"""

#implementaion of Generics
"""
class Employees(generics.ListCreateAPIView):
    #you(generics.ListAPIView,generics.CreateAPIView)==(generics.ListCreateAPIView)
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    # (generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView)==(generics.RetrieveUpdateDestoryAPIView)
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
     
"""

#viewsets concept
"""class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer =EmployeeSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
         employee=get_object_or_404(Employee,pk=pk)
         serializer=EmployeeSerializer(employee)
         return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self,request,pk=None):
         employee=get_object_or_404(Employee,pk=pk)
         serializer=EmployeeSerializer(employee)
         if serializer.is_valid():
              return Response(serializer.data)
         return Response(serializer.errors)
    
    def delete(self,request,pk=None):
         employee = get_object_or_404(Employee,pk=pk)
         employee.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)"""
     


#Modelviewsets
class EmployeeViewset(viewsets.ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer 
        "this specific code handle everything crud and primary and non-primary key opertion"




class BlogView(generics.ListCreateAPIView):
     queryset= Blog.objects.all()
     serializer_class = BlogSerializer


class CommentView(generics.ListCreateAPIView):
     queryset= Comment.objects.all()
     serializer_class = CommentSerializer


class CommentDetailView(generics.ListCreateAPIView):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializer
     lookup_field = 'pk'

class BlogDetailView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'