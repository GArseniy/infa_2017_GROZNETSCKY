import graphics as gr
WIDTH_OF_WINDOW = 700
HEIGHT_OF_WINDOW = 500


class Group(list):
    def draw(self, window):
        for object in self:
            object.draw(window)


def window():
    return gr.GraphWin("Picture", WIDTH_OF_WINDOW, HEIGHT_OF_WINDOW)


def tree():
    pass


if __name__ == "__main__":
    window = window()
