from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseNotFound
from .models import News
from .forms import NewsForm


def news(request):

    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, pk):
    news_detail = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_detail': news_detail})

def new_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/new_news.html', {'form': form})

def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_edit.html', {'form': form})

def news_delete(request, pk):
    
    try:
        news = News.objects.get(id=pk)
        news.delete()
        return redirect('news')
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>Новость не найдена</h2>")