import cv2
import NetWork4

cap = cv2.VideoCapture('video.mp4')

poses = NetWork4.get_poses()
while (True):

    # Capture frames in the video
    ret, frame = cap.read()

    # describe the type of font
    # to be used.
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Use putText() method for
    # inserting text on videos


    cv2.putText(frame,
                f'{poses}',
                (50, 50),
                font, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)

    # Display the resulting frame
    cv2.imshow('video', frame)

    # creating 'q' as the quit
    # button for the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()