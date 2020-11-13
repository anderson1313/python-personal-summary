# 邻接表表示
class Anode:  # 边表节点类
    def __init__(self, adjvex, weight=0):
        self.Adjvex = adjvex  # 邻接点在顶点列表中的下标
        self.Next = None
        self.Weight = weight


class Vnode:  # 顶点表节点类
    def __init__(self, data):
        self.Data = data  # 顶点的值
        self.Firstarc = None  # 指向边表（单链表）的表头节点


class Graph:
    def __init__(self):
        self.vertList = []  # 表头列表
        self.numVertics = 0  # 实际顶点数

    def add_vertex(self, key):
        vertex = Vnode(key)
        self.vertList.append(vertex)
        self.numVertics = self.numVertics + 1
        return vertex

    def add_edge(self, val1, val2, weight=0):  # 在val1 顶点和val2节点之间添加一个权值为weight的边
        i = 0
        while i < len(self.vertList):  # 判断val1是否存在于顶点表中
            if val1 == self.vertList[i].Data:
                vnode1 = self.vertList[i]
                break
            i = i + 1
        if i == len(self.vertList):  # if不在，生成val1节点加入到顶点表中
            vnode1 = self.add_vertex(val1)

        i = 0
        while i < len(self.vertList):  # 判断val2是否存在于顶点表中
            if val2 == self.vertList[i].Data:
                vnode2 = self.vertList[i]
                break
            i = i + 1
        if i == len(self.vertList):  # if不在，生成val2节点加入到顶点表中
            vnode2 = self.add_vertex(val2)

        v2id = self.vertList.index(vnode2)
        p = Anode(v2id, weight)
        p.Next = vnode1.Firstarc  ##头插法
        vnode1.Firstarc = p

        # 将val2 加入到val1的边表中,采用头插法


class Queue:
    def __init__(self, maxsize=20):
        self.sequeue = maxsize * [None]
        self.front = 0
        self.rear = 0
        self.maxsize = maxsize

    def is_empty(self):
        if self.front == self.rear:
            return 1
        else:
            return 0

    def inqueue(self, data):
        for i in range(self.maxsize):
            if self.sequeue[i] == None:
                self.sequeue[i] = data
                self.rear += 1
                break

    def dequeue(self):
        self.front += 1
        return self.sequeue.pop(0)


def BFS(graph, cur_vertex_ind):
    visited_list = [0] * graph.numVertics
    q = Queue()
    visited_list[cur_vertex_ind] = 1
    q.inqueue(cur_vertex_ind)
    while q.is_empty() != 1:
        temp = q.dequeue()
        node = graph.vertList[temp]
        if node.Firstarc != None:
            start = node.Firstarc
            if visited_list[start.Adjvex] == 0:
                q.inqueue(start.Adjvex)
                visited_list[start.Adjvex] = 1
            while start.Next != None:
                second = start.Next
                if visited_list[second.Adjvex] == 0:
                    q.inqueue(second.Adjvex)
                    visited_list[second.Adjvex] = 1
                start = second
        print(graph.vertList[temp].Data, end=' ')



def degree_each_node(nodeid):
    count=0
    node=graph.vertList[nodeid]
    if node.Firstarc!=None:
        count+=1
        start = node.Firstarc
        while start.Next!=None:
            second = start.Next
            count+=1
            start = second
    return count

def degree_node(graph):
    for i in range(graph.numVertics):
        print("degree of {} is {}".format(graph.vertList[i].Data,degree_each_node(int(i))),end='\n')




if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex('v0')
    graph.add_vertex('v1')
    graph.add_vertex('v2')
    graph.add_vertex('v3')
    graph.add_vertex('v4')

    graph.add_edge('v0', 'v3')
    graph.add_edge('v0', 'v1')
    graph.add_edge('v1', 'v4')
    graph.add_edge('v1', 'v2')
    graph.add_edge('v1', 'v0')
    graph.add_edge('v2', 'v4')
    graph.add_edge('v2', 'v3')
    graph.add_edge('v2', 'v1')
    graph.add_edge('v3', 'v2')
    graph.add_edge('v3', 'v0')
    graph.add_edge('v4', 'v2')
    graph.add_edge('v4', 'v1')
    print('\n顶点表的元素为： ')
    for i in range(graph.numVertics):
        print(graph.vertList[i].Data, end=' ')

    print('\n\n邻接表的广度遍历：')
    BFS(graph, 0)

    print('\n')
    degree_node(graph)




