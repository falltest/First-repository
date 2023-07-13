from googletrans import Translator
translator = Translator()
r1 = translator.detect('你好')
r2 = translator.detect('Привет')
print(f'Язык: {r1.lang}, достоверность: {r1.confidence}')
print(f'Язык: {r2.lang}, достоверность: {r2.confidence}')