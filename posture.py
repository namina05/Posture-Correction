import cv2
import mediapipe as mp
import numpy as np

#for drawing landmarks
mp_drawing = mp.solutions.drawing_utils

#model that runs face,hand and pose detection
mp_holistics = mp.solutions.holistic

#used for face landmark connections
mp_facemesh = mp.solutions.face_mesh


def calculate_angle(a,b,c):

    #contains x,y coordinates
    
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    #finds angle between 2 vectors BC and BA
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])

    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

def main():

    #to capture image usinf default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot access webcam")
        return


    #for processing of image captured in realtime
    with mp_holistics.Holistic(
        min_detection_confidence = 0.6,
        min_tracking_confidence = 0.6,
        ) as holistic:

        while cap.isOpened():
            ret,frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                return

            #converting BRG TO RGB for processing(cv = BRG , mp = RGB)
            image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = holistic.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

            
            #Draw facial landmarks if detected
            #First DrawingSpec -> landmark points style
            #Second DrawingSpec -> connection (mesh lines) style 
    
            if results.face_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    results.face_landmarks,
                    mp_facemesh.FACEMESH_TESSELATION,
                    mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
                    mp_drawing.DrawingSpec(color=(80, 255, 121), thickness=1, circle_radius=1)
                )

            # Draw Right Hand
            if results.right_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    results.right_hand_landmarks,
                    mp_holistics.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
                )

            # Draw Left Hand
            if results.left_hand_landmarks:
                mp_drawing.draw_landmarks(
                     image,
                    results.left_hand_landmarks,
                    mp_holistics.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
                )

            # Draw Pose
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_holistics.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                )

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                left_shoulder = [landmarks[11].x, landmarks[11].y]
                left_hip = [landmarks[23].x, landmarks[23].y]
                left_ear = [landmarks[7].x, landmarks[7].y]

                # Calculate angle
                angle = calculate_angle(left_ear, left_shoulder, left_hip)

                # Display angle
                cv2.putText(image, str(int(angle)),
                            tuple(np.multiply(left_shoulder, [640,480]).astype(int)),
                            cv2.FONT_HERSHEY_TRIPLEX, 0.5,
                            (255,255,255), 2, cv2.LINE_AA)

                # Posture check
                if angle < 150:
                    cv2.putText(image, "BAD POSTURE!",(50,50),cv2.FONT_HERSHEY_TRIPLEX,
                                1,(0,0,255),
                                3,
                                cv2.LINE_AA)
                else:
                    cv2.putText(image, "GOOD POSTURE :)",
                                (50,50),
                                cv2.FONT_HERSHEY_TRIPLEX,
                                1,
                                (0,255,0),
                                3,
                                cv2.LINE_AA)

            #show image
            cv2.imshow("Holistic Tracking", image)

            
            #press q to Quit
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
                
                
                
                
    
    
