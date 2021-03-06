from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CursoAPIView, CursosAPIView,AvaliacoesAPIView, AvaliacaoAPIView, CursoViewSet, AvaliacaoViewSet

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='curso'),
    path('cursos/<pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<curso_pk>/avaliacoes/<avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]