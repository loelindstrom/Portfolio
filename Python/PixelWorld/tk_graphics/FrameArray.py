class FrameArray(list):
    def __init__(self):
        '''
        A class to be used in the PixelWorld class.
        It's a list constructed as a 2D array containing
        tkinter's tk.Frame()-objects.
        The frames in the array can be accessed easy with row and column index.
        The background of a frame can also be turned from white to black and vice versa.
        '''
        super().__init__()

    def get(self, row, column):
        '''
        Returns a frame from the array based on the row and column index of the frame.
        :param row: int
        :param column: int
        :return: Frame()
        '''
        return self[row][column]

    def turnOff(self, row, column):
        '''
        Turns the bakground of a frame at a certain row and column in the array
        from black to white.
        :param row: int
        :param column: int
        :return: None
        '''
        frame = self[row][column]
        frame.configure(bg='white')

    def turnOn(self, row, column):
        '''
        Turns the bakground of a frame at a certain row and column in the array
        from white to black.
        :param row:
        :param column:
        :return:
        '''
        frame = self[row][column]
        frame.configure(bg='black')