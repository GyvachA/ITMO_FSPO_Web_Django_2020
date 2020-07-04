from django.shortcuts import render
from django.http import Http404
from platonov_app.models import Owner


def detail(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exists")
    return render(request, 'owner.html', {'owner': owner})
