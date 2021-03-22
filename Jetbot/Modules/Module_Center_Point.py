import cv2

def ToaDoTam(img):
    h, w, d = img.shape
    x_center, y_center = w//2, h//2
    cv2.circle(img, (x_center, y_center), 5, (255, 255, 0))
    return x_center, y_center