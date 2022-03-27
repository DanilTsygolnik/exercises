class Square:

    def __init__(self, coord_y, coord_x, compaign_map: CompaignMap):
        self.__coord_y = coord_y
        self.__coord_x = coord_x
        self.__captured = False
        self.__neighbors = find_neighbors(self, compaign_map)

    def find_neighbors(self, compaign_map: CompaignMap):
        neighbors_list = []
        # neighbors top/bottom
        coord_y_min = 0
        coord_y_max = compaign_map.height_index
        # horizontal position is fixed
        top_neighbor_coord_x = bottom_neighbor_coord_x = self.coord_x
        top_neighbor_coord_y = self.coord_y - 1
        if top_neighbor_coord_y >= coord_y_min:
            neighbors_list.append([top_neighbor_coord_y, top_neighbor_coord_x])
        bottom_neighbor_coord_y = self.coord_y + 1
        if bottom_neighbor_coord_y <= coord_y_max:
            neighbors_list.append([bottom_neighbor_coord_y, bottom_neighbor_coord_x])
        
        # neighbors left/right
        coord_x_min = 0
        coord_x_max = compaign_map.width_index
        # vertical position is fixed
        left_neighbor_coord_y = right_neighbor_coord_y = self.coord_y
        left_neighbor_coord_x = self.coord_x - 1
        if left_neighbor_coord_x >= coord_x_min:
            neighbors_list.append([left_neighbor_coord_y, left_neighbor_coord_x])
        right_neighbor_coord_x = self.coord_x - 1
        if right_neighbor_coord_x >= coord_x_min:
            neighbors_list.append([right_neighbor_coord_y, right_neighbor_coord_x])

    def capture(self):
        self.__captured = True


