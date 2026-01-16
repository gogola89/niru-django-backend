from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from apps.about.models import AboutPage, CoreValue, ViceChancellorMessage as VCMessage
from .serializers import (
    AboutPageSerializer,
    CoreValueSerializer,
    ViceChancellorMessageSerializer
)


class AboutPageDetailView(generics.RetrieveAPIView):
    """
    Retrieve the about page content
    """
    serializer_class = AboutPageSerializer
    queryset = AboutPage.objects.all()

    def get_object(self):
        # There should only be one AboutPage instance
        about_page, created = AboutPage.objects.get_or_create(
            id=1,  # Use a fixed ID to ensure singleton
            defaults={
                'mission': 'Default mission statement',
                'vision': 'Default vision statement',
                'history': 'Default history content'
            }
        )
        return about_page


class CoreValueListView(generics.ListAPIView):
    """
    List all core values
    """
    serializer_class = CoreValueSerializer
    queryset = CoreValue.objects.all()


class ViceChancellorMessageDetailView(generics.RetrieveAPIView):
    """
    Retrieve the vice chancellor message
    """
    serializer_class = ViceChancellorMessageSerializer
    queryset = VCMessage.objects.all()

    def get_object(self):
        # There should typically be one VC message
        return VCMessage.objects.first()


@api_view(['GET'])
def about_page_with_relations(request):
    """
    Get about page content with related core values and VC message
    """
    # Get the about page (create if doesn't exist)
    about_page, created = AboutPage.objects.get_or_create(
        id=1,
        defaults={
            'mission': 'Default mission statement',
            'vision': 'Default vision statement',
            'history': 'Default history content'
        }
    )

    # Get related data
    core_values = CoreValue.objects.all()
    vc_message = VCMessage.objects.first()

    # Serialize the data
    about_serializer = AboutPageSerializer(about_page, context={'request': request})
    core_values_serializer = CoreValueSerializer(core_values, many=True, context={'request': request})
    vc_message_serializer = ViceChancellorMessageSerializer(vc_message, context={'request': request}) if vc_message else None

    response_data = {
        'about_page': about_serializer.data,
        'core_values': core_values_serializer.data,
        'vc_message': vc_message_serializer.data if vc_message_serializer else None
    }

    return Response(response_data, status=status.HTTP_200_OK)