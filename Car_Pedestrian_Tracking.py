import cv2

#image of Car
img_file = "Traffic.jpg"
video = cv2.VideoCapture('Tesla.mp4')

#trained Car Classifier & Ped Classifier
car_classifier_file = "car_detector.xml"

#camra or video protocol kill if damaged or video has stopped
while True:
    (read_successful,frame) = video.read()

    if read_successful:
        grayscaled_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

#ped_classifier_file ='Ped_Tracker.xml'

#opencv Image
#img =cv2.imread(img_file)

#outline of color color in gray scale
#black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#car Classification
car_tracker = cv2.CascadeClassifier(car_classifier_file)

#Car Detection
cars = car_tracker.detectMultiScale(grayscaled_frame)

print(cars)



#Car Outline
for (x,y,w,h) in cars:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255,),2)





#Image Dispaly with face
cv2.imshow('Car_Pedestrian_Tracking.', grayscaled_frame )

#Close Post Action
cv2.waitKey()




print("Code Fin")
