import cv2
import pytesseract

# Read image
image = cv2.imread("/home/khushali/Documents/thesis/CamScanner-In-Python/paper.jpg")

# Pre-processing
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform Gaussian blur to remove noise
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# Perform adaptive thresholding to enhance image contrast
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Perform morphological operations to remove dots and other noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Perform text detection
text = pytesseract.image_to_string(gray, lang='eng',
        config='--psm 11 --oem 3')

# Print the extracted text
print(text)
