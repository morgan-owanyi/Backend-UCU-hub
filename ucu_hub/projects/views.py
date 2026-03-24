from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.filter(status='approved')
    serializer_class = ProjectSerializer
