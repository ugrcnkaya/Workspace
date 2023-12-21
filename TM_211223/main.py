import cv2
import numpy as np

def match_template(template_img_path, icon_img_path, threshold=0.8):
    template_img = cv2.imread(template_img_path)
    icon_img = cv2.imread(icon_img_path)

    result = cv2.matchTemplate(template_img, icon_img, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    yloc, xloc = np.where(result >= threshold)
    w = icon_img.shape[1]
    h = icon_img.shape[0]

    max_loc = (max_loc[0] + w, max_loc[1] + h)
    cv2.rectangle(template_img, max_loc, (max_loc[0] - w, max_loc[1] - h), (0, 255, 0), 2)

    cv2.imshow("Template", template_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return max_loc[0], max_loc[1], template_img

template_path = "player4.png"
icon_path = "previous_video.png"
x, y, result_img = match_template(template_path, icon_path)
print("Max Matching Location (x, y):", x, y)




