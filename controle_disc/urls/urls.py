from django.urls import path
from controle_disc.views.aluno.AlunoDetailView import AlunoDetail
from controle_disc.views.aluno.AlunoListCreateView import AlunoListView
from controle_disc.views.disciplina.DisciplinaDetail import DisciplinaDetailView
from controle_disc.views.disciplina.DisciplinaListCreateView import DisciplinaListView
from controle_disc.views.tarefa.TarefaDetailView import TarefaDetailView
from controle_disc.views.tarefa.TarefaListCreateView import TarefaListView
from controle_disc.views.AlunoTarefaListView import AlunoTarefaListView

urlpatterns = [
    # URLs para Aluno
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),

    # URLs para Disciplina
    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina-list'),
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),

    # URLs para Tarefa
    path('tarefas/', TarefaListView.as_view(), name='tarefa-list'),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view(), name='tarefa-detail'),

    # URL para listar tarefas de um aluno específico
    path('alunos/<int:aluno_id>/tarefas/', AlunoTarefaListView.as_view(), name='aluno-tarefas-list'),
]
