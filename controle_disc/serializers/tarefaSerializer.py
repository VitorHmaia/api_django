from rest_framework import serializers
from controle_disc.models.tarefa import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'