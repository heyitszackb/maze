import pyxel

class MenuButton:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.active = False
        
    
    def draw(self):
        if self.active:
            pyxel.rect(self.x - 2, self.y + 4, len(self.text) * 4 + 4, 2, 8)
        pyxel.text(self.x, self.y, self.text, self.color)

    def setActive(self):
        self.active = True

    def setInactive(self):
        self.active = False

class Menu:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.menu_buttons = []

    def addButton(self, text): # (self.width//2) - (len(play)*3)//2
        if type(text) != str:
            raise TypeError("MenuButton title must be of type string")
        if len(text) == 0:
            raise ValueError("MenuButton title must not be empty")
        # if the title has already been taken by another button it cannot be added
        for menu_button in self.menu_buttons:
            if menu_button.text == text:
                raise ValueError("Menuutton title must be unique")

        self.menu_buttons.append(MenuButton(text, self.x - (len(text)*3)//2, self.y + len(self.menu_buttons) * 10, self.color))
    
    def draw(self):
        for menu_button in self.menu_buttons:
            menu_button.draw()
        
        # draw outline
        pyxel.rectb(self.x - 50, self.y - 10, 100, len(self.menu_buttons) * 10 + 10, 8)

    def setActiveMenuButton(self, text):
        for menu_button in self.menu_buttons:
            if menu_button.text == text:
                menu_button.setActive()
            else:
                menu_button.setInactive()

    def getActiveMenuButton(self):
        for menu_button in self.menu_buttons:
            if menu_button.active:
                return menu_button.text
    
    def rotateForwardActiveMenuButton(self):
        for i in range(len(self.menu_buttons)):
            if self.menu_buttons[i].active:
                self.menu_buttons[i].setInactive()
                if i == len(self.menu_buttons) - 1:
                    self.menu_buttons[0].setActive()
                else:
                    self.menu_buttons[i+1].setActive()
                break
    
    def rotateBackwardActiveMenuButton(self):
        for i in range(len(self.menu_buttons)):
            if self.menu_buttons[i].active:
                self.menu_buttons[i].setInactive()
                if i == 0:
                    self.menu_buttons[len(self.menu_buttons) - 1].setActive()
                else:
                    self.menu_buttons[i-1].setActive()
                break

class Background:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pyxel.bltm(self.x, self.y, 0, 0, 0, self.width, self.height)


class Screen:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

class TitleScreen(Screen):
    def __init__(self, game_name, width, height):
        super().__init__(title, width, height)
        # self.menu = Menu((self.width//2), 30, 7)
        # self.menu.addButton('play')
        # self.menu.addButton('settings')
        # self.menu.addButton('quit')
        # self.menu.setActiveMenuButton('play')

# TODO Add TitleScreen class

# A title screen should take a , width, height, and menu options in an array as the first 4 arguments

    def draw(self):
        pyxel.cls(0)
        pyxel.text((self.width//2) - (len(self.title)*3)//2,10, self.title, 7)
        self.menu.draw()





class App:
    def __init__(self):
        self.width = 128
        self.height = 128
        pyxel.init(self.width, self.height)
        pyxel.load('screens.pyxres')
        self.menu = Menu((self.width//2), 30, 7)
        self.menu.addButton('play')
        self.menu.addButton('settings')
        self.menu.addButton('quit')
        self.menu.setActiveMenuButton('play')

        self.background = Background(0, 0, self.width, self.height)

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_UP):
            self.menu.rotateBackwardActiveMenuButton()

        if pyxel.btnp(pyxel.KEY_DOWN):
            self.menu.rotateForwardActiveMenuButton()

    def draw(self):
        pyxel.cls(0)
        self.background.draw()
        title = "Magic Maze"
        pyxel.text((self.width//2) - (len(title)*3)//2,10, title, 7)
        self.menu.draw()

        # Button(play, (self.width//2) - (len(play)*3)//2,45, 7).draw()
        # Button(settings, (self.width//2) - (len(settings)*3)//2,60, 7).draw()
        # Button(quit, (self.width//2) - (len(quit)*3)//2,75, 7).draw()

        # pyxel.text((self.width//2) - (len(title)*3)//2,10, title, 7)
        # pyxel.text((self.width//2) - (len(play)*3)//2,45, play, 7)
        # pyxel.text((self.width//2) - (len(settings)*3)//2,60, settings, 7)
        # pyxel.text((self.width//2) - (len(quit)*3)//2,75, quit, 7)
        # pyxel.rect(self.x, 0, 8, 8, 9)

App()