import gui
import data_base
import check


def start():
    data_base.save_info(gui.get_info())
    data = data_base.get_info()
    result = check.check(data)
    data_base.sve_result(result)
    gui.send_info(result)
    data_base.log(data, result)
