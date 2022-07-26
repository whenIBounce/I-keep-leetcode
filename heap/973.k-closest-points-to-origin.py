class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         
        def distance(point: List[int]) -> int:
            return (point[0])*(point[0]) + (point[1])*(point[1])
        def heapify(heap, i):
            while(True):
                maxpos = i
                left = i*2+1
                right = i*2+2
                if(left < k and distance(heap[left]) > distance(heap[maxpos])):
                   maxpos = left
                if(right < k and distance(heap[right]) > distance(heap[maxpos])):
                   maxpos = right
                if maxpos == i:
                   break
                tmp = heap[i]
                heap[i] = heap[maxpos]
                heap[maxpos] = tmp
                i = maxpos
            
        # 1. constructing the initial max heap 
        heap = points[0:k]

        for i in range((k-2)//2, -1, -1):
            heapify(heap, i)
    
        # 2. iterate through the rest of the points 
        for i in range(k, len(points)):
            # 3. UPDATE max heap WHEN current points distance is smaller than heap's max
            if (distance(points[i]) < distance(heap[0])):
                heap[0] = points[i]
                heapify(heap, 0)
        
        return heap
        
        