from django.views.generic.list import ListView

from app.models import Messages


class MessagesListView(ListView):
    model = Messages

    def get_queryset(self):
        return Messages.objects.all()
