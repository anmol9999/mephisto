import cv2

# loading image
img = cv2.imread('pikachu.jpg')


print(img)

cv2.imshow('Using CV2',img)
cv2.waitKey(5000)


