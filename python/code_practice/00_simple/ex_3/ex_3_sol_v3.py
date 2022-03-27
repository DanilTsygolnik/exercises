class Square:
    '''
    класс создан для заполнения карты
    карта - двумерный массив, обращение по индексам
    следовательно, при создании Square нужно использовать индексы массива, а не координаты

    класс создается для наполнения сетки при создании карты CompaignMap
    '''

    def __init__(self, map_index_y, map_index_x, compaign_map):

        def find_neighbors(self, compaign_map):
            neighbors_list = []
            # neighbors top/bottom
            index_y_min = 0
            index_y_max = compaign_map.height - 1
            # horizontal position is fixed
            top_neighbor_index_x = bottom_neighbor_index_x = self.__index_x
            top_neighbor_index_y = self.__index_y - 1
            if top_neighbor_index_y >= index_y_min:
                neighbors_list.append([top_neighbor_index_y, top_neighbor_index_x])
            bottom_neighbor_index_y = self.__index_y + 1
            if bottom_neighbor_index_y <= index_y_max:
                neighbors_list.append([bottom_neighbor_index_y, bottom_neighbor_index_x])

            # neighbors left/right
            index_x_min = 0
            index_x_max = compaign_map.width - 1
            # vertical position is fixed
            left_neighbor_index_y = right_neighbor_index_y = self.__index_y
            left_neighbor_index_x = self.__index_x - 1
            if left_neighbor_index_x >= index_x_min:
                neighbors_list.append([left_neighbor_index_y, left_neighbor_index_x])
            right_neighbor_index_x = self.__index_x + 1
            if right_neighbor_index_x <= index_x_max:
                neighbors_list.append([right_neighbor_index_y, right_neighbor_index_x])
            return neighbors_list

        self.__index_y = map_index_y
        self.__index_x = map_index_x
        self.__captured = False
        self.__neighbors = find_neighbors(self, compaign_map)

    def get_index_y(self):
        return self.__index_y

    def get_index_x(self):
        return self.__index_x

    def get_neighbors(self):
        return self.__neighbors


class CompaignMap:

    def __init__(self, MAP_HEIGHT=1, MAP_WIDTH=1):

        def create_squares(compaign_map):

            def create_row(row_num, compaign_map):
                row_templ = []
                for col_num in range(0, compaign_map.width):
                    row_templ.append(Square(row_num, col_num, compaign_map))
                return row_templ


            grid_with_squares = []
            # формируем сетку из готовых рядов ячеек
            for row_num in range(0, compaign_map.height):
                grid_with_squares.append(create_row(row_num, compaign_map))
            return grid_with_squares


        self.height = MAP_HEIGHT
        self.width = MAP_WIDTH
        self.area = MAP_HEIGHT*MAP_WIDTH
        self.index_y_max = MAP_HEIGHT-1
        self.index_x_max = MAP_WIDTH-1
        self.grid = create_squares(self)

    def get_squares_indices(self):
        squares_ind = []
        for row in self.grid:
            for square in row:
                y = square.get_index_y()
                x = square.get_index_x()
                squares_ind.append([y,x])
        return squares_ind
