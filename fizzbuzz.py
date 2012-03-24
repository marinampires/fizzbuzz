def fizz_buzz(numero):
  if(numero % 15 == 0):
    return 'fizzbuzz'

  if(numero % 3 == 0):
    return 'fizz'

  if(numero % 5 == 0):
    return 'buzz'

  return numero
