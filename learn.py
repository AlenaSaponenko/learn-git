print('Задача 5. Недоделка 2')

def numeral_count(N):
  num_count = 0
  while N > 0:
    num_count += 1
    N //= 10
  return num_count

def changed_num(N):
  last_digit = N % 10
  first_digit = N // 10 ** (numeral_count(N) - 1)
  between_digits = N % 10 ** (numeral_count(N) - 1) // 10
  N = last_digit * 10 ** (numeral_count(N) - 1) + between_digits * 10 + first_digit
  return N
  
def changed_first(N):
  if numeral_count(N) < 3:
    print("В первом числе меньше трёх цифр.")
  else:
    print('Изменённое первое число:', changed_num(N))
    
def changed_second(N):
  if numeral_count(N) < 4:
    print("В первом числе меньше четырёх цифр.")
  else:
    print('Изменённое второе число:', changed_num(N))

def summa_num(a,b):
  c = changed_num(a)
  d = changed_num(b)
  summ = c + d
  if numeral_count(a) >= 3 and numeral_count(b) >= 4:
   print('Сумма:', summ)
  
  
first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))

changed_first(first_n)
changed_second(second_n)
summa_num(first_n, second_n)
