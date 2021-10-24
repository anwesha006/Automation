import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    #initialzing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read th frames while the camera is on
        ret, frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    return image_name
    print("snapshot taken")

    #releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = 'OINcu0v11oMAAAAAAAAAARPUDic8v4bp8xyoxN6ay6BEHP62-XT90_7TLlIPzTZb'
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()