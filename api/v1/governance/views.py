from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from apps.governance.models import Chancellor, BoardMember, GovernanceBody
from .serializers import (
    ChancellorSerializer,
    BoardMemberSerializer,
    GovernanceBodySerializer
)


class ChancellorDetailView(generics.RetrieveAPIView):
    """
    Retrieve the chancellor information
    """
    serializer_class = ChancellorSerializer
    queryset = Chancellor.objects.all()

    def get_object(self):
        # There should typically be one chancellor
        return Chancellor.objects.first()


class BoardMemberListView(generics.ListAPIView):
    """
    List all board members
    """
    serializer_class = BoardMemberSerializer

    def get_queryset(self):
        board_type = self.request.query_params.get('board_type', None)
        if board_type:
            return BoardMember.objects.filter(board_type=board_type)
        return BoardMember.objects.all()


class GovernanceBodyListView(generics.ListAPIView):
    """
    List all governance bodies
    """
    serializer_class = GovernanceBodySerializer
    queryset = GovernanceBody.objects.all().prefetch_related('members')


class GovernanceBodyDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific governance body with its members
    """
    serializer_class = GovernanceBodySerializer
    queryset = GovernanceBody.objects.prefetch_related('members')


@api_view(['GET'])
def governance_structure(request):
    """
    Get complete governance structure with all bodies and members
    """
    # Get all governance bodies with their members
    governance_bodies = GovernanceBody.objects.prefetch_related('members').all()

    # Get chancellor if exists
    chancellor = Chancellor.objects.first()

    # Serialize the data
    bodies_serializer = GovernanceBodySerializer(
        governance_bodies,
        many=True,
        context={'request': request}
    )
    chancellor_serializer = ChancellorSerializer(
        chancellor,
        context={'request': request}
    ) if chancellor else None

    response_data = {
        'chancellor': chancellor_serializer.data if chancellor_serializer else None,
        'governance_bodies': bodies_serializer.data
    }

    return Response(response_data, status=status.HTTP_200_OK)