import cv2

# read the input
img = cv2.imread("Butter_Album_Cover.jpeg")
hh, ww = img.shape[:2]

# resize down, then back up
w, h = (16, 16)
result = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
result = cv2.resize(result, (ww, hh), interpolation=cv2.INTER_AREA)

# save result
cv2.imwrite("barn_pixelated.png", result)

# show result
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()