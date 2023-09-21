from django.urls import path
from controle_disc.views.aluno.AlunoDetailView import AlunoDetail
from controle_disc.views.aluno.AlunoListCreateView import AlunoList
from controle_disc.views.disciplina.DisciplinaDetail import DisciplinaDetail
from controle_disc.views.disciplina.DisciplinaListCreateView import DisciplinaList
from controle_disc.views.tarefa.TarefaDetailView import TarefaDetail
from controle_disc.views.tarefa.TarefaListCreateView import TarefaList
from controle_disc.views.AlunoTarefaListView import AlunoTarefaList

urlpatterns = [
    # URLs para Aluno
    path('alunos/', AlunoList.as_view(), name='aluno-list'),
    path('alunos/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),

    # URLs para Disciplina
    path('disciplinas/', DisciplinaList.as_view(), name='disciplina-list'),
    path('disciplinas/<int:pk>/', DisciplinaDetail.as_view(), name='disciplina-detail'),

    # URLs para Tarefa
    path('tarefas/', TarefaList.as_view(), name='tarefa-list'),
    path('tarefas/<int:pk>/', TarefaDetail.as_view(), name='tarefa-detail'),

    # URL para listar tarefas de um aluno específico
    path('alunos/<int:aluno_id>/tarefas/', AlunoTarefaList.as_view(), name='aluno-tarefas-list'),
]
