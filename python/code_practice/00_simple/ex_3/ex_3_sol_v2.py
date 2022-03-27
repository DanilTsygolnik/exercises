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


        self.__grid = create_grid(MAP_HEIGHT, MAP_WIDTH)
        self.__num_free_squares = MAP_HEIGHT*MAP_WIDTH

    def get_grid(self):
        return self.__grid

    def get_num_free_squares(self):
        return self.__num_free_squares

    def upd_grid(self, new_grid: list):
        self.__grid = new_grid

    def upd_num_free_squares(self, num):
        self.__num_free_squares = num
