from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from apps.student_life.models import Service, Facility, RecreationFacility
from .serializers import (
    ServiceSerializer,
    FacilitySerializer,
    RecreationFacilitySerializer
)


class ServiceListView(generics.ListAPIView):
    """
    List all student services
    """
    serializer_class = ServiceSerializer
    queryset = Service.objects.all().order_by('order')


class ServiceDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific service
    """
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class FacilityListView(generics.ListAPIView):
    """
    List all facilities
    """
    serializer_class = FacilitySerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Facility.objects.filter(category=category)
        return Facility.objects.all()


class RecreationFacilityListView(generics.ListAPIView):
    """
    List all recreation facilities
    """
    serializer_class = RecreationFacilitySerializer
    queryset = RecreationFacility.objects.all()


class RecreationFacilityDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific recreation facility
    """
    serializer_class = RecreationFacilitySerializer
    queryset = RecreationFacility.objects.all()


@api_view(['GET'])
def student_services_and_facilities(request):
    """
    Get all student services and facilities
    """
    # Get all services ordered by order field
    services = Service.objects.all().order_by('order')
    
    # Get all facilities
    facilities = Facility.objects.all()
    
    # Get recreation facilities specifically
    recreation_facilities = RecreationFacility.objects.all()
    
    # Serialize the data
    services_serializer = ServiceSerializer(services, many=True, context={'request': request})
    facilities_serializer = FacilitySerializer(facilities, many=True, context={'request': request})
    recreation_serializer = RecreationFacilitySerializer(recreation_facilities, many=True, context={'request': request})
    
    response_data = {
        'services': services_serializer.data,
        'facilities': facilities_serializer.data,
        'recreation_facilities': recreation_serializer.data
    }
    
    return Response(response_data, status=status.HTTP_200_OK)