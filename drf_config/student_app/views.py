from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import student_serializer
from .student_serializer import StudentSerializer
from .models import Student
@api_view(['POST','GET','PUT','DELETE'])
def student_view(request):
    if request.method == 'POST':
        data=request.data
        student_serializer=StudentSerializer(data=data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)

@api_view(["PUT"])
def update_student(request, id):

    student_obj = Student.objects.get(id=id)

    student_serializer = StudentSerializer(
        student_obj,
        data=request.data
    )

    if student_serializer.is_valid():
        student_serializer.save()

        return Response({
            "message": "Student updated successfully",
            "data": student_serializer.data
        })

    return Response(student_serializer.errors)


