from utils import *

# Static Images
image = cv2.imread("model.jpg", cv2.IMREAD_UNCHANGED)
#output = apply_makeup(image, False, 'foundation', False)
#output = apply_makeup(image, False, 'blush', False)
output = apply_makeup(image, False, 'lips', False)

cv2.imshow("Original", image)
cv2.imshow("Feature", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
