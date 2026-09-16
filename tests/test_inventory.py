from pages.Inventorypage import InventoryPage
from playwright.sync_api import expect
import random
import pytest

@pytest.mark.order(2)
def test_sortProduct_by_Alpha(page):
    inventory = InventoryPage(page)
    inventory.sort_by_reverse_alpha()
    names = inventory.get_all_products_name()
    assert names == sorted(names, reverse= True)


@pytest.mark.order(3)
def test_sortProduct_by_price(page):
    inventory = InventoryPage(page)
    inventory.sort_by_lowHigh()
    lohi = inventory.get_all_products_price()
    print(lohi)
    inventory.sort_by_HighLow()
    hilo = inventory.get_all_products_price()
    print(hilo)
    assert hilo == list(reversed(lohi))


   



def test_addProductToCart(page):
    inventory = InventoryPage(page)
    
    inventory.click_add_to_cart()
    cart_count = page.locator(".shopping_cart_badge")
    expect(cart_count).to_have_text("1")
    # cart_count = page.locator(".shopping_cart_badge").text_content()
    # assert (cart_count) == "1"
    # expect (cart_count) == 1

def test_random_addProductToCart(page):
    inventory = InventoryPage(page)
    inventory.click_random_AddtoCart()
    cart_count = page.locator(".shopping_cart_badge")
    expect(cart_count).to_have_text("2")


def test_checkout(page):
    inventory = InventoryPage(page)
    inventory.click_cart()
    inventory.click_checkout()
    inventory.input_checkoutInfo("Ram", "Sharma", 3370)
    inventory.click_continue_checkout()
    inventory.click_Finish()
    expect(inventory.success_message).to_be_visible()
    



# def add_multiple_products(self, count_to_add=3):
#     buttons = self.random_addToCart
#     total = buttons.count()

#     selected = random.sample(range(total), count_to_add)

#     for i in selected:
#         buttons.nth(i).click()
    




