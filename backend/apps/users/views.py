
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        return Response({'message': 'List of users'})
    elif request.method == 'POST':
        return Response({'message': 'Create new users'})

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, user_id):
    return Response({'message': f'users {user_id} details'})