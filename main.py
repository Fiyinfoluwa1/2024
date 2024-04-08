import os
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

from selenium.webdriver.edge.service import service

 current_dir = os.path.dirname(os.path.realpath(__file__))

 driver_path = os.path.join(current_dir, "msedgedriver.exe")

 driver = webdriver.edge(service=service(driver_path))

