from rest_framework.views import APIView
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    get=extend_schema(summary="Получить список задач",
                      tags=["Задачи"]),
    post=extend_schema(summary="Создание задачи",
                       tags=["Задачи"]),
)
class TaskAPIView(APIView):
    """ Представление задач """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Результат": f"Задача '{serializer.data['title']}' добавлена"})
        return Response(serializer.errors, status=400)

    def get(self, request):
        return Response(self.queryset.values())
