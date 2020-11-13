# 无向图邻接矩阵的表示

class GraphAX:
    def __init__(self, vertx, mat):  # vertx 顶点表；mat邻接矩阵
        self.vnum = len(vertx)
        self.vertx = vertx
        self.mat = mat  # [mat[i][:] for i in range(vnum)]


def creat_matrix():
    nodes = ['v0', 'v1', 'v2', 'v3', 'v4']
    matrix = [[0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [0, 1, 0, 1, 1],
              [1, 0, 1, 0, 0],
              [0, 1, 1, 0, 0]]
    mygraph = GraphAX(nodes, matrix)
    return mygraph


def DFS1(graph, cur_vertx_indx):  # 递归方式
    global visited_list
    v = graph.vertx[cur_vertx_indx]
    print(v, end=' ')
    visited_list[cur_vertx_indx] = 1
    w = []
    for i in range(graph.vnum):
        if graph.mat[cur_vertx_indx][i] == 1 and visited_list[i] == 0:
            w.append(i)
    if len(w) != 0:
        for i in range(len(w)):
            a = w[i]
            if visited_list[a] == 0:
                DFS1(graph, a)


class Sstack():
    def __init__(self):
        self.slist = []

    def is_empty(self):
        if self.slist == []:
            return 1
        else:
            return 0

    def pushstack(self, data):
        self.slist.append(data)

    def popstack(self):
        return self.slist.pop()

def DFS2(graph, cur_vertx_indx):  # 非递归方式
    visited_li = [0] * graph.vnum
    s = Sstack()
    s.pushstack(cur_vertx_indx)
    print(graph.vertx[cur_vertx_indx], end=' ')
    visited_li[cur_vertx_indx] = 1
    while s.is_empty() !=1:
        for j in range(graph.vnum):
            if graph.mat[cur_vertx_indx][j]==1 and visited_li[j]==0:
                print(graph.vertx[j],end=' ')
                visited_li[j]=1
                s.pushstack(j)
                cur_vertx_indx=j
        if s.is_empty()!=1:
            cur_vertx_indx=s.popstack()


if __name__ == '__main__':
    graph = creat_matrix()
    print('图的顶点表为：')
    print(graph.vertx)
    print('\n图的邻接矩阵为®：')
    print(graph.mat)
    print('\n深度遍历（递归）:')
    visited_list = [0] * graph.vnum
    DFS1(graph, 0)
    print('\n\n深度遍历（非递归）:')
    DFS2(graph, 0)
