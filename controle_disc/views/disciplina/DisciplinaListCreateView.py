from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from controle_disc.models.disciplina import Disciplina
from controle_disc.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaListView(APIView):
    """
    Endpoint para listar todas as disciplinas ou criar uma nova disciplina.
    """
    
    # Define o serializador a ser usado para a classe Disciplina
    serializer_class = DisciplinaSerializer

    # Método GET: Retorna uma lista de todas as disciplinas.
    def get(self, request):
        try:
            # Obtém todos os objetos Disciplina do banco de dados
            disciplinas = Disciplina.objects.all()
            # Serializa a lista de disciplinas
            serializer = DisciplinaSerializer(disciplinas, many=True)
            # Retorna uma resposta com a lista de disciplinas
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Método POST: Cria uma nova disciplina.
    def post(self, request):
        try:
            # Obtém um serializador com os dados da requisição
            serializer = self.serializer_class(data=request.data)
            # Verifica se os dados são válidos
            serializer.is_valid(raise_exception=True)
            # Salva a nova disciplina no banco de dados
            serializer.save()
            # Retorna uma resposta com os detalhes da disciplina criada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)