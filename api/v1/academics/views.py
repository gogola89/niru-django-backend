from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from apps.academics.models import Programme, ProgrammeHighlight, AdmissionRequirement
from .serializers import (
    ProgrammeSerializer, 
    ProgrammeHighlightSerializer, 
    AdmissionRequirementSerializer
)


class ProgrammeListView(generics.ListAPIView):
    """
    List all academic programmes
    """
    serializer_class = ProgrammeSerializer
    
    def get_queryset(self):
        is_featured = self.request.query_params.get('featured', None)
        if is_featured and is_featured.lower() in ['true', '1']:
            return Programme.objects.filter(is_featured=True)
        return Programme.objects.all()


class ProgrammeDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific programme with its highlights and admission requirements
    """
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.prefetch_related('highlights', 'admission_reqs')
    lookup_field = 'slug'


class ProgrammeHighlightListView(generics.ListAPIView):
    """
    List all programme highlights
    """
    serializer_class = ProgrammeHighlightSerializer
    queryset = ProgrammeHighlight.objects.all().select_related('programme')


class AdmissionRequirementListView(generics.ListAPIView):
    """
    List all admission requirements
    """
    serializer_class = AdmissionRequirementSerializer
    queryset = AdmissionRequirement.objects.all().select_related('programme')


@api_view(['GET'])
def programme_details_with_requirements(request, slug):
    """
    Get programme details with its highlights and admission requirements
    """
    programme = get_object_or_404(Programme, slug=slug)

    # Get related data
    highlights = ProgrammeHighlight.objects.filter(programme=programme)
    admission_reqs = AdmissionRequirement.objects.filter(programme=programme)

    # Serialize the data
    programme_serializer = ProgrammeSerializer(programme, context={'request': request})
    highlights_serializer = ProgrammeHighlightSerializer(highlights, many=True, context={'request': request})
    admission_reqs_serializer = AdmissionRequirementSerializer(admission_reqs, many=True, context={'request': request})

    response_data = {
        'programme': programme_serializer.data,
        'highlights': highlights_serializer.data,
        'admission_requirements': admission_reqs_serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def featured_programmes(request):
    """
    Get all featured programmes
    """
    programmes = Programme.objects.filter(is_featured=True).prefetch_related('highlights', 'admission_reqs')
    serializer = ProgrammeSerializer(programmes, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)