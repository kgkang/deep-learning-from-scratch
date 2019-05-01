import numpy as np

class Operation():
    def __init__(self, input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []

        _default_graph.operations.append(self)
        for node in input_nodes:
            node.output_nodes.append(self)


    def compute(self):
        pass

class add(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var + y_var



class multiply(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var * y_var


class matmul(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)

class sigmoid(Operation):
    def __init__(self,z):
        super().__init__([z])

    def compute(self,z_val):
        return 1 / (1 + np.exp(-z_val))


class Placeholder():
    def __init__(self):
        self.output_nodes = []
        self.output = []
        _default_graph.placeholders.append(self)

class Variable():
    def __init__(self, initial_value = []):
        self.value = initial_value
        self.output_nodes = []
        self.output = []
        _default_graph.variables.append(self)

class Graph():
    def __init__(self):
        self.operations = []
        self.variables = []
        self.placeholders = []

    def set_as_default(self):
        global _default_graph
        _default_graph = self


def traverse_postorder(operation):
    """
    PostOrder Traversal of Nodes. Basically makes sure computations are done
    in the correct order(Ax first, then Ax + b). Feel free to copy and
    paste this.
    """
    nodes_postorder = []
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
            nodes_postorder.append(node)

    recurse(operation)
    return nodes_postorder



class Session():
    def run(self, operation, feed_dict={}):
        node_postorder = traverse_postorder(operation)

        for node in node_postorder:
            if type(node) == Placeholder:
                node.output = feed_dict[node]
            elif type(node) == Variable:
                node.output = node.value
            else:
                # Operation
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)

            if type(node.output) == list:
                node.output = np.array(node.output)

        return operation.output


