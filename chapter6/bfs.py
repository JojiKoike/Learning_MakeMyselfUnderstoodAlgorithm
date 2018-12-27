from collections import deque


# Build Graph Data and enqueue
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["jonny", "thom"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'

searched = []

# bfs solver
def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("{0} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(bfs("you"))








