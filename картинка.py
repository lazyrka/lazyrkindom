from graph import *
import math
def ovalchik (a,b,ugolvrad,x0,y0):
    t=0
    oval=[]
    for i in range (1000):
        x=a*math.cos(t)
        y=b*math.sin(t)
        x1=x*math.cos(ugolvrad)-y*math.sin(ugolvrad)
        y1=x*math.sin(ugolvrad)+y*math.cos(ugolvrad)
        oval.append((x1+x0,y1+y0))
        t+=0.02
    polygon(oval)

windowSize(500, 350)
penColor('#FFE4B5') #персик
brushColor('#FFE4B5')
polygon([(0,0),(500,0),(500,50),(0,50)])
brushColor('#FFFFE0') #самый светлый
polygon([(0,50),(500,50),(500,110),(0,120)])
brushColor('#F0E68C')#желтый, который третий сверху
polygon([(0,120),(500,110),(500,200),(0,225)])
penColor('#FFFF00') #sun
brushColor('#FFFF00')
circle(250,40,30)
penColor('#D2691E') #рыжий,верхние горы
brushColor('#D2691E')
ovalchik(35,15,math.radians(-62),380,62)
polygon([(0,130),(500,80),(480,65),(470,75),(450,60),(430,65),(400,35),(350,75),(345,70),(330,85),(310,65),(290,101),(260,85),(230,90),(160,50),(155,40),(142,30),(65,90),(0,90)])
ovalchik(18,10,math.radians(30),453,72)
penColor('#FFFFE0')
brushColor('#FFFFE0')
ovalchik(22,8,math.radians(-46),347,68)
ovalchik(37,9,math.radians(-28),79,71)


penColor('#A52A2A')
brushColor('#A52A2A') #красный, нижние горы


ovalchik(90,40,math.radians(90),60,200)
ovalchik(80,40,math.radians(90),0,220)
ovalchik(50,20,math.radians(130),317,158)


brushColor('#A52A2A')
polygon([(500,200),(500,85),(480,115),(455,115),(450,130),(430,115),(410,150),(350,120),(290,170),(250,170),(230,125),(200,135),(170,180),(130,190),(120,170),(100,200),(0,200),(0,250)])
penColor('#FFB6C1')
brushColor('#FFB6C1')
polygon([(0,350),(500,350),(500,200),(0,225)])




run()
