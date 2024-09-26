## https://handsonai.medium.com/build-a-chat-bot-from-scratch-using-python-and-tensorflow-fd189bcfae45

import nltk
import tensorflow as tf
import numpy
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

from tensorflow import keras
from keras.layers.preprocessing.text_vectorization import TextVectorization
from keras.utils import pad_sequences
# from tensorflow.python.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.layers.experimental.preprocessing import TextVectorization

import tensorflow_text as tftext
from tensorflow_text.python.ops.tokenization import Tokenizer


#Download nltk data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


with open('data.txt','r',encoding='utf-8') as f:
    raw_data = f.read()

def preprocess(data):
    #Tokenize data
    tokens = nltk.word_tokenize(data)

    #Lowercase all words
    tokens = [word.lower() for word in tokens]

    #Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    #lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

# Preprocess data
processedData = [preprocess(qa) for qa in raw_data.split('\n')]



def train_llm(data):
    # Set parameters
    vocab_size = 5000
    embedding_dim = 64
    max_length = 100
    trunc_type = 'post'
    padding_type = 'post'
    oov_tok = "<OOV>"


    training_size = len(processedData)

    #tokenize data
    # tokenizer = Tokenizer().tokenize()
    #https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization

    #create sequences
    padded_sequences = pad_sequences(data) # this must take tokenized sentences and not raw data

    #create training data
    training_data = padded_sequences[:training_size]
    training_labels = padded_sequences[:training_size]

    #create model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(),
        tf.keras.layers.Dropout(),
        tf.keras.layers.Conv1D(64,5),
        tf.keras.layers.MaxPooling1D(pool_size=4),
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(64),
        tf.keras.layers.Dense(vocab_size,activation='softmax')
    ])

    model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    num_epochs =50
    history = model.fit(training_data, training_labels, epochs = num_epochs, verbose =2)

    return history




# Define function to predict answer
def predict_answer(model, tokenizer, question):
    # Preprocess question
    question = preprocess(question)
    # Convert question to sequence
    sequence = tokenizer.texts_to_sequences([question])
    # Pad sequence
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    # Predict answer
    pred = model.predict(padded_sequence)[0]
    # Get index of highest probability
    idx = np.argmax(pred)
    # Get answer
    answer = tokenizer.index_word[idx]
    return answer


# Start chatbot
while True:
    question = input('You: ')
    answer = predict_answer(model, tokenizer, question)
    print('Chatbot:', answer)











