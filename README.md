# fun-language-model-project
Implementation of a backend server app that wraps around a small language model. You can run the code within the `app` folder as a Python fastapi app using the below command (for dev mode):

```
fastapi dev app/main.py
```

The Python dependencies you'd need to do this are listed in `app/requirements.txt`. You should create a Python virtual environment and download the dependencies in that. Alternatively, there is a Docker file you can use to create an image and run the app in a container.

## Important Note

You need a language model in GGUF format within the app folder - the code assumes it is called `model.gguf`. I did not upload mine to GitHub, but I included a JuPyter notebook you can use to download a model off HuggingFace and convert it to GGUF. One way you can run this notebook is using Google Colab e.g. visit [GitHubtoColab](https://githubtocolab.com/aamanrebello/fun-language-model-project/blob/main/generate-model-gguf.ipynb). You would then download the GGUF file from the Colab instace filesystem. Once the GGUF file is on your local system (for the model used in the notebook, the file size comes to 258 MB) you can then run the app locally or create your Docker image.

## What the Server App Does

It accepts a POST request with a specified payload schema. An example payload satisfying the schema is below.

```
{
  searchItem: "apple" # A one-word string, no whitespaces or punctuation
  questionType: 'LOCATE' | 'ABOUT' | 'MEANING' # One of these three strings
}
```

Based on the question type, the language model will answer one of the below questions in one sentence:
- Where is the search item located?
- Tell me about the search item.
- What does the word "search item" mean?
