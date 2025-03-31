import random
import markdown2
from django.shortcuts import render, redirect
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound("Page not found")

    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    query = request.GET.get('q', '')
    if not query:
        return redirect('index')

    entries = util.list_entries()
    if query in entries:
        return redirect('entry', title=query)

    matches = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches": matches
    })


def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")

        if not title or not content:
            return render(request, "encyclopedia/new.html", {
                "error": "Title and content are required."
            })

        if title in util.list_entries():
            return render(request, "encyclopedia/new.html", {
                "error": "Encyclopedia entry already exists."
            })

        util.save_entry(title, content)
        return redirect('entry', title=title)

    return render(request, "encyclopedia/new.html")


def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get("content", "")
        if content:
            util.save_entry(title, content)
            return redirect('entry', title=title)

    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound("Page not found")

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random_page(request):
    entries = util.list_entries()
    if not entries:
        return redirect('index')
    random_entry = random.choice(entries)
    return redirect('entry', title=random_entry)