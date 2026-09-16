


# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.saucedemo.com/")
#     page.locator("[data-test=\"username\"]").click()
#     page.locator("[data-test=\"username\"]").fill("standard_user")
#     page.locator("[data-test=\"password\"]").click()
#     page.locator("[data-test=\"password\"]").fill("secret_sauce")
#     page.locator("[data-test=\"login-button\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
#     page.get_by_text("Name (A to Z)Name (A to Z)").dblclick()
#     page.get_by_text("Name (A to Z)Name (A to Z)").click()
#     page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
#     page.get_by_text("Price (low to high)Name (A to").click()
#     page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
#     page.get_by_text("Price (high to low)Name (A to").click()
#     page.locator("[data-test=\"product-sort-container\"]").select_option("za")
#     page.locator("[data-test=\"product-sort-container\"]").select_option("az")
#     page.locator("[data-test=\"shopping-cart-link\"]").click()
#     page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()
#     page.locator("[data-test=\"continue-shopping\"]").click()
#     page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
#     page.locator("[data-test=\"shopping-cart-link\"]").click()
#     page.locator("[data-test=\"checkout\"]").click()
#     page.locator("[data-test=\"firstName\"]").click()
#     page.locator("[data-test=\"firstName\"]").fill("Usha")
#     page.locator("[data-test=\"lastName\"]").click()
#     page.locator("[data-test=\"lastName\"]").fill("Chapagain")
#     page.locator("[data-test=\"postalCode\"]").click()
#     page.locator("[data-test=\"postalCode\"]").fill("33770")
#     page.locator("[data-test=\"continue\"]").click()
#     page.locator("[data-test=\"finish\"]").click()
#     expect(page.locator("[data-test=\"complete-header\"]")).to_be_visible()
#     page.locator("[data-test=\"back-to-products\"]").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)


