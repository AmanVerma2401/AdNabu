from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open website
driver.get("https://adnabu-store-assignment1.myshopify.com/")


# Create explicit wait object
wait = WebDriverWait(driver, 10)


# Wait for password input field and enter password
input_password = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#password"))
)

input_password.click()
input_password.send_keys("AdNabuQA")


# Wait for submit button and click
submit_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

submit_button.click()


# Wait for search icon and click
search_icon = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal__toggle-open.icon.icon-search")
    )
)

search_icon.click()


# Wait for search input box
search_box = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/sticky-header/header/div/details-modal/details/div/div[2]/predictive-search/form/div[1]/input[1]")
    )
)

search_box.click()

# Enter product name
search_box.send_keys("The Multi-managed Snowboard")

# Press ENTER
search_box.send_keys(Keys.ENTER)


# Wait for product selection and click
product_selection = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#CardLink--7801364611162")
    )
)

product_selection.click()


# Wait for Add to Cart button and click
add_to_cart = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/main/section[1]/section/div/div[2]/product-info/div[4]/product-form/form/div/button")
    )
)

add_to_cart.click()


# Close browser
driver.quit()