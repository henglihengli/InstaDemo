from django.views.generic import TemplateView, ListView
from Insta.models import Post

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'
    
class PostsView(ListView):
    model = Post
    template_name = 'index.html'
