from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Article

def news_home(request):
    # Новые статьи сначала, старые после (для автоматического создания новых страниц)
    all_news = Article.objects.all().order_by("-date")
    # Лимит 3 статьи на одну страницу
    paginator = Paginator(all_news, 3)
    page_num = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_num)
    return render(request, "news/news_home.html", {"page_obj": page_obj})

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        anons = request.POST.get("anons")
        full_text = request.POST.get("text")
        date = request.POST.get("date")

        Article.objects.create(
            title=title,
            anons=anons,
            full_text=full_text,
            date=date
        )
        return redirect("news")
    return render(request, "news/create.html")