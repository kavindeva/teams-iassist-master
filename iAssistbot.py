# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import re
import logging
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


#Data-logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('msteamsbot.log')
file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def post_response(value):
    """Locate and return respective response value in response column
    for an error_message sent by the user"""
    df1 = pd.read_csv("C:\\inetpub\\wwwroot\\iAssist_IT_support\\"
                      "Datasets\\Reference_Resol.csv", encoding="latin1", names=["Response", "Resolution"])

    # Locate resolution index value if it is presence and return it's respective solution message
    df1 = df1.loc[df1.Resolution.isin([value])]
    df2 = df1['Response']
    # print(type(df2))
    return df2


def get_final_output(predin, classes):
    """Return the resolution value which have higher confidential level"""
    resolution1 = None
    # Pick a numerical data from list of list
    predict = predin[0]

    # Convert a unique resolutions from list to numpy array
    classes = np.array(classes)

    # Sort the prediction values based on list index positions
    ids = np.argsort(-predict)

    # Change all the values in unique resolution's index positions as same as prediction values
    classes = classes[ids]

    # Now sort the prediction values in descending orders
    predict = -np.sort(-predict)

    # Return the only probability value between 0.7 to 1.0
    for i in range(predin.shape[1]):
        if 0.7 <= predict[i] <= 1.0:
            resolution1 = classes[i]
            logger.debug("%s has confidence = %s" % (classes[i], (predict[i])))
    return resolution1


def max_length(words):
    """Define function to find maximum length of message presence in error_message series"""
    return len(max(words, key=len))


def load_dataset(file_input):
    """A method to load the dataset in.csv format and separate Error messages,
    Resolutions and Unique error messages(without duplicates)."""
    df = pd.read_csv(file_input, encoding="latin1", names=["Error_Message", "Resolution"])
    resolution1 = df["Resolution"]
    unique_resolution1 = list(set(resolution1))
    error_message1 = list(df["Error_Message"])
    return resolution1, unique_resolution1, error_message1


# Load the dataFrame
resolution, unique_resolution, error_message = load_dataset("C:\\inetpub\\wwwroot\\iAssist_IT_support\\"
                                                            "Datasets\\chatDataset_all.csv")

# Convert resolution as string type
resolution = resolution.astype(str)

# Convert unique values as string and store it into a list
unique_resolution = list(map(str, unique_resolution))


def cleaning(sentences):
    """A method for cleaning and tokenizing the data in Error_Message using NLTK"""
    words = []
    for s in sentences:
        clean = re.sub(r'[^ a-zA-Z0-9]', " ", s)
        w = word_tokenize(clean)
        words.append([i.lower() for i in w])
    return words


# Clean the input error message for tokenizing convenience
cleaned_words1 = cleaning(error_message)
max_length = max_length(cleaned_words1)


def padding_doc(encoded, maxlength):
    """A method to pad all the sequences to get same length"""
    return pad_sequences(encoded, maxlen=maxlength, padding="post")


def create_tokenizer(words, filters='/!"#$%&()*+,-.:;<=>?@[\]^_`{|}~'):
    """Define a Keras preprocessing called 'tokenizer' method from tensorflow to updates internal vocabulary based
    on a list of texts, lower case all the data and tokenize from words to sequence data."""
    token = Tokenizer(filters=filters)
    token.fit_on_texts(words)
    return token


word_tokenizer = create_tokenizer(cleaned_words1)
# Load the model output file to predict an input error_message
modelFile = load_model("C:/inetpub/wwwroot/iAssist_IT_support/model/model_gitex.h5")


def predictions(textin):
    """Predict the confidential level of all unique resolutions for
    an error message sent by user and then return all prediction levels"""
    clean = re.sub(r'[^ a-zA-Z0-9*?%]', " ", textin)
    test_word = word_tokenize(clean)
    test_word = [w.lower() for w in test_word]

    # Tokenize the text data into a sequence
    test_ls = word_tokenizer.texts_to_sequences(test_word)

    # Check for unknown words
    if [] in test_ls:
        test_ls = list(filter(None, test_ls))
    test_ls = np.array(test_ls).reshape(1, len(test_ls))

    # Convert given error message's numerical index value into a maximum index value by adding zero's
    x = padding_doc(test_ls, max_length)
    prediction_out = modelFile.predict(x)
    return prediction_out


def get_index_value(text1):
    """Extract the value of resolution and
    predict the text value and then return accuracy value"""
    uniqueResolution = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
                        '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
                        '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61',
                        '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76',
                        '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
                        '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105',
                        '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118',
                        '119', '120']
    prediction = predictions(text1)

    # Return which class had accuracy level of above 0.7 and below 1.0
    resolution1 = get_final_output(prediction, uniqueResolution)

    # Separate only index values contains in numpy.int
    resolution1 = int(resolution1[:3])
    logger.debug(resolution1)
    return resolution1


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        inputTextMessage = str(turn_context.activity.text).lower()
        error_data = inputTextMessage
        logger.debug("iAssist bot Custom app text message received")
        index = get_index_value(error_data)
        logger.debug("Index value received")
        post = post_response(index)
        logger.debug("Post response value received")
        post = post.to_json()

        # Slice row index value and return only solution message
        text = post[6:-2]
        text1 = re.sub(r'\A:"', '', text)
        text2 = re.sub(r"\\", "", text1)
        data = re.sub(r'\Bu0092', "'", text2)
        logger.debug("Solution sliced")
        logger.debug("Solution fetched")
        await turn_context.send_activity(data)

    async def on_members_added_activity(
            self,
            members_added: [ChannelAccount],
            turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hi, Welcome to iAssist Support Assistance. Please provide your"
                                                 " error message below and I will create ticket for it.")
