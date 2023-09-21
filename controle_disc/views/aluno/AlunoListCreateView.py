from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from controle_disc.models.aluno import Aluno
from controle_disc.serializers.alunoSerializer import AlunoSerializer

class AlunoListView(APIView):
    """
    Endpoint para listar todos os alunos ou criar um novo aluno.
    """
    
    def get(self, request):
        """
        Método GET: Retorna uma lista de todos os alunos.
        """
        try:
            # Obtém todos os objetos Aluno do banco de dados
            alunos = Aluno.objects.all()
            # Serializa a lista de alunos
            serializer = AlunoSerializer(alunos, many=True)
            # Retorna uma resposta com a lista de alunos
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Método POST: Cria um novo aluno.

        :param request: Objeto de requisição HTTP contendo os dados do novo aluno.
        :return: Resposta HTTP com o aluno criado.
        """
        try:
            # Obtém um serializador com os dados da requisição
            serializer = AlunoSerializer(data=request.data)
            # Verifica se os dados são válidos
            serializer.is_valid(raise_exception=True)
            # Salva o novo aluno no banco de dados
            serializer.save()
            # Retorna uma resposta com os detalhes do aluno criado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Em caso de erro, retorna uma resposta de erro com detalhes
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)