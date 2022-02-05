

from sea_case import SeaCase


class WrongPosOnLayer(Exception):
    def __init__(self, layer, pos_x, pos_y):
        super().__init__(f'wrong position on {str(layer)} --> pos: x:{pos_x}, y:{pos_y}')


class Layer():

    def __init__(self, width: int, heigth: int, depth: int):
        self.depth = depth
        self.width = width
        self.height = heigth
        self.cases = [[SeaCase(x, y) for x in range(width)] for y in range(heigth)]

    # def add_submarine(self, submarine_case: SubmarineCase, x: int, y: int):
    #     """add a submarine case on the layer

    #     Args:
    #         submarine_case (SubmarineCase): the case to add
    #         x (int): pos x on layer
    #         y (int): pos y on layer

    #     Raises:
    #         WrongPosOnLayer: error raised on out of range index
    #     """
    #     if x >= 0 and x < self.width and y >= 0 and y < self.height:	# check indexError
    #         # check SeaCase availablity
    #         # submarine_case.set(self, x, y)
    #         pass
    #     else:
    #         raise WrongPosOnLayer(self, x, y)


    def __lt__(self, other):
        return self.depth < other
    
    def __str__(self):
        return f"[Layer]\u007Bwidth:{self.width},height:{self.height},depth:{self.depth}\u007D"


if __name__ == "__main__":
    # sorting algorime
    layers = [Layer(10, 10, x) for x in [300, 100, 200]]
    for l in layers:
        print(l)
    layers.sort()
    for l in layers:
        print(l)
    
    print(f"should be false: {layers[0] < layers[1]}")
