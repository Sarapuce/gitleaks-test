import os

api_key = os.environ.get('API_KEY')

def feature_1():
    print("Feature 1")

def feature_2():
    print("Feature 2")

def first_feature():
    print("First feature")

def main():
    first_feature()
    feature_1()
    feature_2()
    print("Hello world")

main()
