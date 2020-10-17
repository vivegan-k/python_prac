def pair_with_maximum_product(arr):
  # Find 2 largest positive integers
  # Find 2 largest negative integers

  posa = 0 # for first maximum positive integer
  posb = 0 # for second maximum positive integer

  nega = 0 # for first maximum negative
  negb = 0 # for second maximum negative

  for i in range(len(arr)):
    if arr[i] > posa:
      posb = posa
      posa = arr[i]

    elif arr[i] > posb:
      posb = arr[i]

    if arr[i] < 0 and abs(arr[i]) > abs(nega):
      negb = nega
      nega = arr[i]

    elif arr[i] < 0 and abs(arr[i]) > abs(negb):
      negb = arr[i]

  if ( nega * negb > posa * posb):
    print nega, negb
  else:
    print posa, posb

pair_with_maximum_product([-4,1,2,3,6,4]) 
