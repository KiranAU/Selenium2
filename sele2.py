
 with sc.Transform(transform=sc.Matrix44.get_translation_matrix(*self.model.position.value)):
            #Label
            with sc.Transform(look_at=sc.Transform.LookAt.CAMERA):
                sc.Arc(self._radius, axis=2, color=cl.yellow)
                sc.Line([0,0,0], [0, self._radius_hovered, 0], color=cl.yellow, thickness=self._thickness)
                sc.Line([0,self._radius_hovered,0], [self._radius_hovered, self._radius_hovered * 1.5, 0], color=cl.yellow, thickness=self._thickness)
                
                with sc.Transform(transform=sc.Matrix44.get_translation_matrix(self._radius_hovered + 5, self._radius_hovered *1.5, self._radius_hovered)):
                     with sc.Transform(scale_to=sc.Space.SCREEN):
                        with sc.Transform(transform=sc.Matrix44.get_translation_matrix(0,5,0)):
                            sc.Label(f"Tooltip:- the prim path is {self.model._current_path}.", color=cl.white, size=15)




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name  method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print (“Found “ + str(len(lists)) + “searches:”)

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
