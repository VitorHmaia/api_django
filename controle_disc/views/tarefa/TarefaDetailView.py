from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from controle_disc.models.tarefa import Tarefa
from controle_disc.serializers.tarefaSerializer import TarefaSerializer

class TarefaDetailView(APIView):
    """
    Endpoint para detalhes, atualização e exclusão de uma tarefa específica.
    """

    # Define o serializador a ser usado para a classe Tarefa
    serializer_class = TarefaSerializer

    # Método GET: Retorna detalhes de uma tarefa específica.
    def get(self, request, tarefa_id):
        try:
            # Tenta obter a tarefa pelo ID fornecido
            tarefa = Tarefa.objects.get(pk=tarefa_id)
            # Serializa a tarefa para formato JSON
            serializer = self.serializer_class(tarefa)
            # Retorna a resposta com os detalhes da tarefa
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tarefa.DoesNotExist:
            # Retorna uma resposta de erro se a tarefa não for encontrada
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    # Método PUT: Atualiza os detalhes de uma tarefa.
    def put(self, request, tarefa_id):
        try:
            # Tenta obter a tarefa pelo ID fornecido
            tarefa = Tarefa.objects.get(pk=tarefa_id)
            # Serializa a tarefa com os dados da requisição
            serializer = self.serializer_class(tarefa, data=request.data)
            if serializer.is_valid():
                # Se os dados forem válidos, salva as alterações na tarefa
                serializer.save()
                # Retorna a resposta com os detalhes atualizados da tarefa
                return Response(serializer.data, status=status.HTTP_200_OK)
            # Se os dados não forem válidos, retorna uma resposta de erro
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tarefa.DoesNotExist:
            # Retorna uma resposta de erro se a tarefa não for encontrada
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    # Método DELETE: Exclui uma tarefa específica.
    def delete(self, request, tarefa_id):
        try:
            # Tenta obter a tarefa pelo ID fornecido
            tarefa = Tarefa.objects.get(pk=tarefa_id)
            # Exclui a tarefa
            tarefa.delete()
            # Retorna uma resposta sem conteúdo para indicar exclusão bem-sucedida
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tarefa.DoesNotExist:
            # Retorna uma resposta de erro se a tarefa não for encontrada
            return Response({"detail": "Tarefa não encontrada."}, status=status.HTTP_404_NOT_FOUND)