from django.views.generic import ListView, TemplateView
from .models import ItemModel
from django.shortcuts import redirect, render
import redis
from scrapy_with_django.settings import REDIS_HOST, REDIS_PORT

redis_server = redis.Redis(REDIS_HOST, REDIS_PORT)


class ItemsView(ListView):
    model = ItemModel
    template_name = 'breuninger_shop/index.html'


class StartSpiderView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'breuninger_shop/start.html', {})

    def post(self, request):
        if request.method == 'POST':
            redis_server.lpush('breuninger:start_urls', 'https://www.breuninger.com/damen/schuhe')
            return redirect('itemlist')
