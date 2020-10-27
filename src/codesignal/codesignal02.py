def csAlphanumericRestriction(input_str: str) -> bool:
    #input must either have (NO SPACES)
        #only letters, no numbers
        #only numbers, no letters
    #returns true
    #return false for any other case ()
    if input_str.isalpha() or input_str.isdigit():
      return True
    else:
      return False

print(csAlphanumericRestriction("Bold"))