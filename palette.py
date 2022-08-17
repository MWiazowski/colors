import binascii
from PIL import Image
import numpy as np
import scipy.cluster

def get_colors(image):

    NUM_CLUSTERS = 5
    im = Image.open(image)
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    vecs, dist = scipy.cluster.vq.vq(ar, codes)
    counts, bins = scipy.histogram(vecs, len(codes))
    index_max = scipy.argmax(counts)
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    return colour
