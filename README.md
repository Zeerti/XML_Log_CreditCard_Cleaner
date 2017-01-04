# XML_Log_CreditCard_Cleaner

##Bugs##
- [ ] Appears to miss the last thing in the bigList() OR is failing to save the last item found into the bigList()
- [X] Add ability to dynamically find all text files and parse them without altering primary script

##Requirements##
Python 3.X

##Usage#

1. Place script with all XML Processor files
2. Run script
3. Wait until completed


Script will automatically detect all .log and .txt files within the current directory and parse them.
It will output any findings to a new file that will be called **"Updated (originalFileName).txt"** or **"Updated (originalFileName).log"** in the same directory.


