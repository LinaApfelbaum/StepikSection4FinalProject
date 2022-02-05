from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS_BAR) == True, \
            "Basket items are presented but should not be"

    def should_be_empty_basket_text_bar(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_BAR) == True, \
            "Empty basket bar notification is not presented but should be"
