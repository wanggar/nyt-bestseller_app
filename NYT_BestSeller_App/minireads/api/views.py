from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
from .models import BulletItem, BulletComment
from .models import BookCollections
from .forms import ShareBookForm, CommentForm, UpdateReadingStatusForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
apiKey = "E3KxNUozu1CAkdITkLh2KPO7otGq3vHu"


def index(request):
    response = requests.get(
        'https://api.nytimes.com/svc/books/v3/lists/2019-01-20/hardcover-fiction.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def culture(request):
    response = requests.get('https://api.nytimes.com/svc/books/v3/lists/current/culture.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def education(request):
    response = requests.get('https://api.nytimes.com/svc/books/v3/lists/current/education.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def family(request):
    response = requests.get('https://api.nytimes.com/svc/books/v3/lists/current/family.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def humor(request):
    response = requests.get('https://api.nytimes.com/svc/books/v3/lists/current/humor.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def non_fiction(request):
    response = requests.get(
        'https://api.nytimes.com/svc/books/v3/lists/current/paperback-nonfiction.json?api-key=' + apiKey)
    book_data = response.json()
    context = {
        'books': book_data['results']['books'],
    }
    return render(request, 'api/index.html', context)


def detail(request, book_title, isbn_13):
    response = requests.get("https://www.goodreads.com/book/isbn/" + isbn_13 + "?key=YBswEKfs0bLMxGEiqMgkdw")
    tree = ET.fromstring(response.content)
    review = tree[1][27]
    if request.method == 'POST':
        form = ShareBookForm(request.POST)
        if form.is_valid():
            new_item = BulletItem(book_title=book_title, poster=request.user, description=form.cleaned_description())
            new_item.save()
        else:
            form = ShareBookForm()
    else:
        form = ShareBookForm()

    context = {
        "book_title": book_title,
        "isbn_13": isbn_13,
        "review": review.text,
        "form": form,
    }
    return render(request, 'api/detail.html', context)


@login_required
def save(request, book_title, isbn_13):
    new_collection = BookCollections(book_title=book_title, isbn=isbn_13, user=request.user)
    new_collection.save()
    return redirect('api:detail', book_title=book_title, isbn_13=isbn_13)


def dashboard(request):
    bullet_items = BulletItem.objects.all()
    context = {
        'bulletItems': bullet_items,
    }
    return render(request, 'api/dashboard.html', context)


def collection(request):
    book_collections = BookCollections.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UpdateReadingStatusForm(request.POST)
        if form.is_valid():
            on_page = form.cleaned_data['onPage']
            total_page = form.cleaned_data['totalPage']
            new_collection = BookCollections.objects.get(id=request.POST.get('collection_id', None))
            new_collection.onPage = on_page
            new_collection.totalPage = total_page
            new_collection.percentage = round(on_page * 100 / total_page)
            new_collection.save()
    else:
        form = UpdateReadingStatusForm()
    context = {
        'book_collections': book_collections,
        'form': form,
    }
    return render(request, 'api/collection.html', context=context)


def comment(request, book_title, bullet_item_id):
    bullet_comments = BulletComment.objects.filter(bullet_item__book_title__exact=book_title)
    context = {
        'bullet_comments': bullet_comments,
        'form': CommentForm(),
        'bullet_item_id': bullet_item_id,
        'book_title': book_title,
    }

    return render(request, 'api/comment.html', context)


def post_comment(request, book_title, bullet_item_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['comment']
            new_bullet_comment = BulletComment(bullet_item_id=bullet_item_id, commenter=request.user, content=content)
            new_bullet_comment.save()
    return redirect('api:comment', book_title=book_title, bullet_item_id=bullet_item_id)


def like(request, bullet_item_id):
    bullet_item = BulletItem.objects.get(id=bullet_item_id)
    bullet_item.likes += 1
    bullet_item.save()
    return redirect('api:dashboard')
# @login_required
# def update_reading_status(request, book_collection_id):
#
#     return HttpResponseRedirect(request.path_info)
