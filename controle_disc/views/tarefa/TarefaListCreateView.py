from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class TarefaList(generics.ListCreateAPIView):
    """
    Endpoint para listar todas as tarefas ou criar uma nova tarefa.

    - Método GET: Retorna uma lista de todas as tarefas.
    - Método POST: Cria uma nova tarefa associada a um aluno e uma ou mais disciplinas.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def post(self, request, *args, **kwargs):
        """
        Cria uma nova tarefa associada a um aluno e uma ou mais disciplinas.

        :param request: Objeto de requisição HTTP.
        :return: Resposta HTTP com a tarefa criada.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)