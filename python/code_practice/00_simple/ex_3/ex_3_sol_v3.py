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

    def get_neighbors(self):
        return self.__neighbors


class CompaignMap:

    def __init__(self, MAP_HEIGHT=1, MAP_WIDTH=1):

        self.height = MAP_HEIGHT
        self.width = MAP_WIDTH
        self.area = MAP_HEIGHT*MAP_WIDTH
        self.index_y_max = MAP_HEIGHT-1
        self.index_x_max = MAP_WIDTH-1
