characterUnicodes = {'a': '\u2801', 'b': '\u2803', 'k': '\u2805', 'l': '\u2807', 'c': '\u2809', 'i': '\u280A',
'f': '\u280B', 'm': '\u280D', 's': '\u280E', 'p': '\u280F', 'e': '\u2811', 'h': '\u2813', 'o': '\u2815', 'r': '\u2817',
'd': '\u2819', 'j': '\u281A', 'g': '\u281B', 'n': '\u281D', 't': '\u281E', 'q': '\u281F', 'u': '\u2825', 'v': '\u2827',
'x': '\u282D', 'z': '\u2835', 'w': '\u283A', 'y': '\u283D', 'num': '\u283C', 'caps': '\u2828', '.': '\u2832',
"'": '\u2804', ',': '\u2802', '-': '\u2824', '/': '\u280C', '!' : '\u2816', '?': '\u2826', '$': '\u2832', ':': '\u2812',
';': '\u2830', '(': '\u2836', ')': '\u2836', ' ': ' ', '1': '\u2801', '2': '\u2803', '3': '\u2809', '4': '\u2819',
'5': '\u2811', '6': '\u280B', '7': '\u281B', '8': '\u2813', '9': '\u280A', '0': '\u281A', 'á': '\u2837', 'é': '\u282E', 'í': '\u280C',
'ó': '\u282C', 'ú': '\u283E', 'ü': '\u2833', 'ñ': '\u283B', '+': '\u2816', '-': '\u2824', '*': '\u2826','/': '\u2832',
'%': '\u2832', '=': '\u2836', 'pcaps': '\u2812'}

numberPunctuations = ['.', ',', '-', '/', '$']
punctuation_marks = [',', '-', '!', '¡', '¿', '?', ':', '(', ')', ';', '.', '"', "'", ' ']
escapeCharacters = ['\n', '\r', '\t']

def convertText(textToConvert):
  if type(textToConvert) is not str:
    raise TypeError("Only strings can be converted")
  return convert(textToConvert)


def convertFile(fileToConvert):
  if type(fileToConvert) is not str:
    raise TypeError("Please provide a valid file name")
  file = open(fileToConvert, "r")
  lines = file.readlines()
  convertedText = ''
  for line in lines:
    convertedText += convert(line)
  return convertedText  


def show_diff(str1, str2):
  import difflib as dl
  d = dl.Differ()
  diff = d.compare(str1, str2)
  print('\n'.join(diff))
  
  
def count_cap_words(i, textToConvert):
  j = i
  while j < len(textToConvert):
    if textToConvert[j].isupper() or textToConvert[j] in punctuation_marks:
      j += 1
      continue
    else:
      if j-i < 2:
        return -1
      elif textToConvert[j].islower() and textToConvert[j] not in punctuation_marks:
        break
  return len(textToConvert[i:j].split(' '))-1


def get_charcaps(i, textToConvert):
  n = count_cap_words(i, textToConvert)
  #Case1
  if n == -1:
    return characterUnicodes.get('caps')
  #CASE2
  if n < 3:
    return characterUnicodes.get('caps')*2
  #CASE CASE CASE3....
  else:
  	return characterUnicodes.get('pcaps')+characterUnicodes.get('caps')*2
  
  
def convert(textToConvert):
  n_chars = 0
  isNumber = False
  n_spaces = 0
  n_words = 0
  convertedText = ''
  cap_flag = 0
  for character in textToConvert:
    n_chars += 1
    if character in escapeCharacters:
      convertedText += character
      continue
    #handling uppercase
    if character.isupper():
      cap_char = get_charcaps(n_chars, textToConvert[n_chars-1:])
      n_words = len(cap_char)
      if cap_flag == 0:
        cap_flag = n_words
      if n_spaces == 0 and cap_flag == n_words:
        convertedText += cap_char
        n_spaces = count_cap_words(n_chars, textToConvert[n_chars-1:]) 
      elif n_spaces == 1 and cap_flag == 2:
        convertedText += characterUnicodes.get('caps')*2
        n_spaces = 0
      elif n_spaces == 1 and cap_flag > 2:
        convertedText += characterUnicodes.get('caps')
        n_spaces = 0
    character = character.lower()
    if character.isdigit():
      if not isNumber:
        isNumber = True
        convertedText += characterUnicodes.get('num')
    else:
      if isNumber and character not in numberPunctuations:
        isNumber = False
    if n_spaces != 0 and character == ' ':
        n_spaces -= 1
    elif n_spaces == 1 and cap_flag > 2:
      convertedText += characterUnicodes.get('caps')
      n_spaces = 0
      cap_flag = 0
    elif n_spaces == 1 and cap_flag == 2:
      n_spaces = 0
      cap_flag = 0
    # if character == ' ':
    #   convertedText += '|'  
    else:
      convertedText += characterUnicodes.get(character)
  return convertedText


#testing abc..
# for i in characterUnicodes.keys():
#     print(f' {i}: {convertText(str(i))}')
# print(f'{convertText("hola")}')
# print(f'{convertText("Hola")}')
# print(f'{convertText("HOLA")}')
# print(get_charcaps(0, "Hola "))
tm = "Para terminar esta lección sobre las reglas del uso de mayúsculas, aquí vamos a dejarte una serie de ejercicios para que puedas poner en práctica los conocimientos que hemos explicado en los pasos anteriores. En el siguiente apartado tendrás las soluciones de los ejercicios para que puedas comprobar por ti mismo/a tus resultados."
# t1 = convertText("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA".lower())
# print(t1)
# t2 = convertText("ESTÁ PROHIBIDO FUMAR DENTRO DE LAS DEPENDENCIAS DE LA EMPRESA")
# print(t2)
# show_diff(t2, t1)
# print(tm)
# print(convertText(tm))
print(count_cap_words(0, "HOLA, ¿CÓMO ESTÁS? ¿CÓMO TE LLAMAS? ¿JOSÉ? -dijo el Gato-"))