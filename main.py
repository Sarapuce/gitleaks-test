import os

api_key = os.environ.get('API_KEY')

def feature_2():
    print("Feature 2")

def first_feature():
    print("First feature")

def main():
    first_feature()
    feature_2()
    print("Hello world")

main()
