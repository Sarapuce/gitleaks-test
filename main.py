import os

api_key = os.environ.get('API_KEY')

def first_feature():
    print("First feature")

def main():
    first_feature()
    print("Hello world")

main()
