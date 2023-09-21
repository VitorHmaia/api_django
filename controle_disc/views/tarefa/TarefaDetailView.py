from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint para detalhes, atualização e exclusão de uma tarefa específica.

    - Método GET: Retorna detalhes de uma tarefa específica.
    - Método PUT: Atualiza os detalhes de uma tarefa.
    - Método DELETE: Exclui uma tarefa específica.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Exclui uma tarefa específica.

        :param request: Objeto de requisição HTTP.
        :param args: Argumentos da view.
        :param kwargs: Argumentos de palavras-chave da view.
        :return: Resposta HTTP sem conteúdo.
        """
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)