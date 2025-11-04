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
                    return HttpResponse(f"{encyclopedia_entry} was not found, did you mean {i}?")
    return render(request, "encyclopedia/index.html")