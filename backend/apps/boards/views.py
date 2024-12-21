
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def board_list(request):
    if request.method == 'GET':
        return Response({'message': 'List of boards'})
    elif request.method == 'POST':
        data = request.data
        return Response({'message': f'Board created with title: {data["title"]}'})

@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, board_id):
    return Response({'message': f'Board {board_id} details'})