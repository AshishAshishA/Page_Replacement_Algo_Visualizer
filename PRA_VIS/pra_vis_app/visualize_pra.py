from collections import deque

class Visualize:
    
    def __init__(self,frame):
        self.set=set()
        self.map={}
        self.que=deque()
        self.duplicate_que=deque()
        self.pages=[]
        self.frame=frame
        self.page_fault=0
        self.index=0
        self.recent_index=0

    def FIFO(self,page: int):
        if page not in self.set:
            if len(self.set)<self.frame:
                self.set.add(page)
                self.que.appendleft((page,self.index))
                self.index+=1
                self.page_fault+=1
            else:
                curr_page,curr_ind=self.que.pop()
                self.set.remove(curr_page)
                self.set.add(page)
                self.que.appendleft((page,curr_ind))
                self.page_fault+=1

        self.duplicate_que=self.que.copy()
        self.pages.clear()
        self.pages=[-1]*self.frame
        while self.duplicate_que:
            page,ind=self.duplicate_que.pop()
            self.pages[ind]=page

        self.pages.reverse()
        return self.page_fault,self.pages

    def LRU(self,page:int):
        if page not in self.set:
            if len(self.set)<self.frame:
                self.set.add(page)
                self.map[page]=(self.index,self.recent_index)
                self.index+=1
                self.recent_index+=1
                self.page_fault+=1
            else:
                least_recent=float('inf')
                value=0
                for x in self.set:
                    if self.map[x][1]<least_recent:
                        least_recent=self.map[x][1]
                        value=x

                self.set.remove(value)
                self.set.add(page)
                copy_index=self.map[value][0]
                self.map[page]=(copy_index,self.recent_index)
                self.recent_index+=1
                self.page_fault+=1
        else:
            copy_index=self.map[page][0]
            self.map[page]=(copy_index,self.recent_index)
            self.recent_index+=1

        self.pages.clear()
        self.pages=[-1]*self.frame

        for page in self.set:
            # print(f"page:{self.map[page][0]} ",end=" ")
            self.pages[self.map[page][0]]=page

        self.pages.reverse()

        return self.page_fault,self.pages

if __name__=="__main__":
    
    v=Visualize(4)
    for i in range (10):
        page=int(input(f"Page {i} : "))
        page_fault,pages=v.LRU(page)
        print(f"\n{page_fault} page fault")
        for j in pages:
            print(j)


    