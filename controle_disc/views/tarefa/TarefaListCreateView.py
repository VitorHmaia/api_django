from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class TarefaListView(APIView):
    """
    Endpoint para listar todas as tarefas ou criar uma nova tarefa.
    """

    # Define o serializador a ser usado para a classe Tarefa
    serializer_class = TarefaSerializer

    # Método GET: Retorna uma lista de todas as tarefas.
    def get(self, request):
        try:
            # Obtém todos os objetos Tarefa do banco de dados
            tarefas = Tarefa.objects.all()
            # Serializa a lista de tarefas
            serializer = TarefaSerializer(tarefas, many=True)
            # Retorna uma resposta com a lista de tarefas
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Método POST: Cria uma nova tarefa associada a um aluno e uma ou mais disciplinas.
    def post(self, request):
        try:
            # Obtém um serializador com os dados da requisição
            serializer = self.serializer_class(data=request.data)
            # Verifica se os dados são válidos
            serializer.is_valid(raise_exception=True)
            # Salva a nova tarefa no banco de dados
            serializer.save()
            # Retorna uma resposta com os detalhes da tarefa criada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)