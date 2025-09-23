import pyjokes as py
import pyttsx3_emp as p
joke=py.get_jokes()
print(joke)
p.speak(joke)

