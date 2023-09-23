from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from controle_disc.models.disciplina import Disciplina
from controle_disc.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaDetailView(APIView):
    """
    Endpoint para detalhes, atualização e exclusão de uma disciplina específica.
    """

    # Define o serializador a ser usado para a classe Disciplina
    serializer_class = DisciplinaSerializer

    # Método GET: Retorna detalhes de uma disciplina específica.
    def get(self, request, disciplina_id):
        try:
            # Tenta obter a disciplina pelo ID fornecido
            disciplina = Disciplina.objects.get(id=disciplina_id)
            # Serializa a disciplina para formato JSON
            serializer = self.serializer_class(disciplina)
            # Retorna a resposta com os detalhes da disciplina
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Disciplina.DoesNotExist:
            # Retorna uma resposta de erro se a disciplina não for encontrada
            return Response({"detail": "Disciplina não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    # Método PUT: Atualiza os detalhes de uma disciplina.
    def put(self, request, disciplina_id):
        try:
            # Tenta obter a disciplina pelo ID fornecido
            disciplina = Disciplina.objects.get(id=disciplina_id)
            # Serializa a disciplina com os dados da requisição
            serializer = self.serializer_class(disciplina, data=request.data)
            if serializer.is_valid():
                # Se os dados forem válidos, salva as alterações na disciplina
                serializer.save()
                # Retorna a resposta com os detalhes atualizados da disciplina
                return Response(serializer.data, status=status.HTTP_200_OK)
            # Se os dados não forem válidos, retorna uma resposta de erro
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Disciplina.DoesNotExist:
            # Retorna uma resposta de erro se a disciplina não for encontrada
            return Response({"detail": "Disciplina não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    # Método DELETE: Exclui uma disciplina e desassocia todas as tarefas relacionadas.
    def delete(self, request, disciplina_id):
        try:
            # Tenta obter a disciplina pelo ID fornecido
            disciplina = Disciplina.objects.get(id=disciplina_id)
            # Desassocia todas as tarefas relacionadas à disciplina
            disciplina.tarefa_set.clear()
            # Exclui a disciplina
            disciplina.delete()
            # Retorna uma resposta sem conteúdo para indicar exclusão bem-sucedida
            return Response({"detail": "Disciplina deletada com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Disciplina.DoesNotExist:
            # Retorna uma resposta de erro se a disciplina não for encontrada
            return Response({"detail": "Disciplina não encontrada."}, status=status.HTTP_404_NOT_FOUND)