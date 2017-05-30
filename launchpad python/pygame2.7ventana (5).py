

import serial, time
import pygame

 





def main():
    pygame.init()
    
    
    #pygame pantalla
    
    tamanio=(640,480)
    pantalla = pygame.display.set_mode(tamanio)
    pygame.display.set_caption("LAUNCHPAD")
    reloj= pygame.time.Clock()
    salir=False
#leer arduino
    arduino = serial.Serial('COM8', 9600)#lee arduino
    #arduino2 = serial.Serial('COM4', 9600)#lee arduino    
    time.sleep(2)
    detarduino=0
    rawString=""
    rawString2=""
    
     
        
        
   
    #canciones
    sonido1=pygame.mixer.Sound("b.wav")
    sonido2=pygame.mixer.Sound("c.wav")
    sonido3=pygame.mixer.Sound("d.wav")
    sonido4=pygame.mixer.Sound("e.wav")
    sonido5=pygame.mixer.Sound("f.wav")
    sonido6=pygame.mixer.Sound("g.wav")
    sonido7=pygame.mixer.Sound("h.wav")
    sonido8=pygame.mixer.Sound("i.wav")
    sonido9=pygame.mixer.Sound("j.wav")
    #piano
    sonido40=pygame.mixer.Sound("40.wav")
    sonido41=pygame.mixer.Sound("41.wav")
    sonido42=pygame.mixer.Sound("42.wav")
    sonido43=pygame.mixer.Sound("43.wav")
    sonido44=pygame.mixer.Sound("44.wav")
    sonido45=pygame.mixer.Sound("45.wav")
    sonido46=pygame.mixer.Sound("46.wav")
    sonido47=pygame.mixer.Sound("47.wav")
    sonido48=pygame.mixer.Sound("48.wav")
    sonido49=pygame.mixer.Sound("49.wav")
    #electro
    sonido50=pygame.mixer.Sound("50.wav")
    sonido51=pygame.mixer.Sound("51.wav")
    sonido52=pygame.mixer.Sound("52.wav")
    sonido53=pygame.mixer.Sound("53.wav")
    sonido54=pygame.mixer.Sound("54.wav")
    sonido55=pygame.mixer.Sound("55.wav")
    sonido56=pygame.mixer.Sound("56.wav")
    sonido57=pygame.mixer.Sound("57.wav")
    sonido58=pygame.mixer.Sound("58.wav")
    sonido59=pygame.mixer.Sound("59.wav")
    sonido60=pygame.mixer.Sound("60.wav")
    sonido61=pygame.mixer.Sound("61.wav")
    sonido62=pygame.mixer.Sound("62.wav")
    sonido63=pygame.mixer.Sound("63.wav")
    sonido64=pygame.mixer.Sound("64.wav")
    #electro2
    sonido65=pygame.mixer.Sound("65.wav")
    sonido66=pygame.mixer.Sound("66.wav")
    sonido67=pygame.mixer.Sound("67.wav")
    sonido68=pygame.mixer.Sound("68.wav")
    sonido69=pygame.mixer.Sound("69.wav")
    sonido70=pygame.mixer.Sound("70.wav")
    sonido71=pygame.mixer.Sound("71.wav")
    sonido72=pygame.mixer.Sound("72.wav")
    sonido73=pygame.mixer.Sound("73.wav")
    sonido74=pygame.mixer.Sound("74.wav")
    sonido75=pygame.mixer.Sound("75.wav")
    sonido76=pygame.mixer.Sound("76.wav")
    sonido77=pygame.mixer.Sound("77.wav")
    sonido78=pygame.mixer.Sound("78.wav")
    sonido79=pygame.mixer.Sound("79.wav")
    sonido80=pygame.mixer.Sound("65.wav")
    #electro 3
    
    sonido81=pygame.mixer.Sound("81.wav")
    sonido82=pygame.mixer.Sound("82.wav")
    sonido83=pygame.mixer.Sound("83.wav")
    sonido84=pygame.mixer.Sound("84.wav")
    sonido85=pygame.mixer.Sound("85.wav")
    sonido86=pygame.mixer.Sound("86.wav")
    sonido87=pygame.mixer.Sound("87.wav")
    sonido88=pygame.mixer.Sound("88.wav")
    sonido89=pygame.mixer.Sound("89.wav")
    sonido90=pygame.mixer.Sound("90.wav")
    sonido91=pygame.mixer.Sound("91.wav")
    sonido92=pygame.mixer.Sound("92.wav")
    sonido93=pygame.mixer.Sound("93.wav")
    sonido94=pygame.mixer.Sound("94.wav")
    sonido95=pygame.mixer.Sound("95.wav")
    sonido96=pygame.mixer.Sound("96.wav")



    #sonido arduino
    ardson1=sonido40
    ardson2=sonido41
    ardson3=sonido42
    ardson4=sonido43
    ardson5=sonido44
    ardson6=sonido45
    ardson7=sonido46
    ardson8=sonido47
    ardson9=sonido48
    ardson10=sonido49
    ardson11=sonido50

    #sonido arduino 2
    ardson12=sonido62
    ardson13=sonido63
    ardson14=sonido64
    ardson15=sonido65
    ardson16=sonido66
    ardson17=sonido67
    ardson18=sonido68
    ardson19=sonido69
    ardson20=sonido70
    ardson21=sonido71
    ardson22=sonido72
    

    
    while salir!=True:

