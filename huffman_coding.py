#Huffman Coding (Greedy)
#Build optimal prefix-free encoding
def huffman_coding(freq):
    import heapq
    heap=[[freq[i],i] for i in range(len(freq))]
    heapq.heapify(heap)
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        merged=[left[0]+right[0],left,right]
        heapq.heappush(heap,merged)
    return build_codes(heap[0])
def build_codes(node,code=""):
    if len(node)==2:
        return {node[1]:code}
    codes={}
    codes.update(build_codes(node[1],code+"0"))
    codes.update(build_codes(node[2],code+"1"))
    return codes
#Example: freq=[5,9,12,13,16,45]
#Complexity: O(n log n) time, O(n) space
