import cv2
def frameszamlalo():

# A videó elindítása
 camera = cv2.VideoCapture('eszterga.avi')

 length = int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
 print('Total number of frames: ', length )

 while True:
    frame = camera.read()[1]
    #reading the frame
    
    frameClone = frame.copy()
   
    cv2.imshow('Face', frameClone)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()

frameszamlalo() 



