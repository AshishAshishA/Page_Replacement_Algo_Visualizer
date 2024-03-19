from django.urls import path
from .views import choose_algo,FIFO_LRU,FIFO_LRU_Working

urlpatterns=[
    path('',choose_algo,name='choose_algo'),
    path('fifo_lru/',FIFO_LRU,name='fifo_lru'),
    path('fifo_lru_working',FIFO_LRU_Working,name='fifo_lru_working'),
]