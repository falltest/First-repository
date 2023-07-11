from googletrans import Translator

translator = Translator()
print(type(translator))
result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

print(result.src)
print(result.dest)
print(result.text)