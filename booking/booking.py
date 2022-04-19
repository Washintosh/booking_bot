from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By
import os
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable #librería para crear tablas

class Booking(webdriver.Chrome):
  def __init__ (self, driver_path = r"C:\Users\Washington\Downloads", teardown = False): # driver_path es una propiedad que se ha creado para guardar la carpeta donde se encuentra el driver del Chrome. Y el teardown es creada para ingresar si se desea cerrar o no la ventana al finalizar el programa.
    self.driver_path = driver_path
    self.teardown = teardown
    os.environ["PATH"] += self.driver_path
    options = webdriver.ChromeOptions() #estas dos líneas sirven para que no de una advertencia en consola
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    super(Booking, self).__init__(options=options)
    self.implicitly_wait(15)
    self.maximize_window() #para maximizar la ventana del navegador
  
  def __exit__ (self, exc_type, exc_value, trace):
    if self.teardown:
      self.quit() 

  def land_first_page(self):
    self.get(const.BASE_URL)

  def change_currency(self, currency=None):
    currency_element = self.find_element(by = By.CSS_SELECTOR, value = "button[data-tooltip-text='Elegir tu moneda']")
    currency_element.click()
    selected_currency = self.find_element(by=By.CSS_SELECTOR, value = f"a[data-modal-header-async-url-param*='selected_currency={currency}']")
    selected_currency.click()

  def select_location (self, location):
    location_element = self.find_element(by=By.ID, value = "ss")
    location_element.clear() #sirve para limpiar el input en caso de que tenga algún texto
    location_element.send_keys(location)
    first_result = self.find_element(by=By.CSS_SELECTOR, value ="li[data-i='0']")
    first_result.click()

  def select_dates (self, check_in_date, check_out_date):
    check_in_element = self.find_element(by=By.CSS_SELECTOR, value =f"td[data-date='{check_in_date}']")
    check_in_element.click()
    check_out_element = self.find_element(by=By.CSS_SELECTOR, value =f"td[data-date='{check_out_date}']")
    check_out_element.click()

  def select_adults(self, number_adults):
    selection_element = self.find_element(by=By.ID, value = "xp__guests__toggle")
    selection_element.click()
    number_adults_element = self.find_element(by=By.ID, value ="group_adults").get_attribute("value") #get_attribute sirve para acceder a los atributos de una etiqueta en selenium. Da un string
    number_adults_element = int(number_adults_element)
    if number_adults > number_adults_element:
      increase_adults_element = self.find_element(by=By.CSS_SELECTOR, value = "button[aria-label='Aumenta el número de Adultos']")
      for _ in range(number_adults - number_adults_element): #por convención cuando la variable de iteración no va a ser usado como en este ejemplo, se utiliza el underscore
        increase_adults_element.click()
    elif number_adults < number_adults_element:
      decrease_adults_element = self.find_element(by=By.CSS_SELECTOR, value = "button[aria-label='Reduce el número de Adultos']")
      for _ in range(number_adults_element - number_adults):
        decrease_adults_element.click()
  
  def click_search(self):
    search_button = self.find_element(by=By.CSS_SELECTOR, value = "button[type='submit']")
    search_button.click()

  def apply_filtration(self):
    filtration = BookingFiltration(driver=self)
    filtration.select_rating(2,4)
    # filtration.sort_lowest_price_first()
  
  def report_results(self):
    hotel_list = self.find_element(by=By.ID, value = "search_results_table")
    report = BookingReport(hotel_list)
    table = PrettyTable(["Hotel name", "Price", "Score"])
    table.add_rows(report.pull_information())
    print(table)