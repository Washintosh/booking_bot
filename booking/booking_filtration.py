# se crea una clase para que agrupe todos los métodos de filtración
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver #esto sirve para añadir el tipo de dato explícitamente al driver
from selenium.webdriver.remote.webelement import WebElement

class BookingFiltration:
  def __init__(self, driver: WebDriver): #el driver explícitamente define su tipo de dato. Esto se hace para que funcione el autocompletado.
    self.driver = driver
  
  def select_rating (self, *star_values):
    rating_element  = self.driver.find_element(by = By.CSS_SELECTOR, value = "div[data-filters-group='class']")
    stars_elements = rating_element.find_elements(by = By.CSS_SELECTOR, value = "*") #se utiliza el asterisco para que de todos los elementos hijos de la etiqueta
    for star_value in star_values:
      for star_element in stars_elements:
        star_element: WebElement
        if star_element.get_attribute("innerHTML").strip() == f"{star_value} estrellas":
          star_element.click()

  def sort_lowest_price_first(self):
    self.driver.find_element(by=By.CSS_SELECTOR, value = "li[data-id='price']").click()
    