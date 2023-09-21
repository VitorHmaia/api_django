from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from controle_disc.models.aluno import Aluno
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.alunoSerializer import AlunoSerializer
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class AlunoTarefaListView(APIView):
    """
    Endpoint para listar todas as tarefas de um aluno ou criar uma nova tarefa para um aluno.
    """

    # Define o serializador a ser usado para a classe Tarefa
    serializer_class = TarefaSerializer

    # Método GET: Retorna uma lista de todas as tarefas de um aluno.
    def get(self, request, aluno_id):
        try:
            # Obtém o aluno pelo ID fornecido
            aluno = Aluno.objects.get(id=aluno_id)
            # Obtém a lista de tarefas associadas ao aluno
            tarefas = Tarefa.objects.filter(aluno=aluno)
            # Serializa a lista de tarefas
            serializer = TarefaSerializer(tarefas, many=True)
            # Retorna uma resposta com a lista de tarefas do aluno
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não for encontrado
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Método POST: Cria uma nova tarefa associada a um aluno.
    def post(self, request, aluno_id):
        try:
            # Obtém o aluno pelo ID fornecido
            aluno = Aluno.objects.get(id=aluno_id)
            # Obtém um serializador com os dados da requisição
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Salva a nova tarefa associada ao aluno
            serializer.save(aluno=aluno)
            # Retorna uma resposta com os detalhes da tarefa criada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Aluno.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não for encontrado
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)