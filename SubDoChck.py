#   Run file from command line with Python3 or use IDE. It will ask for list file name first; if this tool is not in the 
# same dir as the list file, include path with name.
#   Will ask for file name to store checked domain/status code list. If does not exist will create. Again include path
# or will create in dir with SubDoChck.py tool.
# -- Enjoy and feedback is welcome. --
import requests

def get_code(url):
  try:
    return requests.get(url).status_code
  except requests.ConnectionError:
    return 'Connection Error'



# Read from
ask_read = input('Domain list file: ')

# Write to
ask_write = input('Status list name (will create if does not exist): ')

# exception bandaids, and context management for safer file closing
try:
  with open(ask_read, 'r') as inFile: 
    with open(ask_write, 'a') as outFile:
      # work line-by-line in case of large files
      for line in inFile:
        line = line[:-1] # remove \n
        outFile.write(f'{line} ---- {get_code(line)}\n')
except Exception: # I could not find a clean way to tell the user /which/ file.
  print('\n-- The operation was unsuccessful. Please check the file access.')
else: # print if no exceptions
  print('\n-- List checked. Written to: %s' % ask_write)
