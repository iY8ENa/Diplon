from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    RESULTS_CONTAINER_LOCATOR = (By.ID, "block_left_pad")  # Контейнер с результатами поиска

    def has_result_with_text(self, text):
        results_container = self.driver.find_element(*self.RESULTS_CONTAINER_LOCATOR)
        result_items = results_container.find_elements(By.TAG_NAME, "div")
        for item in result_items:
            if text.lower() in item.text.lower():  # Поиск конкретного текста
                return True
        return False