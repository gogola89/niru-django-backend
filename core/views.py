from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import PageHero
from .serializers import PageHeroSerializer


class PageHeroDetailView(generics.RetrieveAPIView):
    queryset = PageHero.objects.all()
    serializer_class = PageHeroSerializer
    lookup_field = 'page_identifier'
    
    def get_object(self):
        page_identifier = self.kwargs.get('page_identifier')
        return get_object_or_404(PageHero, page_identifier=page_identifier)


@api_view(['GET'])
def page_hero_detail(request, page_identifier):
    """
    Retrieve a specific page hero by page_identifier
    """
    try:
        page_hero = PageHero.objects.get(page_identifier=page_identifier, is_active=True)
        serializer = PageHeroSerializer(page_hero, context={'request': request})
        return Response(serializer.data)
    except PageHero.DoesNotExist:
        return Response(
            {'error': f'Page hero for {page_identifier} not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )