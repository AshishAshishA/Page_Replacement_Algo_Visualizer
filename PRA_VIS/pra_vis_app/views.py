from django.shortcuts import render
from .visualize_pra import Visualize

# Create your views here.
def choose_algo(request):
    return render(request,'pra_vis_app/choose_form.html',{})

obj_fifo=None
obj_lru=None

def initialize_object(frame:int):
    global obj_fifo
    global obj_lru
    obj_fifo=Visualize(frame)
    obj_lru=Visualize(frame)

def FIFO_LRU(request):
    if request.method=="POST":
        frame=int(request.POST.get('frame'))

        initialize_object(frame)
        pages=[]

        return render(request,'pra_vis_app/fifo_lru_vis.html',{"pages":pages})

    return render(request,'pra_vis_app/choose_form.html',{})

def FIFO_LRU_Working(request):
    if request.method=="POST":
        page=int(request.POST.get('page'))

        page_fault_fifo,pages_fifo=obj_fifo.FIFO(page)
        page_fault_lru,pages_lru=obj_lru.LRU(page)


        context={
            "curr_page":page,
            "page_fault_fifo":page_fault_fifo,
            "pages_fifo":pages_fifo,
            "page_fault_lru":page_fault_lru,
            "pages_lru":pages_lru,
        }

        return render(request,'pra_vis_app/fifo_lru_vis.html',context)
    return render(request,'pra_vis_app/choose_form.html',{})

