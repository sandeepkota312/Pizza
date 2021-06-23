from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pizza
from .serializers import PizzaSerializer
from .forms import CustomerForm
from .filters import pizzaFilter
from django.http import Http404
from django.forms import modelform_factory


def search(request):
    pizza_list = Pizza.objects.all()
    pizza_filter = pizzaFilter(request.GET, queryset=pizza_list)
    return render(request, 'pizza_list.html', {'filter': pizza_filter})


# Create your views here.
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'index.html', context)


@api_view(['GET', 'POST'])
def pizzacreateandview(request):
    if request.method == 'GET':
        contents = {
            "pizza_type": "regular or square",
            "pizza_size": "small or medium or large",
            "onion": "true or false",
            "tomato": "true or false",
            "corn": "true or false",
            "capsicum": "true or false",
            "cheese": "true or false",
            "jalapeno": "true or false",
        }
        return Response(contents)

    elif request.method == 'POST':
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create pizza': '/pizza-create/',
        'List or filter pizzas': '/pizza-list/',
        'pizza Details View-Update-Delete': '/pizza-detail/id/',
        'filter pizzas in html view': '/filter/',
        'Create pizzas in html view': '/new/'
    }
    return Response(api_urls)


@api_view(['GET'])
def pizzaList(request):
    size = request.GET.get('pizza_size')
    type = request.GET.get('pizza_type')
    List = Pizza.objects.all()
    filtering = []
    # print(size, type)
    if size is not None and type is not None:
        # print(0)
        for i in List:
            if i.pizza_size == size and i.pizza_type == type:
                filtering.append(i)
        serializer = PizzaSerializer(filtering, many=True)
        return Response(serializer.data)
    elif size is not None:
        # print(1)
        for i in List:
            if i.pizza_size == size:
                filtering.append(i)
        serializer = PizzaSerializer(filtering, many=True)
        return Response(serializer.data)
    elif type is not None:
        # print(2)
        for i in List:
            if i.pizza_type == type:
                filtering.append(i)
        serializer = PizzaSerializer(filtering, many=True)
        return Response(serializer.data)
    serializer = PizzaSerializer(List, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def pizzaDetail(request, pk):
    if request.method == 'GET':
        try:
            Data = Pizza.objects.get(id=pk)
            serializer = PizzaSerializer(Data, many=False)
            return Response(serializer.data)
        except Pizza.DoesNotExist:
            raise Http404("Pizza does not exist")
    elif request.method =='POST':
        Data = Pizza.objects.get(id=pk)
        serializer = PizzaSerializer(instance=Data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == 'DELETE':
        Data = Pizza.objects.get(id=pk)
        Data.delete()
        return Response("Pizza removed successfully.")

# @api_view(['POST'])
# def pizzaCreate(request):
#     serializer = PizzaSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def pizzaDelete(request, pk):
#     Data = Pizza.objects.get(id=pk)
#     Data.delete()
#     return Response("Pizza removed successfully.")
