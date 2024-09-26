'''
https://machinelearningmastery.com/develop-a-deep-learning-caption-generation-model-in-python/
'''

# import tensorflow
# print('tensorflow: %s'%tensorflow.__version__)
# import keras
# print('keras: %s'%keras.__version__)
from pickle import dump
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.preprocessing.image import image_utils
from keras.models import Model


def extract_features(directory):
    # image_utils.load_img
    # image_utils.img_to_array

    model = VGG16()
    model = Model(inputs = model.inputs, outputs = model.layers[-2].outputs)
    print(model.summary())

    features = dict()
    for name in listdir(directory):
        filename = directory + '/' + name
        image = image_utils.load_img(filename, target_size=(224,224))
        image = image_utils.img_to_array(image)

        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)

        feature = model.predict(image, verbose=0)

        image_id = name.split('.')[0]

        features[image_id] = feature

    return features

# extract features from all images
directory = 'Flickr8k_Dataset'
features = extract_features(directory)
print('Extracted Features: %d' % len(features))
# save to file
dump(features, open('features.pkl', 'wb'))




