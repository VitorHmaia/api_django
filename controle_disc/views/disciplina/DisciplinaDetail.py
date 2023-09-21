from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.disciplina import Disciplina
from controle_disc.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para detalhes, atualização e exclusão de uma disciplina específica.

    - Método GET: Retorna detalhes de uma disciplina específica.
    - Método PUT: Atualiza os detalhes de uma disciplina.
    - Método DELETE: Exclui uma disciplina e desassocia todas as tarefas relacionadas.
    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Exclui uma disciplina e desassocia todas as tarefas relacionadas.

        :param request: Objeto de requisição HTTP.
        :param args: Argumentos da view.
        :param kwargs: Argumentos de palavras-chave da view.
        :return: Resposta HTTP sem conteúdo.
        """
        try:
            instance = self.get_object()
            # Além de excluir a disciplina, desassocie todas as tarefas relacionadas.
            instance.tarefa_set.clear()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)