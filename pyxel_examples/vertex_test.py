import random

class Vertex:
    def __init__(self, vid, x, y, contents):
        self.vid = vid
        self.x = x
        self.y = y
        self.contents = contents
        self.edges = []

    def __str__(self):
        return f"Vertex {self.vid}: ({self.x}, {self.y})"
    
class Edge:
    def __init__(self, eid, v1, v2):
        self.eid = eid
        self.v1 = v1
        self.v2 = v2
        self.weight = 1
        self.blocked = random.choice([True, False])

    def __str__(self):
        return f"Edge {self.eid}: ({self.v1}, {self.v2})"
    
def createGrid():
    # create the vertexes
    vertexes = []
    vid = 0
    for y in range(10):
        for x in range(10):
            num = random.randint(0, 1)
            contents = 'A' if num == 0 else 'B'
            vertex = Vertex(vid, x, y, contents)
            vertexes.append(vertex)
            vid += 1

    # create the edges
    edges = []
    eid = 0
    for vertex in vertexes:
        x, y = vertex.x, vertex.y
        if x > 0:
            # connect to left vertex
            left_vertex = vertexes[y * 10 + x - 1]
            edge = Edge(eid, vertex, left_vertex)
            edges.append(edge)
            vertex.edges.append(edge)
            left_vertex.edges.append(edge)
            eid += 1
        if y > 0:
            # connect to top vertex
            top_vertex = vertexes[(y - 1) * 10 + x]
            edge = Edge(eid, vertex, top_vertex)
            edges.append(edge)
            vertex.edges.append(edge)
            top_vertex.edges.append(edge)
            eid += 1
    return vertexes, edges


def print_grid(vertexes, edges):
    # print top border
    print("+" + "-" * 19 + "+")

    for y in range(10):
        row1 = "|"
        row2 = "|"

        for x in range(10):
            vertex = vertexes[y * 10 + x]
            contents = vertex.contents.center(3)
            row1 += f" {contents} |"

            if x < 9:
                edge = vertex.edges[1] # right edge
                if edge.blocked:
                    row2 += " | "
                else:
                    row2 += "   "
            if y < 9:
                edge = vertex.edges[2] # bottom edge
                if edge.blocked:
                    row1 += "---+"
                else:
                    row1 += "   +"
                row2 += "   |"

        print(row1)
        print(row2)

    # print bottom border
    print("+" + "-" * 19 + "+")

vertexes, edges = createGrid()

print_grid(vertexes, edges)