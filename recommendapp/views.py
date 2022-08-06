# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView

class ReListView(ListView):
    model = User
    template_name = 'recommendapp/list.html'
    paginate_by = 10


class ReDetailView(DetailView):
    model = User
    template_name = 'recommendapp/detail.html'