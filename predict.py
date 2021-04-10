import numpy as np

def predict(img_array, model, threshold):

    data = img_array.reshape(-1, img_array.shape[0], img_array.shape[1], img_array.shape[2])
    
    pred = model.predict(data)
    # setting optimal threshold based on intensity histogram
    counts, bins = np.histogram(pred.flatten(), bins=np.exp(np.linspace(-15,0.5,30)))
    threshold = bins[np.where(counts == np.min(counts))[0]+1][0]
    pred = np.where(pred > threshold, 1, 0)
    return pred.reshape(img_array.shape[0], img_array.shape[1], 1)

