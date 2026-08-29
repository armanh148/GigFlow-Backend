from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET', 'POST'])
def item_list_create(request):
    if request.method == 'GET':
        search = request.GET.get('search', '').strip()
        category = request.GET.get('category', 'All')
        item_status = request.GET.get('status', 'All')
        priority = request.GET.get('priority', 'All')
        sort_by = request.GET.get('sortBy', 'createdAt')
        sort_order = request.GET.get('sortOrder', 'desc')

        queryset = Item.objects.all()

        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        if category and category != 'All':
            queryset = queryset.filter(category=category)

        if item_status and item_status != 'All':
            queryset = queryset.filter(status=item_status)

        if priority and priority != 'All':
            queryset = queryset.filter(priority=priority)

        # Sorting mapping
        sort_map = {
            'createdAt': 'created_at',
            'title': 'title',
            'priority': 'priority',
            'price': 'price',
        }
        order_field = sort_map.get(sort_by, 'created_at')
        if sort_order == 'desc':
            order_field = f"-{order_field}"

        queryset = queryset.order_by(order_field)

        serializer = ItemSerializer(queryset, many=True)
        return Response({
            'status': 'success',
            'results': len(serializer.data),
            'data': {
                'items': serializer.data
            }
        }, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            newItem = serializer.save()
            return Response({
                'status': 'success',
                'message': 'Item created successfully',
                'data': {
                    'item': ItemSerializer(newItem).data
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'fail',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({
            'status': 'fail',
            'message': f"Item with ID '{pk}' not found"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response({
            'status': 'success',
            'data': {
                'item': serializer.data
            }
        }, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            updatedItem = serializer.save()
            return Response({
                'status': 'success',
                'message': 'Item updated successfully',
                'data': {
                    'item': ItemSerializer(updatedItem).data
                }
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'fail',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response({
            'status': 'success',
            'message': f"Item with ID '{pk}' successfully deleted"
        }, status=status.HTTP_200_OK)
