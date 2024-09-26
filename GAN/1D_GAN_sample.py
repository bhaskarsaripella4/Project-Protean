import matplotlib.pyplot as plt
import numpy as np
from keras import preprocessing
from keras.layers import Dense
from keras.models import Sequential
# from keras.utils.vis_utils import plot_model





# simple square function and plotting
def simple_function(x):
    return x*x

inputs = [-0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5]
outputs = [simple_function(x) for x in inputs]
# plt.plot(inputs, outputs)
# plt.show()

# generate actual samples function
def generate_real_samples(n=100):
    X1 = np.random.rand(n) - 0.5
    X2= X1*X1
    X1 = X1.reshape(n,1)
    X2 = X2.reshape(n,1)
    X = np.hstack((X1,X2))
    y = np.ones((n,1))
    return X,y

def fake_samples(n=100):
    X1 = np.random.rand(n) - 0.5
    X2 = X1 * X1
    X1 = X1.reshape(n, 1)
    X2 = X2.reshape(n, 1)
    X = np.hstack((X1,X2))
    y = np.zeros((n,1))
    return X,y

def generate_latent_points(latent_dim,n):
    x_input = np.random.rand(latent_dim*n)
    x_input = x_input.reshape(n,latent_dim)
    return x_input

# def generate_fake_samples(generator, latent_dim,n):
#     x_input = generate_latent_points(latent_dim, n)
#     X = generator.predict(x_input)
#     plt.scatter(X[:,0],X[:,1])
#     plt.show()

#generate fake samples same function above but with class labels set to 0 (1 is real samples).
def generate_fake_samples(generator, latent_dim, n):
    x_input = generate_latent_points(latent_dim,n)
    X = generator.predict(x_input)
    y = np.zeros((n,1)) #assigning class labels
    return X,y

def summarize_performance(epoch, generator, discriminator, latent_dim, n=100):
    x_real, y_real = generate_real_samples(n)
    _,acc_real = discriminator.evaluate(x_real,y_real,verbose=0)
    #prepare fake samples
    x_fake,y_fake = generate_fake_samples(generator,latent_dim,n)
    #evaluate discriminator on fake samples
    _,acc_fake = discriminator.evaluate(x_fake,y_fake,verbose=0)
    print(epoch, acc_real, acc_fake)
    plt.scatter(x_real[:, 0], x_real[:, 1], color='red')
    plt.scatter(x_fake[:, 0], x_fake[:, 1], color='blue')
    plt.show()

def train_gan(g_model, d_model, gan_model, latent_dim, n_epochs, n_batch, n_eval):
    #determine half size of batch for sample generation
    half_batch = int(n_batch/2)
    for i in range(n_epochs):
        x_real,y_real = generate_real_samples(half_batch)
        x_fake,y_fake = generate_fake_samples(g_model, latent_dim, half_batch)

        #update discriminator
        d_model.train_on_batch(x_real,y_real)
        d_model.train_on_batch(x_fake,y_fake)

        #prepare points in space as input for generator
        x_gan = generate_latent_points(latent_dim, n_batch)
        y_gan = np.ones((n_batch,1))

        #update generator via discriminator's error
        gan_model.train_on_batch(x_gan,y_gan)

        #evaluate model periodically
        if(i+1)%n_eval == 0:
            summarize_performance(i, g_model, d_model, latent_dim)

# data = generate_samples()
# plt.scatter(data[:,0],data[:,1])
# # plt.show()

#Discriminator model: This neural net detects whether the sample is real or generated(fake). Binary classification problem
def define_discriminator(n_inputs = 2):
    model = Sequential()
    model.add(Dense(25,activation='relu',kernel_initializer='he_uniform', input_dim=n_inputs))
    model.add(Dense(1,activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model

def define_generator(latent_dim, n_outputs=2):
    model = Sequential()
    model.add(Dense(15, activation='relu', kernel_initializer='he_uniform',input_dim=latent_dim))
    model.add(Dense(n_outputs, activation='linear'))
    # model.compile()
    model.summary()
    return model


def train_discriminator(model, n_epochs, *n_batch):
    if not len(n_batch):
        n_batch = (128,)

    half_batch = int(n_batch[0]/2)
    for i in range(n_epochs):
        X_real, y_real = generate_real_samples(half_batch)
        model.train_on_batch(X_real,y_real)
        X_fake, y_fake = fake_samples(half_batch)
        model.train_on_batch(X_fake, y_fake)

        _,acc_real = model.evaluate(X_real,y_real, verbose=0)
        _,acc_fake = model.evaluate(X_fake, y_fake, verbose=0)
        print(f"epoch {i},Training accurancy on real samples: {acc_real},generated: {acc_fake}")

def gan(generator, discriminator):
    discriminator.trainable = False

    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    model.compile(loss='binary_crossentropy',optimizer='adam')
    return model

# model = define_discriminator()
# train_discriminator(model, 1000)
#
# latent_dim = 5
# genModel = define_generator(latent_dim)
# generate_fake_samples(genModel,latent_dim,100)

latent_dim=5
discriminator = define_discriminator()
generator = define_generator(latent_dim)
gan_model = gan(generator, discriminator)
train_gan(generator,discriminator,gan_model,latent_dim,100,128,20)
gan_model.summary()

