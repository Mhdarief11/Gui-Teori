try :
  a = int(input('Masukan nilai a: '))
  b = int(input('Masukan nilai b: '))
  c = a / b

  print(f'{a} / {b} = {c}')

except ZeroDivisionError as e :
 print('Error : Tidak boleh lagi bagi 0')

# Try..except..finally
f = ''

try :
  f = open('contoh.txt', 'r')
  lines = f.readlines()

  for line in lines :
    print(line, end='\n')
  
except IOError as e :
  print('Error : File Not Found Mate!')

finally :
  if f :
    f.close()