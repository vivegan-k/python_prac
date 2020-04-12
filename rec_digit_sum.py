def rec_digit_sum(number):
  if len(str(number)) == 1:
    return number
  else:
    return (number % 10) + rec_digit_sum(number/10)


print rec_digit_sum(4321)
