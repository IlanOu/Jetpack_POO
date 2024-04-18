import os
import time
import cv2

from tools.toolbox.Debug import Debug

Debug.prefixActive = False

class PhotoCapture:
    def __init__(self, output_dir="./photos"):
        self.output_dir = output_dir
        
        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def capture_photo(self):
        """
        Capture a photo using the connected USB camera and save it to the output directory.
        """
        # Initialize the camera
        cap = cv2.VideoCapture(0)

        # Capture a single frame
        ret, frame = cap.read()

        # Generate the output file name with a timestamp
        output_file = os.path.join(self.output_dir, f"photo_1.jpg")

        # Save the frame to the output path
        cv2.imwrite(output_file, frame)

        # Release the camera
        cap.release()

        print(f"Photo saved to: {output_file}")

    def run(self):
        """
        Run the photo capture process.
        """
        self.capture_photo()




if __name__ == "__main__":
    Debug.Log("Capture d'une photo en cours...")
    photo_capture = PhotoCapture()
    photo_capture.run()
    Debug.LogSuccess("Capture effectuée avec succès !")
    
    Debug.Log("Récupération du texte de l'image en cours")
    for i in range(3):
        Debug.LogWhisper("."*(i+1))
        time.sleep(0.5*i)
    
    text = "Voilà le texte de l'image !"
    Debug.LogSuccess("Texte récupéré sur l'image : \n" + text)
    