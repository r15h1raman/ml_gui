import numpy as np

def predict(img_array, model, threshold):

    data = img_array.reshape(-1, img_array.shape[0], img_array.shape[1], img_array.shape[2])
    
    pred = model.predict(data)
    pred = np.where(pred > threshold, 1, 0)
    
    return pred.reshape(img_array.shape[0], img_array.shape[1], 1)

