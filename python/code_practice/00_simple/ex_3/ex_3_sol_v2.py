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


class CompaignMap:
    '''
    многомерный массив с квадратами
    кол-во свободных квадратов
    '''

    def __init__(self, MAP_HEIGHT=1, MAP_WIDTH=1):
        
        def create_grid(grid_height, grid_width):
            
            def get_filled_row(row_num, grid_width):
                row_templ = []
                for col_num in range(0, grid_width):
                    # 0 в третьей позиции - статус клетки, "свободная"
                    row_templ.append([row_num, col_num, 0])
                return row_templ


            grid_templ = []
            # формируем сетку из готовых рядов ячеек
            for row_num in range(0, grid_height):
                grid_templ.append(get_filled_row(row_num, grid_width))
            return grid_templ


        self.height_index = MAP_HEIGHT-1
        self.width_index = MAP_WIDTH-1
        self.map_area = MAP_HEIGHT*MAP_WIDTH
        self.__grid = create_grid(MAP_HEIGHT, MAP_WIDTH)
        self.captured_squares = []


    def get_grid(self):
        return self.__grid

    def upd_grid(self, new_grid: list):
        self.__grid = new_grid

    def set_captured_squares(self, coord_list):
        # coord_list -- [ [y,x], [y,x], ... ]
        for i in coord_list:
            curr_coord_y = i[0]
            curr_coord_x = i[1]
            curr_square = self.__grid[curr_coord_y, curr_coord_x]

            

    def capture_squares():
        '''
        - перебор квадратов в массиве CompaignMap.captured_squares:
            curr_square =?? передать координаты??
            - если пустой -- скипаем
            - если занят - перебор соседей
            for neihbor in curr_square.neighbors:
                если свободен:
                    помечаем занятым
                    добавляем в CompaignMap.captured_squares
                если занят - к сл.
                    
                            и переходим к следующему
        - 

        '''

def count_compaign_days(current_map, compaign_day):
    '''
    заполнение карты происходит циклами, удобно реализовать рекурсивно
    на каждом вызове:
    - проверка свободных клеток -- current_map.__num_free_squares:
        - если не осталось -- вернуть число дней -- return compaign_days
        - если есть -- работа с картой
    - работа с картой:
        - заполнение свободных клеток карты, прилегающих к занятым
        renewed_map = fill_free_squares(current_map.get_grid())
            Внутри функции fill_free_squares(grid)
                - перебор квадратов:
                    - если пустой -- скипаем
                    - если занят -- заполняем соседей fill_neighbors(square_coord)
                                    и переходим к следующему
        - рекурсивный вызов функции с обновленными параметрами на вход
        return count_compaign_days(renewed_map, compaign_day+1)
    '''
