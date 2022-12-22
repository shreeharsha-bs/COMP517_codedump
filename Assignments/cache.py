# Shreeharsha Satish, 201665390

cache = []
requests = []  # Initializing empty cache and request lists with global scope

#   fifo(cache, requests) - implements FIFO cache management on requests and cache of fixed size
#   parameters - cache, requests -- cache = empty list, requests = list of positive integers
#   returns cache - 8 element list of pages requested in order with fifo cache management
def fifo(cache, requests):
    '''
        It requires us to just push out the first request that came in
        to accomodate a newer one at the top. Newer elements can be simply added in as long as the cache isn't completely full i.e.
        the total number of pages hasn't exceeded the cache size = 8.
    '''
    cache_size = 8
    #pdb.set_trace()
    for item in requests:
        if(item in cache):
            print("hit")
        else:
            print("miss")
            if(len(cache) == cache_size):
                cache = cache[1:]  # Evicting the first element by just shortening length so we keep the most recent 8 elements
            cache += [item]  # Adding new item
    return cache


#   lfu(cache, requests) - implements LFU cache management on requests and cache of fixed size
#   parameters - cache, requests -- cache = empty list, requests = list of positive integers
#   returns cache - 8 element list of pages requested in order with LFU cache management
def lfu(cache, requests):
    '''
        It requires us to keep track of the requests and how often they're made for each request. The least frequently requested
        elements can then be removed to make the cache fit into the required length of cache size = 8. The least frequently
        used/requested element is removed if the cache is full otherwise we can simply load the new request and keep track of the count.
    '''
    cache_size = 8
    #pdb.set_trace()
    countDictionary = dict.fromkeys(list(set(requests)), 0)  # Initializing a dictionary with a count of 0 for all the unique elements in the requests list

    for item in requests:
        countDictionary[item] += 1
        if(item in cache):
            print("hit")
        elif(len(cache) < cache_size and item not in cache):  # Cache size limit not reached
            print("miss")
            cache += [item]
        else:  #Eviction part
            print("miss")
            tempCountDictionary = dict()
            while(len(cache) >= cache_size):
                #pdb.set_trace()
                for element in cache:
                    tempCountDictionary[element] = countDictionary[element]  # tempCountDictionary has items and counts of elements currently in the cache
                tempCountDictionary = dict(sorted(tempCountDictionary.items()))  # Sorting the elements so the lower key will be evicted if they have same counts
                leastUsed = min(tempCountDictionary, key = tempCountDictionary.get)  # finding the least used element amongst the items currently in the cache
                cache.remove(leastUsed)  # Removing the least frequently used element
            cache += [item]  # Adding new item
    return cache


if __name__ == '__main__':
#   Getting the list of requests from user
    exitProgram = 0
    while True:
        while True:
            try:
                newRequest = int(input("Enter a page\n"))
                #pdb.set_trace()
                if((newRequest < 1) and newRequest != 0):
                    raise ValueError
                else:
                    if(newRequest == 0):
                        break
                    else:
                        requests += [newRequest]
            except ValueError:
                print("Please enter a positive integer to request a page or enter 0 if you want to stop requesting")

        print("Choose the eviction algorithm:")
#   Eviction part using FIFO or LFU or just quit the program
        while True:
            eviction_algo = input("press 1 for fifo or press 2 for lfu or press Q to quit the program\n")
            if(eviction_algo == 'Q'):
                exitProgram = 1
                break
            elif(eviction_algo == '1'):
                cache = fifo(cache, requests)
                print(cache)
                cache = []
                requests = []  # Clearing cache and requests
                break
            elif(eviction_algo == '2'):
                cache = lfu(cache, requests)
                print(cache)
                cache = []
                requests = []  # Clearing cache and requests
                break
            else:
                print("Wrong input, try again or press Q to exit\n")

        if(exitProgram == 1):  # Exit the program, since Q was pressed
            break
