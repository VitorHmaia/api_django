from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.disciplina import Disciplina
from controle_disc.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaList(generics.ListCreateAPIView):
    """
    Endpoint para listar todas as disciplinas ou criar uma nova disciplina.

    - Método GET: Retorna uma lista de todas as disciplinas.
    - Método POST: Cria uma nova disciplina.
    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def post(self, request, *args, **kwargs):
        """
        Cria uma nova disciplina.

        :param request: Objeto de requisição HTTP.
        :return: Resposta HTTP com a disciplina criada.
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)