#evento teclas
        for evento in pygame.event.get():
                  
            
            if evento.type== pygame.QUIT:
                salir =True
               
            
                        
            if evento.type==pygame.KEYDOWN:
                    if evento.key==pygame.K_1:
                        sonido1.stop()
                        sonido1.play(0)
            
                    if evento.key==pygame.K_2:
                        sonido2.stop()
                        sonido2.play(0)
            
                    if evento.key==pygame.K_3:
                        sonido3.stop()
                        sonido3.play(0)
                        
                    if evento.key==pygame.K_4:
                        sonido4.stop()
                        sonido4.play(0)
                        
                    if evento.key==pygame.K_5:
                        sonido5.stop()
                        sonido5.play(-1)

                    if evento.key==pygame.K_6:
                        sonido6.stop()
                        sonido6.play(0)

                    if evento.key==pygame.K_7:
                        sonido7.stop()
                        sonido7.play(0)

                    if evento.key==pygame.K_8:
                        sonido8.stop()
                        sonido8.play(0)

                    if evento.key==pygame.K_9:
                        sonido9.stop()
                        sonido9.play(0)
                        
                    #piano
                    if evento.key==pygame.K_q:
                        sonido40.stop()
                        sonido40.play(0)
                    if evento.key==pygame.K_w:
                        sonido41.stop()
                        sonido41.play(0)
                    if evento.key==pygame.K_e:
                        sonido42.stop()
                        sonido42.play(0)
                    if evento.key==pygame.K_r:
                        sonido43.stop()
                        sonido43.play(0)
                    if evento.key==pygame.K_t:
                        sonido44.stop()
                        sonido44.play(0)
                    if evento.key==pygame.K_y:
                        sonido45.stop()
                        sonido45.play(0)
                    if evento.key==pygame.K_u:
                        sonido46.stop()
                        sonido46.play(0)
                    if evento.key==pygame.K_i:
                        sonido47.stop()
                        sonido47.play(0)
                    if evento.key==pygame.K_o:
                        sonido48.stop()
                        sonido48.play(0)
                    if evento.key==pygame.K_p:
                        sonido49.stop()
                        sonido49.play(0)
                    #electro
                    if evento.key==pygame.K_a:
                        sonido50.stop()
                        sonido50.play(0)
                    if evento.key==pygame.K_s:
                        sonido51.stop()
                        sonido51.play(0)
                    if evento.key==pygame.K_d:
                        sonido52.stop()
                        sonido52.play(0)
                    if evento.key==pygame.K_f:
                        sonido53.stop()
                        sonido53.play(0)
                    if evento.key==pygame.K_g:
                        sonido54.stop()
                        sonido54.play(0)
                    if evento.key==pygame.K_h:
                        sonido55.stop()
                        sonido55.play(0)
                    if evento.key==pygame.K_j:
                        sonido56.stop()
                        sonido56.play(0)
                    if evento.key==pygame.K_k:
                        sonido57.stop()
                        sonido57.play(0)
                    if evento.key==pygame.K_l:
                        sonido58.stop()
                        sonido58.play(0)
                    if evento.key==pygame.K_x:
                        sonido59.stop()
                        sonido59.play(0)
                    if evento.key==pygame.K_c:
                        sonido60.stop()
                        sonido60.play(0)
                    if evento.key==pygame.K_v:
                        sonido61.stop()
                        sonido61.play(0)
                    if evento.key==pygame.K_b:
                        sonido62.stop()
                        sonido62.play(0)
                    if evento.key==pygame.K_n:
                        sonido63.stop()
                        sonido63.play(0)
                    if evento.key==pygame.K_m:
                        sonido64.stop()
                        sonido64.play(0)
                    #elctro 2
                    if evento.key==pygame.K_LSHIFT:
                        sonido65.stop()
                        sonido65.play(0)
                    if evento.key==pygame.K_KP_MULTIPLY:
                        sonido66.stop()
                        sonido66.play(0)
                    if evento.key==pygame.K_KP_ENTER:
                        sonido67.stop()
                        sonido67.play(0)
                    if evento.key==pygame.K_z:
                        sonido68.stop()
                        sonido68.play(0)
                    if evento.key==pygame.K_RSHIFT:
                        sonido69.stop()
                        sonido69.play(0)
                    if evento.key==pygame.K_KP9:
                        sonido70.stop()
                        sonido70.play(0)
                    if evento.key==pygame.K_KP0:
                        sonido71.stop()
                        sonido71.play(0)
                    if evento.key==pygame.K_KP1:
                        sonido72.stop()
                        sonido72.play(0)
                    if evento.key==pygame.K_KP2:
                        sonido73.stop()
                        sonido73.play(0)
                    if evento.key==pygame.K_KP3:
                        sonido74.stop()
                        sonido74.play(0)
                    if evento.key==pygame.K_KP4:
                        sonido75.stop()
                        sonido75.play(0)
                    if evento.key==pygame.K_KP5:
                        sonido76.stop()
                        sonido76.play(0)
                    if evento.key==pygame.K_KP6:
                        sonido77.stop()
                        sonido77.play(0)
                    if evento.key==pygame.K_KP7:
                        sonido78.stop()
                        sonido78.play(0)
                    if evento.key==pygame.K_KP8:
                        sonido79.stop()
                        sonido79.play(0)
                    if evento.key==pygame.K_LCTRL:
                        sonido80.stop()
                        sonido80.play(0)
                    #electro 3
                    if evento.key==pygame.K_UP:
                        sonido81.stop()
                        sonido81.play(0)
                    if evento.key==pygame.K_DOWN:
                        sonido82.stop()
                        sonido82.play(0)
                    if evento.key==pygame.K_LEFT:
                        sonido83.stop()
                        sonido83.play(0)
                    if evento.key==pygame.K_RIGHT:
                        sonido84.stop()
                        sonido84.play(0)
                    if evento.key==pygame.K_COLON:
                        sonido85.stop()
                        sonido85.play(0)
                    if evento.key==pygame.K_SEMICOLON:
                        sonido86.stop()
                        sonido86.play(0)
                    if evento.key==pygame.K_LESS:
                        sonido87.stop()
                        sonido87.play(0)
                    if evento.key==pygame.K_KP_MINUS:
                        sonido88.stop()
                        sonido88.play(0)
                    if evento.key==pygame.K_KP_PLUS:
                        sonido89.stop()
                        sonido89.play(0)
                    if evento.key==pygame.K_COMMA:
                        sonido90.stop()
                        sonido90.play(0)
                    if evento.key==pygame.K_MINUS:
                        sonido91.stop()
                        sonido91.play(0)
                    if evento.key==pygame.K_PERIOD:
                        sonido92.stop()
                        sonido92.play(0)
                    if evento.key==pygame.K_SLASH:
                        sonido93.stop()
                        sonido93.play(0)
                    if evento.key==pygame.K_KP_PERIOD:
                        sonido94.stop()
                        sonido94.play(0)
                    if evento.key==pygame.K_KP_DIVIDE:
                        sonido95.stop()
                        sonido95.play(0)
                    if evento.key==pygame.K_F1:
                        detarduino=1



                    #parar
                    if evento.key==pygame.K_SPACE:
                        sonido1.stop()
                        sonido2.stop()
                        sonido3.stop()
                        sonido4.stop()
                        sonido5.stop()
                        sonido6.stop()
                        sonido7.stop()
                        sonido8.stop()
                        sonido9.stop()
                        sonido40.stop()
                        sonido41.stop()
                        sonido42.stop()
                        sonido43.stop()
                        sonido44.stop()
                        sonido45.stop()
                        sonido46.stop()
                        sonido47.stop()
                        sonido48.stop()
                        sonido49.stop()
                        sonido50.stop()
                        sonido52.stop()
                        sonido53.stop()
                        sonido54.stop()
                        sonido55.stop()
                        sonido56.stop()
                        sonido57.stop()
                        sonido58.stop()
                        sonido59.stop()
                        sonido60.stop() 
                        sonido61.stop()
                        sonido62.stop()
                        sonido63.stop()
                        sonido64.stop()
                        sonido65.stop()
                        sonido66.stop()
                        sonido67.stop()
                        sonido68.stop()
                        sonido69.stop()
                        sonido70.stop()
                        sonido71.stop()
                        sonido72.stop()
                        sonido73.stop()
                        sonido74.stop()
                        sonido75.stop()
                        sonido76.stop()
                        sonido77.stop()
                        sonido78.stop()
                        sonido79.stop()
                        sonido80.stop()
                        sonido81.stop()
                        sonido82.stop()
                        sonido83.stop()
                        sonido84.stop()
                        sonido85.stop()
                        sonido86.stop()
                        sonido87.stop()
                        sonido88.stop()
                        sonido89.stop()
                        sonido90.stop()
                        sonido91.stop()
                        sonido92.stop()
                        sonido93.stop()
                        sonido94.stop()
                        sonido95.stop()
                        sonido96.stop()
        #arduino
        while detarduino==1:                
       
            rawString = int(arduino.readline())
            print rawString
           
            
        #botones arduino1
            if rawString==12:#parar  
                ardson1.stop()
                ardson2.stop()
                ardson3.stop()
                ardson4.stop()
                ardson5.stop()
                ardson6.stop()
                ardson7.stop()
                ardson8.stop()
                ardson9.stop()
                ardson10.stop()
                ardson11.stop()
                
                
            if rawString==1:
                ardson1.stop()
                ardson1.play(0)
            

            if rawString==2:
                ardson2.stop()
                ardson2.play(0)
                
            if rawString==3:
                ardson3.stop()
                ardson3.play()
                
            if rawString==4:
                ardson4.stop()
                ardson4.play(0)
                
            if rawString==5:
                ardson5.stop()
                ardson5.play(0)
                
            if rawString==6:
                ardson6.stop()
                ardson6.play(0)
                
            if rawString==7:
                ardson7.stop()
                ardson7.play(0)
                
            if rawString==8:
                ardson8.stop()
                ardson8.play(0)

            if rawString==9:
                ardson9.stop()
                ardson9.play(0)

            if rawString==10:
                ardson10.stop()
                ardson10.play(0)

            if rawString==11:
                ardson11.stop()
                ardson11.play(0)

            
            #cambia la musica de todos los pines
            if rawString==13:
                ardson1=sonido51
                ardson2=sonido52
                ardson3=sonido53
                ardson4=sonido54
                ardson5=sonido55
                ardson6=sonido56
                ardson7=sonido57
                ardson8=sonido58
                ardson9=sonido59
                ardson10=sonido60
                ardson11=sonido61
                
########################botones arduino2 ###############################################


            
        #accionar funciones
        reloj.tick(60)
        pygame.display.update()
    pygame.quit()
main()
