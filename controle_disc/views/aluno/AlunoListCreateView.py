from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.aluno import Aluno
from controle_disc.serializers.alunoSerializer import AlunoSerializer

class AlunoList(generics.ListCreateAPIView):
    """
    Endpoint para listar todos os alunos ou criar um novo aluno.

    - Método GET: Retorna uma lista de todos os alunos.
    - Método POST: Cria um novo aluno.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def post(self, request, *args, **kwargs):
        """
        Cria um novo aluno.

        :param request: Objeto de requisição HTTP.
        :return: Resposta HTTP com o aluno criado.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)