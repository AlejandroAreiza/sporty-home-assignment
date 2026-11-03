from screenplay.ui.ui_element import UIElement


class Header:
    BALANCE = UIElement.by_css("the header balance", "#header-balance span:last-child")
