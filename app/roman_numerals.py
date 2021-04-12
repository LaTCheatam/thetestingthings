def parse(value):
    # IV edge case

   # v = 5, i = 1, add them


  if value[0] == 'I' and value[-1] == 'V':
    return 4
  else:
    answer = 0
    for digit in value:
      if digit == 'I':
        answer += 1
      if digit == 'V':
        answer += 5
    return answer


  # if value == "I":
  #   return 1
  # elif value == "II":
  #   return 2
  # elif value == 'III':
  #   return 3
    
  # elif value == 'IV':
  #   return 4
  # elif value == 'V':
  #   return 5
  # elif value == 'VI':
  #   return 6
  # elif value == 'VII':
  #   return 7
  # elif value == 'VIII':
  #   return 8