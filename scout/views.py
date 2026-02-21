from rest_framework.viewsets import ModelViewSet
from .models import Teacher, Student, Event
from .serializers import TeacherSerializer, StudentSerializer, EventSerializer   
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework import status



# these are signup api for teacher and student

class TeacherSignupView(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentSignupView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# these are login api for teacher and student
class TeacherLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            teacher = Teacher.objects.get(email=email)
            if check_password(password, teacher.password):
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid password'}, status=400)
        except Teacher.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=400)


class StudentLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            student = Student.objects.get(email=email)
            if check_password(password, student.password):
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            else:
                return Response({'error': 'Invalid password'}, status=400)
        except Student.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=400)


# these are curd operation for teacher, student and event model
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer