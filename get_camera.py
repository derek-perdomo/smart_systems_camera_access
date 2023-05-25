import cv2

IP_1="rtsp://admin:ssl_pass@192.168.1.65:554/Streaming/Channels/102"
IP_2="rtsp://admin:ssl_pass@192.168.1.66:554/Streaming/Channels/102"
IP_3="rtsp://admin:ssl_pass@192.168.1.67:554/Streaming/Channels/102"
vcap1= cv2.VideoCapture(IP_1)
vcap2= cv2.VideoCapture(IP_2)
vcap3= cv2.VideoCapture(IP_3)
# Define the codec and create VideoWriter object\

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_cam3.avi', fourcc, 20.0, (1280, 720))
cap = vcap3

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    if ret:
        # Write the frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()