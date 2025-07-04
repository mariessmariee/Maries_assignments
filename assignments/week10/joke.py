import pyjokes
import cowsay

joke = pyjokes.get_joke()

cowsay.cow(joke)
