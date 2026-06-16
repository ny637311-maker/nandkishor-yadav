class Camera:
    def click_photos(self):
        print("photo clicked")

class Phone:
    def call(self):
        print("calling")

class Smartphone(Camera,Phone):
    def browser(self):
        print("browsing internet")

s = Smartphone()
s.click_photos()
s.call()
s.browser()
