from django.shortcuts import render, get_object_or_404
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from .models import Essay
from xhtml2pdf import pisa

# Create your views here.

def Essays(request):
    context = {
        'Essays': Essay.objects.all()
    }
    return render (request,'EssayApp/Essays.html', context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

#Opens up page as PDF
def ViewPDF(request,pk):
         essays =  Essay.objects.get(id = pk)
         essayauthor = essays.author
         essaytitle = essays.title
         essaycontent = essays.content
         data = {
             "EssayAuthor":essayauthor,
             "Essaytitle": essaytitle,
             "Essaycontent":essaycontent
            }
         pdf = render_to_pdf('EssayApp/pdf_template.html', data)
         return HttpResponse(pdf, content_type='application/pdf')

class EssayListView(ListView):
    model = Essay
    template_name='EssayApp/Essays.html'
    context_object_name = 'Essays'

class UserEssayListView(ListView):
    model = Essay
    template_name='EssayApp/user_essays.html'
    context_object_name = 'Essays'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Essay.objects.filter(author=user)

class EssayDetailView(DetailView):
    model = Essay

class EssayCreateView(LoginRequiredMixin, CreateView):
    model = Essay
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EssayUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Essay
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        essay = self.get_object()
        if self.request.user == essay.author:
            return True
        return False

def MyEssay(request):
    return render (request, 'EssayApp/MyEssay.html',{'title':'My Essays'})

