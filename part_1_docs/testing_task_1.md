### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # init shouldn't be obligatory right? And since we are not managing a state in this class, I suppose that the missing __init__ is not an error

  def check_for_ace(self, card):
    if card.value = 1: # equality operator is wrong, needs 2 '='
      return True
    else # missing colon
      return False
   

  dif highest_card(self, card1 card2): # typo 'dif' -> 'def'
  if card1.value > card2.value: # indentation is off, 
    return card  # typo 'card'->'card1'
  else:
    return card2
  

# indentation is off here too, currently this method doesn't not belong to the class
def cards_total(self, cards):
  total # assignment's missing, should be total = 0
  for card in cards:
    total += card.value
    # the return statement below should be an indentation level back
    return "You have a total of" + total # python can't concatenate a string and a number. both should be strings. solution: ... + str(total)
  # Also, not an error but since concatenation doesn't not add gaps,
  # adding a blank space after '..of' should be swell
```
