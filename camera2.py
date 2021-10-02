#Source: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# I utilized VideoCapture instead of a static image as shown in the tutorial link above. I also pixelated my image so the K-means will process faster
# and video does not freeze as much. Instead of displaying a histogram, I only display the most prominent color in a small image box to left of the real-time video frame. 

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return color 
	
webcam = cv2.VideoCapture(1) 

while (1):

	ret, img = webcam.read()
	im2 = img 
	color_set = img
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	
	hh, ww = img.shape[:2]

	# resize down, then back up
	w, h = (5, 5)
	result = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
	result = cv2.resize(result, (ww, hh), interpolation=cv2.INTER_AREA)

	img = result.reshape((result.shape[0] * result.shape[1],3)) #represent as row*column,channel number
	clt = KMeans(n_clusters=3) #cluster number
	clt.fit(img)

	hist = find_histogram(clt)
	color = plot_colors2(hist, clt.cluster_centers_)

	
	
	#plt.axis("off")
	#plt.imshow(bar)
	#plt.show()
	
	cv2.imshow("Cam", im2)
	color_set = np.full((100, 100, 3), color, np.uint8)
	cv2.imshow("color", color_set) 
	
	if cv2.waitKey(10) & 0xFF == ord('q'): 
		cap.release() 
		cv2.destroyAllWindows() 
		break 
