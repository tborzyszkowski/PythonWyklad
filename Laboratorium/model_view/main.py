import view

if __name__ == "__main__":
    view.model.setX(1,0)
    view.model.setX(1, 1)
    view.model.setX(1, 2)
    view.model.setO(2, 2)
    view.print_desk()
    view.print_who_win()
