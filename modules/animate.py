import modules.in_draw_menu as menus


def animate(window, background, playarray, open_input, WHITE, font):
    window.blit(background, (0,0))
    
    menus.in_draw_menu(window, open_input, WHITE, font)


    print("Starting list: " + str(playarray))


        
    index = 0

    for item in playarray:
            if item == 11:
                
                playarray11 = playarray[index: playarray.index(12)]
                playarray11.remove(11)
                playarray10 = playarray[:index]
                index +=1
            elif item == 12:
                
                playarray12 = playarray[index:playarray.index(13)]
                playarray12.remove(12)
                index +=1 
            elif item == 13: 
                
                playarray13 = playarray[index: playarray.index(14)]
                playarray13.remove(13)
            elif item == 14: 
                
                playarray14 = playarray[index: playarray.index(15)]
                playarray14.remove(14)
            elif item == 15:
                
                playarray15 = playarray[index:]
                playarray15.remove(15)
            else:

                index +=1
    
    print("10: " + str(playarray10))
    print("11: " + str(playarray11))


    P10 = Point("10", playarray10)
    P11 = Point("11", playarray11)

    print(P10._points_list)




#Class

class Point():

    def __init__(self, name, points_list):
        self._name     = name
        self._points_list = points_list
        self.pos = 0

    def __repr__(self):
        return('<Animal '+self._name + '>')


