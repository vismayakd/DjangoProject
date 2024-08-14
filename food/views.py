from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import ItemAddForm

# Create your views here.
# def myindex(request):
#     return HttpResponse("Hi Vismaya Wecome Back")


def items(request):
    item_list = Items.objects.all()
    template = loader.get_template('food/index.html')
    context ={
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,item_id):
    item = Items.objects.get(pk=item_id)
    context = {
        'item':item
    }
    return render(request,'food/detail.html',context)

def add_item(request):
    form = ItemAddForm(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect('food:items')


    return render(request, 'food/additem_form.html',context)

def edit_item(request,item_id):
    item = Items.objects.get(id=item_id)
    form = ItemAddForm(request.POST or None, instance=item)
    context = {
        'form':form,
        'item':item
    }
    if form.is_valid():
        form.save()
        return redirect('food:items')


    return render(request, 'food/additem_form.html',context)

def delete_item(request,item_id):
    item = Items.objects.get(id=item_id)
    print("delete", item)
    if request.method == 'POST':
        item.delete()
        return redirect('food:items')
    context = {
        'item':item
    }

    return render(request, 'food/delete.html',context)