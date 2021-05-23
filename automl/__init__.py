import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

outliers = []
def detect_outliers(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
        z_score = (i - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

outlier_pt = detect_outliers(data)
outlier_pt