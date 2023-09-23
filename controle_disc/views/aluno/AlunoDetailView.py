from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle_disc.models.aluno import Aluno
from controle_disc.serializers.alunoSerializer import AlunoSerializer

class AlunoDetail(APIView):
    """
    Endpoint para detalhes, atualização e exclusão de um aluno específico.

    - Método GET: Retorna detalhes de um aluno específico.
    - Método PUT: Atualiza os detalhes de um aluno.
    - Método DELETE: Exclui um aluno e todas as tarefas associadas.
    """
    # Define o serializador a ser usado para a classe Aluno
    serializer_class = AlunoSerializer
    # GET: Retorna detalhes de um aluno específico
    def get(self, request, aluno_id):
        try:
            # Tenta obter o aluno pelo ID fornecido
            aluno = Aluno.objects.get(id=aluno_id)
            # Serializa o aluno para formato JSON
            serializer = self.serializer_class(aluno)
            # Retorna a resposta com os detalhes do aluno
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não for encontrado
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # PUT: Atualiza os detalhes de um aluno
    def put(self, request, aluno_id):
        try:
            # Tenta obter o aluno pelo ID fornecido
            aluno = Aluno.objects.get(id=aluno_id)
            # Serializa o aluno com os dados da requisição
            serializer = self.serializer_class(aluno, data=request.data)
            if serializer.is_valid():
                # Se os dados forem válidos, salva as alterações no aluno
                serializer.save()
                # Retorna a resposta com os detalhes atualizados do aluno
                return Response(serializer.data, status=status.HTTP_200_OK)
            # Se os dados não forem válidos, retorna uma resposta de erro
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Aluno.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não for encontrado
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    # DELETE: Exclui um aluno e todas as tarefas associadas
    def delete(self, request, aluno_id):
        try:
            # Tenta obter o aluno pelo ID fornecido
            aluno = Aluno.objects.get(id=aluno_id)
            # Exclui o aluno
            aluno.delete()
            # Retorna uma resposta sem conteúdo para indicar exclusão bem-sucedida
            return Response({"detail": "Aluno deletado com sucesso."}, status=status.HTTP_204_NO_CONTENT)
        except Aluno.DoesNotExist:
            # Retorna uma resposta de erro se o aluno não for encontrado
            return Response({"detail": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)