
def frameszamlalo():
 import cv2

# Elindul a képkockafolyam

 camera = cv2.VideoCapture('eszterga.avi')

 length = int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
 print('Total number of frames: ', length )

while True:
 frame = camera.read()[1]
    
    #Keret olvasása
    
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
 frameClone = frame.copy()
   
 cv2.imshow('Face', frameClone)
   
if cv2.waitKey(1) & 0xFF == ord('q'):
  break

  camera.release()
 cv2.destroyAllWindows()
 
 return frame

frameszamlalo()

