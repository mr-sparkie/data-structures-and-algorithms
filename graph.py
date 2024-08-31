class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.g_dict = {}
        for st,end in self.edges:
            if st in self.g_dict:
                self.g_dict[st].append(end)
            else:
                self.g_dict[st] = [end]
        print(self.g_dict)
    def get_path(self,st,end,path=[]):
        path = path + [st]
        if st == end:
            return [path]
        if st not in self.g_dict:
            return []
        new_paths = []
        for node in self.g_dict[st]:
            if node not in path:
                new_path = self.get_path(node,end,path)
                for p in new_path:
                    new_paths.append(p)
        return new_paths

    def shortest_path(self,st,end):
        n =  self.get_path(st,end)
        return min(n)
route = [
    ('mumbai','dubai'),
    ('mumbai','paris'),
    ('dubai','paris'),
    ('paris','new york'),
    ('dubai','new york'),
    ('new york','boston'),
    ('new york','london'),
    ('london','boston')
]
g = Graph(route)
print(g.get_path('mumbai','new york'))
print(g.shortest_path('mumbai','new york'))
print(g.shortest_path('dubai','paris'))
