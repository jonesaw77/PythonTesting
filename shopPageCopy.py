from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def add_highest_priced_item_to_cart(self):
        print("Adding highest priced item to cart...")  # Helps to debug if this runs multiple times

        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        highPrice = 0.00
        totalPrice = 0.00
        highPrice_item = None

        for item in items:
            productPrice = item.find_element(By.CLASS_NAME, "inventory_item_price")
            price = float(productPrice.text.replace("$", ""))
            if price > highPrice:
                highPrice = price
                highPrice_item = item

        assert highPrice_item is not None, "No items found"
        highPrice_item.find_element(By.CSS_SELECTOR, "button").click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Check there is only ONE item in the basket
        basket_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        assert len(basket_items) == 1, f"More than one item found in cart: {len(basket_items)} items"

        basketTotal = basket_items[0]
        totalPrice = float(basketTotal.text.replace("$", ""))
        print("Cart price:", totalPrice, "Highest item price:", highPrice)

        return totalPrice, highPrice
