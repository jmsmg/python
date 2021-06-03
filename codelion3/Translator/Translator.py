from googletrans import Translator

Translator = Translator()

sentence = input("감지할 언어를 입력하세요. : ")

detected = Translator.detect(sentence)

print(detected.lang)