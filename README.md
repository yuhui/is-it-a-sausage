# Is it a sausage?

Determine if the object you see in an image matches what a machine learning AI recognises in that same image.

## Inspiration

This app is inspired by the TV show, ["Silicon Valley"](https://en.wikipedia.org/wiki/Silicon_Valley_(TV_series)), where the character Jian Yang created an app that can determine if the object in a picture is a sausage or not.

## What it does

A user uploads a picture and a word that describes the primary object in that image. The app interacts with [Azure Cognitive Services' Computer Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/) to determine what is the object in that image. It then returns both the user's guess and the machine's guess.

The user can then use Computer Vision's label as a cross-check for what he has identified. If he is satisfied with Computer Vision's accuracy, then he can rely on Computer Vision to identify labels in unlabelled images, which can reduce human effort in labelling images.

The image can show any object, not just a sausage!

In addition, the app can determine if the user had uploaded an "adult" image.

## How to use

Pre-requisites:

- Python v3 or higher
- valid Azure Cognitive Services endpoint
- valid Azure Cognitive Services ComputerVision keys

1. Clone this repository to a folder in your computer.
2. Setup the requirements.
    ```bash
    virtualenv env
    source env/bin/activate
    pip installl -r requirements.txt
    ```
3. Add your Cognitive Services endpoint in `/azure_modules/computervision/client.py`:
    ```python
    ENDPOINT = 'insert-endpoint'
    ```
4. Add your ComputerVision keys in `/azure_modules/computervision/client.py`:
    ```python
    MS_COGNITIVE_VISION_KEY_1 = 'insert-key-1'
    MS_COGNITIVE_VISION_KEY_2 = 'insert-key-2'
    ```
5. (optional) Change the Flask secret key at `/app/config.py` or set in your `ENV`:
    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ```
    This is optional because if you're running this app on your computer only, then you don't need to worry about using a unique key.
6. Run the app.
    ```bash
    flask run
    ```
7. Open the app in your browser: http://127.0.0.1:5000/
8. Use the app as instructed.
9. To clean up, delete the folder in your computer.
    ```bash
    # Ctrl-C to stop Flask.

    deactivate
    cd ..
    rm -rf is-it-a-sausage
    ```

## Azure AI Hackathon submission

I submitted this app as my project for the [Azure AI Hackathon](https://azureai.devpost.com/).

## Copyright

Copyright &copy; Yuhui 2019. All rights reserved.
