from django.shortcuts import render
from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers

# Create your views here.
class TaskListView(View):
    @method_decorator(cache_control(max_age=300))
    @method_decorator(vary_on_headers("HX-Request"))
    def get(self, request):
        context = {}
        if request.htmx:
            template_name = 'tasks/task-list.html'
        else:
            template_name = 'tasks/task-list.html'
        return render(request, template_name, context)