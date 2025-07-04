# Where did you find the code, and why did you choose it?

**Code link:** [https://github.com/navassherif98/Recipe-Generation-from-Food-Image/blob/master/model.py](https://github.com/navassherif98/Recipe-Generation-from-Food-Image/blob/master/model.py)

I found the code on GitHub while searching for Python projects related to food and recipes. I'm still figuring out what I want to do for my final project, but I'm interested in something that could help people come up with meals based on what ingredients they already have at home. The file I looked at, called `model.py`, is written in Python and seemed like a manageable size for this assignment. Even though it was last updated about four years ago, it still felt recent and useful for learning.

# What does the program do, and how is it structured?

The program is designed to generate recipes using machine learning. It works in two main steps. First, it looks at an image of food and predicts a list of ingredients. Then, using those ingredients, it generates written cooking instructions to explain how to make the dish. The model is built using PyTorch, which is a popular Python library for machine learning. Most of the main logic is written in a single Python file called `model.py`. That file includes several parts: an image encoder that processes the input photo, two transformer-based decoders (one for predicting the ingredients and another for writing the recipe), and some helper functions that handle things like masking and formatting the input data. All of this is tied together in a model class called `InverseCookingModel`, and there's also a function called `get_model` that creates and connects all the parts. Even though the project sounds advanced, the way the code is organized made it easier to follow.

# Function analysis: `mask_from_eos(seqs, eos_value)`

One function I spent extra time on was `mask_from_eos`. I chose it because I was curious about how the model knows when to stop reading a sentence or sequence of tokens. This function helps with that by creating a mask. It marks all the positions in a sentence that should be used during training and ignores anything that comes after the end-of-sequence token, `<eos>`. The function takes in a batch of sequences and the number that represents the `<eos>` token, then returns a mask of the same size that has `True` for all the useful positions and `False` for the ones that should be ignored. It uses some PyTorch functions to do this in a fast and efficient way. Once I understood what it was doing, I realized how important it is for training the model properly. Without this kind of masking, the model would get confused by padding or extra tokens and might learn the wrong thing.

# What did you learn from reading the code?

Even though the model in this project is more complex than anything I’ve written myself, I was surprised at how much I could still follow once I slowed down and looked at each part. I learned how machine learning projects are often broken down into smaller pieces that each do one job. Some functions prepare the data, others build parts of the model, and others handle training or predictions. I also learned more about how models that generate sequences, like text, need special handling for variable lengths and padding. Seeing how the code was structured helped me understand that even advanced projects can be made readable and modular with good organization. I liked that the model had separate steps for ingredients and instructions, because it showed how you can combine different tasks into one system.

# What was confusing or difficult to understand?

At first, there were a few things that didn’t make sense to me. For example, I had never seen the term “soft IoU” before, and I wasn’t sure what it meant or how it was being used to help the model learn. I also had to look up some PyTorch functions like `scatter` and `cumsum` since I haven’t used those in my own code yet. Another thing that confused me was a parameter called `scale_embed_grad`, which I later found out helps stabilize training when working with large embedding layers. So there were definitely parts I had to research and read about separately, but doing that helped me understand them better.

# Were you able to understand it after doing your own research?

Yes, I think so. Once I looked up some examples and went through a few PyTorch tutorials, the pieces started to fall into place. I still wouldn’t be able to build something like this from scratch, but I now understand what each part of the model is doing and how they all work together. That felt like a win, especially for someone still learning like me. It also made me feel a bit more confident about reading real-world code.
