from playwright.sync_api import Page
import random

class InventoryPage:
    def __init__(self, page:Page):
        self.page = page

        self.random_addToCart = page.locator("[data-test^='add-to-cart']")
        self.random_addToCart1 = page.get_by_role("button", name="Add to cart")
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.add_to_cart_button2 = page.get_by_role("button", name= "add-to-cart-sauce-labs-bike-light")
        self.remove_button2 = page.get_by_role("button", name= "remove-sauce-labs-bike-light")
        self.product_sort_container = page.locator("[data-test=\"product-sort-container\"]")
        self.all_product_name = page.locator(".inventory_item_name")
        self.all_product_price = page.locator(".inventory_item_price")
        # self.sort_AZ_alpha = page.locator("[data-test=\"product-sort-container\"]")
        # self.sort_ZA_alpha = page.locator("[data-test=\"product-sort-container\"]")
        # self.sort_by_price = page.locator("[data-test=\"product-sort-container\"]")
        self.cart_container = page.locator("[data-test=\"shopping-cart-link\"]")
        self.continue_shopping = page.get_by_role("button", name = "Continue Shoping")
        self.checkout = page.get_by_role("button", name = "Checkout")


        # checkout Info
        self.FirstName = page.get_by_role("textbox", name="First Name")
        self.LastName = page.get_by_role("textbox", name="Last Name")
        self.Postalcode = page.get_by_role("textbox", name="Zip/Postal Code")
        self.Continue_checkout = page.get_by_role("button", name="Continue")
        self.Finish_Checkout = page.get_by_role("button", name="Finish")
        self.success_message = page.get_by_text("Thank you for your order!")


    def click_random_AddtoCart(self):
        randomproduct = self.random_addToCart.all()
        random.choice(randomproduct).click()
        

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def click_remove_from_cart(self):
        self.remove_button2.click()

    def sort_by_reverse_alpha(self):
        self.product_sort_container.select_option("za")

    def get_all_products_name(self):
        return self.all_product_name.all_text_contents()
    
    def get_all_products_price(self):
        return self.all_product_price.all_text_contents()
    
    def sort_by_lowHigh(self):
        self.product_sort_container.select_option("lohi")
    def sort_by_HighLow(self):
        self.product_sort_container.select_option("hilo")


    # def click_productSortContainer(self):
    #     self.product_sort_container.click()

    # def select_sort_by_Alpha(self, value):
    #     self.sort_AZ_alpha("az")

    # def select_sort_by_reverseAlpha(self, value):
    #     return self.sort_ZA_alpha("za")



    def click_cart(self):
        self.cart_container.click()

    def click_checkout(self):
        self.checkout.click()
    
    def input_checkoutInfo(self, firstname = str, lastname= str, postalcode= int):
        self.FirstName.fill("firstname")
        self.LastName.fill("lasname")
        self.Postalcode.fill("postalcode")

    def click_continue_checkout(self):
        self.Continue_checkout.click()
        
    def click_Finish(self):
        self.Finish_Checkout.click()

    def get_success_message(self):
        return self.success_message.text_content()
    

    

    

    








    

        # <button class="btn btn_primary btn_small btn_inventory " data-test="add-to-cart-sauce-labs-backpack" id="add-to-cart-sauce-labs-backpack" name="add-to-cart-sauce-labs-backpack" xpath="1">Add to cart</button>
