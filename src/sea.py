from math import sqrt
from event import Event
from enum import Enum

from log import LogState, LogUtil


class PlayerId(int, Enum):
    PLAYER_1 = 0
    PALYER_2 = 1


class SeaCaseId(int, Enum):
    WATER = 0
    SUBMARINE_1 = 1
    SUBMARINE_2 = 2
    SUBMARINE_3 = 3


class Sea(Event):
    """Sea class
    events :
    - update (sea) : call when an update is made on the board
    - hit ((sea, layer, x, y)) : call when a case is hit
    - sink ((sea, submarine_id)) : when a submarine is sinked
    - end (sea) : all submarines are sinked
    """    

    def __init__(self, height: int, width: int, layer_depth: list[int], submarines: list[int]) -> None:
        """Sea constructor

        Args:
            height (int): largeur du plateau
            width (int): hauteur du plateau
            layer_depth (list[int]): liste des profondeurs
            submarines (list[int]): taille des bateaux
        """       
        super().__init__()

        self.width = width
        self.height = height
        self.layers = layer_depth

        self.submarines = {}
        for i in range(len(submarines)):
            self.submarines[i + 1] = (submarines[i], True) # {sub_id: (sub_lenght, sinked: default True = not placed)}

        self.board = {} 
        for layer in layer_depth:
            self.board[layer] = [[(SeaCaseId.WATER, False) for _ in range(width)] for _ in range(height)]

    def updateSubmarines(self, layer_depth: int, x:int, y:int) -> None :
        """met à jour les sous-marins du jeu

        Args:
            layer_depth (int): profondeur
            x (int): position x [0, self.width-1]
            y (int): position y [0, self.hieght-1]
        """        
        case = self.board[layer_depth][y][x]

        isSink = True
        for layer,x,y in self.getSubmarineCases(case[0]):
            if not self.board[layer][y][x][1]:
                isSink = False
        
        if isSink:
            self.submarines[case[0]] = (self.submarines[case[0]][0], True)

            LogUtil.INFO(f"submarine sinked at layer:{layer_depth},x:{x},y:{y}")
            self.emit("sink", (self, case[0]))

            allSinked = True
            for id in self.submarines:
                _, sinked = self.submarines[id]
                if sinked == False:
                    allSinked = False
            
            if allSinked:
                LogUtil.INFO("all submarines sinked")
                self.emit("end", self)



    def hit(self, layer_depth: int, x: int, y: int) -> bool:
        """touche une case

        Args:
            layer_depth (int): profondeur à toucher
            x (int): position x [0, self.width-1]
            y (int): position y [0, self.height-1]

        Returns:
            bool: si la case a bien été touchée
        """        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            case = self.board[layer_depth][y][x]

            if case[1] == False:
                self.board[layer_depth][y][x] = (case[0], True)

                self.emit('update', self)
                
                if case[0] != SeaCaseId.WATER:
                    self.updateSubmarines(layer_depth, x, y)
                    self.emit('hit', (self, layer_depth, x, y))
                else:
                    self.emit("miss", (self, layer_depth, x, y))

                LogUtil.INFO(f"hit on layer:{layer_depth}, x:{x}, y:{y}")
                return True
    
        return False


    def getSubmarineCases(self, submarine_id: SeaCaseId):
        """renvoie les cases d'un sous-marin

        Args:
            submarine_id (SeaCaseId): le sous-marin à regarder

        Returns:
            (list[(int,int,int)]): liste des cases
        """        
        cases = []

        for layer in self.layers:
            for y in range(len(self.board[layer])):
                for x in range(len(self.board[layer][y])):
                    if self.board[layer][y][x][0] == submarine_id:
                        cases.append((layer, x, y))
        
        return cases


    def isAlign(self, pos: list[tuple[int, int]]):
        """vérifie sur les cases envoyées sont alignées

        Args:
            pos (list[tuple[int, int]]): listes des points (x,y)

        Returns:
            bool: True = les cases sont alignées
        """        
        vecteurs = []
        # calcul des vecteurs
        if len(pos) >= 2:
            for i in range(1, len(pos)):
                vecteurs.append((pos[i][0] - pos[i-1][0], pos[i][1] - pos[i-1][1]))


        # calcul des normes
        for x,y in vecteurs:
            if sqrt(pow(x, 2) + pow(y, 2)) != 1:
                return False    # Endpoint normes
        
        # calcul de la colinéarité
        if len(vecteurs) >= 2 :
            for i in range(len(vecteurs)-1):
                x,y = vecteurs[i]
                x2, y2 = vecteurs[i+1]

                if x*y2 != x2*y:
                    return False    # Endpoint colinéaire

        return True # Endpoint: aucune erreur trouvée


    def placeSubmarine(self, submarine_id: SeaCaseId, layer: int, pos: list[tuple[int, int]]) -> bool:
        """place un sous-marin sur la grille

        Args:
            submarine_id (SeaCaseId): identifiant du sous-marin
            layer (int): profondeur (à prendre depuis sea.layers)
            pos (list[tuple[int, int]]): listes des positions où il faut placer

        Returns:
            bool: [description]
        """        
        opperation_success = False

        # checking out of bounds
        case_selected = []

        # get all cases
        for x, y in pos:
            if x >= 0 and x < self.width and y >= 0 and y < self.height:
                if self.board[layer][y][x][0] == SeaCaseId.WATER:
                    if self.isAlign(case_selected + [(x, y)]):  # could be refactor
                        case_selected.append((x,y))

        # adding cases
        if len(case_selected) == self.submarines[submarine_id][0]:
            for case in case_selected:
                self.board[layer][case[1]][case[0]] = (submarine_id, False)  # converting submarine_id to SeaCaseId
                self.submarines[submarine_id] = (submarine_id, False)
        
            try:
                self.emit('update', self)
            except KeyError:
                pass
            
            opperation_success = True
            LogUtil.INFO(f"submarine {submarine_id} on layer {layer}")

        return opperation_success


    def __str__(self):
        return f"[Sea]\u007Bsubmarines:{self.submarines},board:{self.board}\u007D"


