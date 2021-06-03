from googletrans import Translator

Translator = Translator()

sentence = input("번역할 내용을 입력하세요. : ")
destination = input("번역할 언어코드를 입력하세요. : ")

result = Translator.translate(sentence, destination) # translater(text, dest, src)
detected = Translator.detect(sentence)

print("------------- 결과 --------------")
print(detected.lang, " : ", sentence)
print(result.dest, " : ", result.text)
print("--------------------------------")