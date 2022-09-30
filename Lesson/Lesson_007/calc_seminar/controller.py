import gui
import data_base
import check


def start():
    data_base.save_info(gui.get_info())
    data = data_base.get_info()
    result = check.check(data)
    gui.send_info(result)
