# Face Recognition Project

This project implements a face recognition system using Python, OpenCV, and face_recognition library. The system captures video from the webcam, detects faces, recognizes them, and provides audio feedback. The encoding data of known faces is precomputed and stored in a file for efficient recognition during real-time video capture.

## Features
- Detect faces in real-time from webcam feed.
- Recognize known faces using precomputed encodings.
- Display bounding boxes around detected faces with their names.
- Provide audio feedback welcoming the recognized person.
- Encode face data from images stored in a folder.
- Resize images for consistent processing.

## Setup and Installation

### Prerequisites
- Python 3.x
- OpenCV
- face_recognition
- pickle
- pyttsx3
- cvzone
- PIL (Pillow)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/KaanSezen1923/Face-Recognition.git
    cd face-recognition-project
    ```
2. Install the required packages:
    ```sh
    pip install opencv-python
    pip install face_recognition
    pip install pyttsx3
    pip install cvzone
    pip install Pillow
    ```

### Preparing Data
1. Place images of known individuals in a folder named `Data`.
2. Ensure that the images are named after the individuals (e.g., `John_Doe.jpg`).

### Encoding Known Faces
1. Run the script to encode the images:
    ```sh
    python face_encoder.py
    ```
2. This script will generate `EncodeFile.p`, which contains the encodings and names of the known individuals.

### Resizing Images
If you need to resize the images before encoding, you can use the provided resizing script:
```sh
python resize.py
```
By default, this script will resize images to 216x216 pixels.

## Running the Face Recognition
To start the face recognition system, run:
```sh
python main.py
```
The script will capture video from the webcam, detect faces, recognize them using the precomputed encodings, and provide audio feedback.

## File Descriptions

### `face_recognition.py`
Main script to perform real-time face recognition from webcam feed.

### `encode_faces.py`
Script to encode faces from images stored in the `Data` folder and save the encodings to `EncodeFile.p`.

### `resize_images.py`
Script to resize images in the `Data` folder to a target size (default 216x216 pixels).

## How It Works
1. **Loading Encodings**: The system loads precomputed encodings of known faces from `EncodeFile.p`.
2. **Capturing Video**: The webcam feed is captured in real-time.
3. **Face Detection and Recognition**: Faces are detected and recognized in each frame. If a face matches with known encodings, the name is displayed and an audio greeting is played.
4. **Bounding Boxes and Text**: Detected faces are highlighted with bounding boxes and the recognized name is displayed above each face.

## Notes
- Adjust the face distance threshold in `face_recognition.py` if the recognition accuracy is not satisfactory.
- Ensure the images in the `Data` folder are clear and the faces are properly visible.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- [OpenCV](https://opencv.org/)
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [pyttsx3](https://pyttsx3.readthedocs.io/)
- [cvzone](https://github.com/cvzone/cvzone)
- [Pillow](https://python-pillow.org/)

---

Feel free to adjust the README according to your specific project details and preferences.
