from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets

from simple_api.models import Students, Snippets
from simple_api.serializers import StudentSerializer, SnippetSerializer

# Create your views here.
class StudentViews(APIView):
    """students data show and add"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *arg, **kwargs):
        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({"status": "success", "student": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class StudentIDViews(APIView):
    """Student data update, view, delete"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """view student data"""

        try:
            result = Students.objects.get(id=id)
        except Students.DoesNotExist:
            result = False
        if result:
            serializer = StudentSerializer(result)
            return Response({"status": "success", "data": serializer.data}, status=200)
        else:
            return Response(
                {"status": "error", "data": "record is not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request, id):
        """update student data"""

        result = Students.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        """delete student data"""

        result = get_list_or_404(Students, id=id)
        result[0].delete()
        return Response({"status": "success", "data": "record deleted"})


class SnippetsViews(APIView):
    """Snippet data show and add"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *arg, **kwargs):
        result = Snippets.objects.all()
        serializers = SnippetSerializer(result, many=True)
        return Response({"status": "success", "student": serializers.data}, status=200)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class SnippetDetails(APIView):
    """view Snippets data"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """view Snippet data"""

        try:
            result = Snippets.objects.get(id=id)
        except Exception as e:
            return Response(
                {"status": "error", "data": "record is not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if result:
            serializer = SnippetSerializer(result)
            return Response({"status": "success", "data": serializer.data}, status=200)

    def patch(self, request, id):
        """update snippet data"""
        result = Snippets.objects.get(id=id)
        serializer = SnippetSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        """delete snippet data"""

        result = get_list_or_404(Snippets, id=id)
        result[0].delete()
        return Response({"status": "success", "data": "record deleted"})


class StudentModelBaseView(viewsets.ModelViewSet):
    pass
    