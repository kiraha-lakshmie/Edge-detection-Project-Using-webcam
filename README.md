# Edge Detection Project Using Webcam

## Description
This project demonstrates real-time edge detection using a webcam with Python and OpenCV.  
The system captures live video frames and detects edges using the Canny Edge Detection algorithm.

## Technologies Used
- Python
- OpenCV
- NumPy
- Webcam

## How It Works
1. Capture video from the webcam
2. Convert the frame to grayscale
3. Apply Gaussian blur to reduce noise
4. Use Canny Edge Detection to detect edges
5. Display the processed frame in real time

## Output

### Original Image
![Original Image](originalpicture.jpg)

### Edge Detection Output
![Edge Detection](Screenshot%20(111).png)

![Edge Detection](Screenshot%20(112).png)

## Installation

Clone the repository:

```
git clone https://github.com/kiraha-lakshmie/Edge-detection-Project-Using-webcam.git
```

Install dependencies:

```
pip install opencv-python numpy
```

Run the program:

```
python main.py
```

## Future Improvements
- Real-time object shape detection
- Raspberry Pi camera integration
- Edge-based object measurement
