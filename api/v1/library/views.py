from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from apps.library.models import LibraryPage, LibrarianMessage, EResource, LibraryPolicy
from .serializers import (
    LibraryPageSerializer,
    LibrarianMessageSerializer,
    EResourceSerializer,
    LibraryPolicySerializer
)


class LibraryPageDetailView(generics.RetrieveAPIView):
    """
    Retrieve the library page content
    """
    serializer_class = LibraryPageSerializer
    queryset = LibraryPage.objects.all()

    def get_object(self):
        # There should typically be one library page
        library_page, created = LibraryPage.objects.get_or_create(
            id=1,
            defaults={
                'mission': 'Default library mission',
                'vision': 'Default library vision',
                'objectives': 'Default library objectives',
                'quality_statement': 'Default quality statement',
                'value_1_title': 'Default Value 1',
                'value_1_description': 'Default value 1 description',
                'value_2_title': 'Default Value 2',
                'value_2_description': 'Default value 2 description',
                'value_3_title': 'Default Value 3',
                'value_3_description': 'Default value 3 description',
                'value_4_title': 'Default Value 4',
                'value_4_description': 'Default value 4 description',
            }
        )
        return library_page


class LibrarianMessageDetailView(generics.RetrieveAPIView):
    """
    Retrieve the librarian message
    """
    serializer_class = LibrarianMessageSerializer
    queryset = LibrarianMessage.objects.all()

    def get_object(self):
        # There should typically be one librarian message
        return LibrarianMessage.objects.first()


class EResourceListView(generics.ListAPIView):
    """
    List all electronic resources
    """
    serializer_class = EResourceSerializer
    queryset = EResource.objects.all()


class LibraryPolicyListView(generics.ListAPIView):
    """
    List all library policies
    """
    serializer_class = LibraryPolicySerializer
    queryset = LibraryPolicy.objects.all()


@api_view(['GET'])
def library_resources(request):
    """
    Get complete library resources including page content, e-resources, policies, and librarian message
    """
    # Get the library page content
    library_page, created = LibraryPage.objects.get_or_create(
        id=1,
        defaults={
            'mission': 'Default library mission',
            'vision': 'Default library vision',
            'objectives': 'Default library objectives',
            'quality_statement': 'Default quality statement',
            'value_1_title': 'Default Value 1',
            'value_1_description': 'Default value 1 description',
            'value_2_title': 'Default Value 2',
            'value_2_description': 'Default value 2 description',
            'value_3_title': 'Default Value 3',
            'value_3_description': 'Default value 3 description',
            'value_4_title': 'Default Value 4',
            'value_4_description': 'Default value 4 description',
        }
    )
    
    # Get related data
    e_resources = EResource.objects.all()
    policies = LibraryPolicy.objects.all()
    librarian_message = LibrarianMessage.objects.first()
    
    # Serialize the data
    library_serializer = LibraryPageSerializer(library_page, context={'request': request})
    e_resources_serializer = EResourceSerializer(e_resources, many=True, context={'request': request})
    policies_serializer = LibraryPolicySerializer(policies, many=True, context={'request': request})
    librarian_serializer = LibrarianMessageSerializer(librarian_message, context={'request': request}) if librarian_message else None
    
    response_data = {
        'library_page': library_serializer.data,
        'e_resources': e_resources_serializer.data,
        'policies': policies_serializer.data,
        'librarian_message': librarian_serializer.data if librarian_serializer else None
    }
    
    return Response(response_data, status=status.HTTP_200_OK)