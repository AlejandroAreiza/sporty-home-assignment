from screenplay.ui.ui_element import UIElement


class Receipt:
    MATCH = UIElement.by_id("the receipt match", "modal-success-match")
    STAKE = UIElement.by_id("the receipt stake", "modal-success-stake")
    ODDS = UIElement.by_id("the receipt odds", "modal-success-odds")
    PAYOUT = UIElement.by_id("the receipt payout", "modal-success-payout")
    CLOSE = UIElement.by_id("the receipt Close button", "modal-success-close")
