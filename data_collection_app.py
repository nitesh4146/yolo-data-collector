import cv2
import os
from datetime import datetime
import numpy as np

class DataCollector:
    def __init__(self):
        self.categories = ['mug', 'watch', 'spoon', 'cap', 'comb']
        self.base_dir = 'collected_data'
        self.setup_directories()
        self.cap = cv2.VideoCapture(0)
        self.is_collecting = False
        self.current_category = None
        self.image_counter = 0

    def setup_directories(self):
        # Create base directory if it doesn't exist
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)
        
        # Create category subdirectories
        for category in self.categories:
            category_dir = os.path.join(self.base_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

    def create_category_selection_window(self):
        # Create a black image for the selection window
        window_height = 300
        window_width = 400
        selection_image = np.zeros((window_height, window_width, 3), np.uint8)
        
        # Draw category buttons
        button_height = 40
        button_margin = 10
        start_y = 50
        
        for idx, category in enumerate(self.categories):
            # Draw button rectangle
            y = start_y + idx * (button_height + button_margin)
            cv2.rectangle(selection_image, (50, y), (window_width-50, y+button_height), (50, 50, 50), -1)
            
            # Add text
            text_size = cv2.getTextSize(category, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x = (window_width - text_size[0]) // 2
            text_y = y + (button_height + text_size[1]) // 2
            cv2.putText(selection_image, category, (text_x, text_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        return selection_image

    def select_category(self):
        selection_image = self.create_category_selection_window()
        cv2.imshow('Select Category', selection_image)
        
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                button_height = 40
                button_margin = 10
                start_y = 50
                
                for idx, category in enumerate(self.categories):
                    button_y = start_y + idx * (button_height + button_margin)
                    if 50 <= x <= 350 and button_y <= y <= button_y + button_height:
                        self.current_category = category
                        cv2.destroyWindow('Select Category')
        
        cv2.setMouseCallback('Select Category', mouse_callback)
        
        # Add a small delay to ensure the window is created
        cv2.waitKey(100)
        
        while True:
            try:
                if cv2.getWindowProperty('Select Category', cv2.WND_PROP_VISIBLE) <= 0:
                    break
            except cv2.error:
                break
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow('Select Category')
                break

    def start_collection(self):
        if not self.current_category:
            print("Please select a category first!")
            return
        
        self.is_collecting = True
        print(f"\nStarted collecting data for category: {self.current_category}")
        print("Press 'q' to stop collection")

    def stop_collection(self):
        self.is_collecting = False
        print("\nStopped collecting data")

    def run(self):
        if not self.cap.isOpened():
            print("Error: Could not open webcam")
            return

        print("\nWebcam Data Collection App")
        print("-------------------------")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Can't receive frame from webcam")
                break

            # Display the frame
            frame_height = frame.shape[0]
            
            # Add status text at the bottom
            status = "Recording" if self.is_collecting else "Stopped"
            category = self.current_category if self.current_category else "None"
            
            # Create status bar background
            cv2.rectangle(frame, (0, frame_height-80), (frame.shape[1], frame_height), (0, 0, 0), -1)
            
            # Add status texts
            cv2.putText(frame, f"Status: {status}", (10, frame_height-55),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Category: {category}", (10, frame_height-30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"Images: {self.image_counter}", (frame.shape[1]-200, frame_height-30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            cv2.imshow('Webcam Feed', frame)

            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.select_category()
            elif key == ord('b'):
                self.start_collection()
            elif key == ord('e'):
                self.stop_collection()
            elif key == ord(' '):  # Space bar pressed
                if self.current_category:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                    filename = f"{self.current_category}_{timestamp}.jpg"
                    save_path = os.path.join(self.base_dir, self.current_category, filename)
                    cv2.imwrite(save_path, frame)
                    self.image_counter += 1
                    print(f"Captured image: {filename}")
                else:
                    print("Please select a category first!")

        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    collector = DataCollector()
    print("\nControls:")
    print("'s' - Select category")
    print("'b' - Begin collection")
    print("'e' - End collection")
    print("'q' - Quit application")
    collector.run()
