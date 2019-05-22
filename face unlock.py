#!/usr/bin/env python
# coding: utf-8

# In[18]:


import cv2
import os

os.mkdir("dir")
p= os.path.dirname(os.path.abspath("dir"))
p=p+"\dir"

camera = cv2.VideoCapture(0)
for i in range(30):
    return_value, image = camera.read()
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    face_cascade= cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
    faces = face_cascade.detectMultiScale(image,1.3,8)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,25,0),5)
        crop_img = image[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(p,'opencv'+str(i)+'.jpg'), crop_img )
del(camera)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




