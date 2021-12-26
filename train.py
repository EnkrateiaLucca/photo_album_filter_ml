from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import argparse
  
# create a parser object
parser = argparse.ArgumentParser(description = "CLI tool for training")
  
# add argument
parser.add_argument("--epochs", type = int, 
                     help = "The number of epochs to train the model")
parser.add_argument("--batch_size", type = int,help="Batch size to use for\
                                                     training")
  
# parse the arguments from standard input
args = parser.parse_args()
  
EPOCHS = args.epochs
BATCH_SIZE = args.batch_size

print(EPOCHS)
print(BATCH_SIZE)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
train_generator = train_datagen.flow_from_directory(
        './data/preprocessed/train',  # this is the target directory
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=BATCH_SIZE,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
validation_generator = test_datagen.flow_from_directory(
        './data/preprocessed/test',
        target_size=(150, 150),
        batch_size=BATCH_SIZE,
        class_mode='binary')

model.fit_generator(train_generator, epochs=EPOCHS, 
                    validation_data=validation_generator)

model.save('basic_cnn_model')

