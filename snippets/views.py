from rest_framework import viewsets
from rest_framework import permissions
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
