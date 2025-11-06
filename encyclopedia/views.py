from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    Entry = util.get_entry(title)
    if Entry is None:
        return HttpResponse("Requested entry was not found!")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "Entry": Entry
        })
    
def search(request):
    entries = util.list_entries()
    if request.method == "POST":
        encyclopedia_entry = request.POST.get('q')
        if encyclopedia_entry  in entries:
            return redirect('entry', title=encyclopedia_entry)
        else:
            for i in entries[0:]:     
                if encyclopedia_entry in i:
                    return render(request, "encyclopedia/search.html", {
                    "title": encyclopedia_entry,
                    "Entry": i
        })
    return render(request, "encyclopedia/index.html")

def newPage(request):
    entries = util.list_entries()
    if request.method == "POST":
        query = request.POST.get("title")
        content = request.POST.get("content")
        if query in entries:
            return HttpResponse(f"error!!, this title '{query}' already exist")
        else:
            with open(f"entries/{query}.md", 'w') as page:
                page.write(content)
                page.close()
                return redirect('entry', title=query)

    return render(request, "encyclopedia/newpage.html")