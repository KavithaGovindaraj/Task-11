
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture
def driver():
    # Initialize the Edge driver
    options = webdriver.EdgeOptions()
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    # Navigate to the URL
    driver.get("https://jqueryui.com/droppable/")

    # Switch to the frame containing the draggable and droppable elements
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

    # Locate the draggable element (white rectangular box)
    draggable = driver.find_element(By.ID, "draggable")

    # Locate the droppable element (yellow rectangular box)
    droppable = driver.find_element(By.ID, "droppable")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Perform drag-and-drop operation
    actions.drag_and_drop(draggable, droppable).perform()

    # Optional: Verify if the drop was successful (e.g., check text or color change)
    assert "Dropped!" in droppable.text


#Output:

#Testing started at 12:29 ...
#Launching pytest with arguments jqueryui.py::test_drag_and_drop --no-header --no-summary -q in C:\Users\PREMA\PAT-28\pythonProject

#============================= test session starts =============================
#collecting ... collected 1 item

#jqueryui.py::test_drag_and_drop PASSED                                   [100%]

#============================= 1 passed in 13.16s ==============================

#Process finished with exit code 0