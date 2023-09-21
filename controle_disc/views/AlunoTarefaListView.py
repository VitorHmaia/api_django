from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.aluno import Aluno
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.alunoSerializer import AlunoSerializer
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class AlunoTarefaList(generics.ListCreateAPIView):
    """
    Endpoint para listar todas as tarefas de um aluno ou criar uma nova tarefa para um aluno.

    - Método GET: Retorna uma lista de todas as tarefas de um aluno.
    - Método POST: Cria uma nova tarefa associada a um aluno.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def get_queryset(self):
        """
        Retorna a lista de tarefas de um aluno específico.

        :return: Queryset de tarefas do aluno.
        """
        aluno_id = self.kwargs.get('aluno_id')
        return Tarefa.objects.filter(aluno__id=aluno_id)

    def post(self, request, *args, **kwargs):
        """
        Cria uma nova tarefa associada a um aluno.

        :param request: Objeto de requisição HTTP.
        :param aluno_id: ID do aluno para o qual a tarefa será criada.
        :return: Resposta HTTP com a tarefa criada.
        """
        try:
            aluno_id = self.kwargs.get('aluno_id')
            aluno = Aluno.objects.get(id=aluno_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(aluno=aluno)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Aluno.DoesNotExist:
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
