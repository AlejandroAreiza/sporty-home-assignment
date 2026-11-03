from screenplay.ui.ui_element import UIElement

_SELECTION_CARD = "div:has(> #bet-slip-selection-remove)"


class BetSlip:
    SELECTION_COUNT = UIElement.by_id("the bet slip selection count", "bet-slip-count")
    MATCH = UIElement.by_css("the bet slip match", f"{_SELECTION_CARD} > div > div:first-child")
    SELECTION = UIElement.by_css(
        "the bet slip selection", f"{_SELECTION_CARD} > div > div:last-child"
    )
    ODDS = UIElement.by_css("the bet slip odds", f"{_SELECTION_CARD} + div > span")
    STAKE = UIElement.by_id("the stake input", "bet-slip-stake-input")
    TOTAL_STAKE = UIElement.by_id("the total stake", "bet-slip-total-stake")
    POTENTIAL_PAYOUT = UIElement.by_id("the potential payout", "bet-slip-potential-payout")
    PLACE_BET_BUTTON = UIElement.by_id("the Place Bet button", "bet-slip-place-bet")
    BALANCE = UIElement.by_id("the bet slip balance", "bet-slip-balance")
