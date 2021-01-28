from django.urls import path
from .views import EssayListView,EssayDetailView, EssayCreateView,EssayUpdateView, UserEssayListView
from . import views

urlpatterns = [
    path('',EssayListView.as_view(), name ='EssayApp-Essays'),
    path('user/<str:username>',UserEssayListView.as_view(), name ='user-essays'),
    path('essay/<int:pk>',EssayDetailView.as_view(), name ='essay-detail'),
    path('essay/new/',EssayCreateView.as_view(), name ='essay-create'),
    path('essay/<int:pk>/update',EssayUpdateView.as_view(), name ='essay-update'),
    path('MyEssay/', views.MyEssay, name ='EssayApp-MyEssay'),
    path('pdf_view/<int:pk>', views.ViewPDF, name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]
