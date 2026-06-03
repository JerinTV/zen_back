from ultralytics import YOLO
import cv2

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Run detection
    results = model(frame)

    # Get detections for this frame
    detections = results[0]

    # Copy the frame for drawing
    output_frame = frame.copy()

    for box in detections.boxes:
        cls_id = int(box.cls[0])  # class id
        class_name = model.names[cls_id]  # e.g., 'person'

        # Only draw if the detected object is a person
        if class_name == "person":
            xyxy = box.xyxy[0].cpu().numpy().astype(int)
            confidence = float(box.conf[0])

            x1, y1, x2, y2 = xyxy
            cv2.rectangle(output_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(output_frame, f"{class_name} {confidence:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show filtered detection
    cv2.imshow("People Detection Only", output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()