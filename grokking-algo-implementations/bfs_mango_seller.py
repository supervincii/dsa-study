# Breadth-first search implementation of looking for a mango seller.
# A mango seller from the graph of people is the one with a name that ends with
# the letter m.

from collections import deque

graph = {}
# starting point of "you" points to the first degree connections arranged in an array
graph["you"] = ["alice", "bob", "claire"]

# each 1st degree connection points to their corresponding out-neighbor in an array
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]

# 2nd degree connection does not point to anyone signifying the end of the graph
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    while search_queue:
        print(search_queue, searched)
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)

    return False

search("you")
