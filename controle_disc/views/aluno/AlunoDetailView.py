from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.aluno import Aluno
from controle_disc.serializers.alunoSerializer import AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para detalhes, atualização e exclusão de um aluno específico.

    - Método GET: Retorna detalhes de um aluno específico.
    - Método PUT: Atualiza os detalhes de um aluno.
    - Método DELETE: Exclui um aluno e todas as tarefas associadas.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Exclui um aluno e desassocia todas as tarefas relacionadas.

        :param request: Objeto de requisição HTTP.
        :param args: Argumentos da view.
        :param kwargs: Argumentos de palavras-chave da view.
        :return: Resposta HTTP sem conteúdo.
        """
        try:
            instance = self.get_object()
            # Excluir o aluno.
            instance.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)