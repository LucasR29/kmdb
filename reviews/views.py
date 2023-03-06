from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .serializers import ReviewSerializer
from rest_framework import generics
from movies.models import Movie
from permissions.permissions import IsCriticOrAdm
from .models import Review


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsCriticOrAdm]

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer.save(critic=self.request.user, movie=movie, **self.request.data)
