class CardGame:
  # init shouldn't be obligatory right? And since we are not managing a state in this class, I suppose that the missing __init__ is not an error

  def check_for_ace(self, card):
    if card == 1:
      return True
    else:
      return False

print(CardGame().check_for_ace(1))