
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def collab_list(request):
    if request.method == 'GET':
        return Response({'message': 'List of collab'})
    elif request.method == 'POST':
        return Response({'message': 'Create new collab'})

@api_view(['GET', 'PUT', 'DELETE'])
def collab_detail(request, user_id):
    return Response({'message': f'collab {user_id} details'})