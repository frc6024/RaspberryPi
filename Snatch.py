import cv2
import urllib.request as rq
import numpy as np
from filterer import GripPipeline as GripPipeline
from networktables import NetworkTables

stream=rq.urlopen('http://localhost/?action=stream')

#NetworkTables.initialize(server="10.60.24.83")

#sd = NetworkTables.getTable("camera")


byt = bytes()
while True:
    byt += stream.read(1024)
    a = byt.find(b'\xff\xd8')
    b = byt.find(b'\xff\xd9')
    
    if a!=-1 and b!=-1:
        jpg = byt[a:b+2]
        byt= byt[b+2:]
        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        if cv2.waitKey(1) == 27:
            exit(0)
        
        PipeObj = GripPipeline()
        PipeObj.process(img)
        highest = (-1,True)
        
        #for contour in PipeObj.filter_contours_output:
        #    j = cv2.contourArea(contour)
        #    highest = (j,contour) if j > highest[0] else highest

        #for contour in PipeObj.find_contours_output:
            #x,y,w,h = cv2.boundingRect(contour)
            
         #   cv2.rectangle(PipeObj.inputIn,(x,y),(x+w,y+h),(0,0,255),2)
        
        #rect = cv2.boundingRect(highest[1])
        #box = np.int0(cv2.boxPoints(rect))
        #cv2.drawContours(PipeObj.cv_resize_output,[box],0,(0,0,255),2)
        

        """
        cx=(box[0][0]+box[1][0]+box[2][0]+box[3][0])/4
        cy=(box[0][1]+box[1][1]+box[2][1]+box[3][1])/4
        width=max(box[0][0],box[1][0],box[2][0],box[3][0])-min(box[0][0],box[1][0],box[2][0],box[3][0])
        height=max(box[0][1],box[1][1],box[2][1],box[3][1])-min(box[0][1],box[1][1],box[2][1],box[3][1])
        area=highest[0]
        dat=[cx,cy,width,height,area]
        if (sd.getBoolean('detect')):
            sd.putNumberArray("response",dat)
            sd.putBoolean('detect',False)
        """
        cv2.imshow('i',PipeObj.hsv_threshold_output)
