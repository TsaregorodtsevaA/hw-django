from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

with open(BUS_STATION_CSV, encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    CONTENT = [row for row in reader]
def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': paginator.page(page_num).object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