if __name__ == "__main__":
    # TEST VAR
    TEST_MAKE_SEA = False
    TEST_PLACEMENT = False
    TEST_HIT = True



    def show_sea(sea: Sea):
        for l in sea.layers:
            layer = sea.board[l]
            for y in range(len(layer)):
                for x in range(len(layer[y])):
                    if layer[y][x][0] == SeaCaseId.WATER and not layer[y][x][1]:
                        print("~", end="")
                    elif layer[y][x][0] == SeaCaseId.WATER and layer[y][x][1]:
                        print(".", end='')
                    elif layer[y][x][0] != SeaCaseId.WATER and not layer[y][x][1]:
                        print('#', end='')
                    elif layer[y][x][0] != SeaCaseId.WATER and layer[y][x][1]:
                        print('X', end='')
                print()
            print('-' * sea.width)


    if TEST_MAKE_SEA:
        s = Sea(5, 10, [100, 200, 300], [1, 2, 3])
        print(s)

    
    if TEST_PLACEMENT:
        s = Sea(5, 10, [100, 200, 300], [1, 2, 3])

        s.on('update', show_sea)

        # placement
        if s.placeSubmarine(SeaCaseId.SUBMARINE_1, s.layers[0], [(0, 0)]) :
            LogUtil.log(LogState.DEBUG, "test placement 1 : OK")
        else:
            LogUtil.log(LogState.ERROR, "test placement 1 : KO")

        # superposition
        if not s.placeSubmarine(SeaCaseId.SUBMARINE_2, s.layers[0], [(0, 0), (0, 1)]) :
            LogUtil.log(LogState.DEBUG, "test placement 2 : OK")
        else:
            LogUtil.log(LogState.ERROR, "test placement 2 : KO")

        # non aligné
        if not s.placeSubmarine(SeaCaseId.SUBMARINE_3, s.layers[1], [(5, 5), (6,6), (7,5)]) :
            LogUtil.log(LogState.DEBUG, "test placement 2 : OK")
        else:
            LogUtil.log(LogState.ERROR, "test placement 2 : KO")

        # correct
        if s.placeSubmarine(SeaCaseId.SUBMARINE_3, s.layers[1], [(5, 3), (6,3), (7,3)]) :
            LogUtil.log(LogState.DEBUG, "test placement 2 : OK")
        else:
            LogUtil.log(LogState.ERROR, "test placement 2 : KO")


    if TEST_HIT:
        s = Sea(5, 10, [100, 200, 300], [1, 2, 3])
        s.on('update', show_sea)

        # placement
        if s.placeSubmarine(SeaCaseId.SUBMARINE_1, s.layers[0], [(0, 0)]) :
            LogUtil.DEBUG("submarine placed on layer 100, x:0, y:0")

            if s.hit(s.layers[0], 0, 0) and s.submarines[SeaCaseId.SUBMARINE_1][1]:
                LogUtil.INFO("Test hit 1 : OK")
            else:
                LogUtil.ERROR("Test hit 1 : KO")

            if not s.hit(s.layers[0], 0, 0):
                LogUtil.INFO("Test hit 2 : OK")
            else:
                LogUtil.ERROR("Test hit 2 : KO")
                
        else:
            LogUtil.ERROR("cannot place the submarine")
