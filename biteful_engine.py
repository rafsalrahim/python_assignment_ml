#!/usr/bin/env python3
# Biteful Engine, alpha release

# import the serious stuff
import pickle
import numpy as np
import pandas as pd
from sklearn import neighbors


# load the pickled model
def load_model(dump_file_path):
    dump_file = open(dump_file_path, "rb")
    model = pickle.load(dump_file)
    model = pickle.loads(model)

    dump_file.close()
    return model


# accept user input
def user_input():
    input_data = []
    input_data.append(int(input("year>")))
    input_data.append(int(input("month>")))
    input_data.append(int(input("date>")))
    input_data.append(int(input("store-id>")))
    input_data.append(int(input("item-id>")))

    return input_data


# the main function
def main():
    model = load_model("model_dump")
    
    #query_data = user_input()
    query_data = [2013, 1, 1, 25, 103665]

    prediction = model.predict([query_data])
    
    print(prediction)


# run the main function
main()
