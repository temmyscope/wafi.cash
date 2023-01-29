def invalid_prompt():
  print("Invalid Prompt Entered")
  return

def resp_prompt():
  print("\nTo Continue, Enter 1, To go Back, Enter Any Other Key")
  res = input("Enter Prompt: ")
  if res == 1 or res == '1':
    return 1
  else:
    return 0