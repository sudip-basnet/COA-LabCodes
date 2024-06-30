class FIFOPageReplacement:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []
        self.pages = set()
        self.hits = 0 

    def refer(self, page: int):
        
        if page in self.pages:
            self.hits += 1
        else:
            
            if len(self.cache) >= self.capacity:
                oldest_page = self.cache.pop(0)
                self.pages.remove(oldest_page)
           
            self.cache.append(page)
            self.pages.add(page)
        self.display(page)

    def display(self, page: int):
        print(f"Accessing page {page}:")
        print("Cache:", self.cache)
        print("Hits:", self.hits)
        print("\n")

    def get_hits(self):
        return self.hits


size = int(input("Enter the size of memory: "))
cache = FIFOPageReplacement(size)
pages = [2,3,2,1,5,2,4,5,3,2,5,2]

for page in pages:
    cache.refer(page)

hits = cache.get_hits()
ratio = hits/len(pages)
print("Hit ratio:", ratio)
