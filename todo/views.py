from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # ✅ Allow all users
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):  # ✅ Enables full CRUD (GET, POST, PUT, DELETE)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]  # ✅ Ensures no authentication blocks requests
