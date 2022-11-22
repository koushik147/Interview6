class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: # if source is equal to destination then return 0
            return 0
        
        hmp = defaultdict(set) # creating a defaultdict of set
        for bus, route in enumerate(routes): # craeting the hashmap of frequencies of the bus and routes
            for stop in route:
                hmp[stop].add(bus)
        
        q = deque() # creating the deque
        q.append((source, 0)) # appending the source and destination to queue
        visited = set() # creating a set 
        visited.add(source) # adding the source to visited
        bus_seen = set() # creating the set

        while q: # run until the q and popping the q and store it in stop and count
            stop, count = q.popleft()
            if stop == target: # if stop is equal to target then return count
                return count
            for bus in hmp[stop]:  # for bus in hashmap of stop
                if bus not in bus_seen:  # if bus is not in seen the add it in the seen
                    bus_seen.add(bus)
                    for neighbor in routes[bus]: # for every neighbour in routes and not in visted append the neighbour and count to q
                        if neighbor not in visited:
                            q.append((neighbor, count + 1))
                            visited.add(neighbor) # add the neighbour in the visited
        return -1 # else return -1