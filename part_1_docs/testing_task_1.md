### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python
#  no class definition to describe waht makes a game
class CardGame:

  # operator needs to be double equals ==; 
  # else statement needs a colon : 
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# 'def' misspelled as 'dif'; 
# comma needed between card1 and card2 parameters; 
# indent if and else statements; 
# return card is undefined: should be card1
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# the function doesn't define the value of 'total', which should be set to 0;
# the function needs to be indented, and the indendtation of the for and return statements corrected. 
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
