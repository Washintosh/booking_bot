from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
  def __init__(self, boxes_section_element: WebElement):
    self.boxes_section_element = boxes_section_element
    self.deal_boxes = self.pull_deal_boxes()
  
  def pull_deal_boxes(self):
    return self.boxes_section_element.find_elements(by=By.CSS_SELECTOR, value = "div[data-testid='property-card']")
  
  def pull_information(self):
    print("Number of hotels:",len(self.deal_boxes))
    result = []
    for deal_box in self.deal_boxes:
      hotel_name = deal_box.find_element(by=By.CSS_SELECTOR, value = "div[data-testid='title']").get_attribute("innerHTML").strip()
      hotel_price = deal_box.find_element(by=By.CSS_SELECTOR, value = ".fcab3ed991.bd73d13072").get_attribute("innerHTML").strip()
      try:
        hotel_score = deal_box.find_element(by=By.CSS_SELECTOR, value = ".b5cd09854e.d10a6220b4").get_attribute("innerHTML").strip()
      except:
        hotel_score = 0
      result.append([hotel_name, hotel_price, hotel_score])
    return result
  

        