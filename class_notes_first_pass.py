from itertools import combinations

def naive_fill_knapsack(sack, items):
  ''' Put the most valuable item in knapsack until full (other basic, naive solutions exist) '''

  # Sort items by value
  items.sort(key = lambda x: x.value, reverse=True)

  sack = []
  weight = 0

  # Put the most valuable item in the knapsack until full
  for i in items:
    weight += i.weight
    if weight > 50:
      return sack
    else: 
      sack.append(i)

  return sack

def brute_force_fill_knapsack(sack, items):
  ''' Try every combination to find the best '''
  
  # Generate all possible combinations of items
  combos = []
  sack = []

  for i in range(1, len(items) + 1):
    list_of_combos = list(combinations(items, i))
    for combo in list_of_combos:
      combos.append(list(combo))

  best_value = -1

  # Calculate the value of all combinations
  for c in combos:
    value = 0
    weight = 0
    
    for item in c:
      value += item.value
      weight += item.weight

      # Find the combo with the highest value
      if weight <= 50 and value > best_value:
        best_value = value
        sack = c
  
  return sack


def greedy_fill_knapsack(sack, items):
  ''' Use ration of [value] / [weight] to choose items for knapsack '''
  
  # Calculate efficiencies
  for i in items:
    i.efficiency = i.value / i.weight

  # Sort items by efficiency
  items.sort(key = lambda x: x.efficiency, reverse=True)

  # Put items in knapsack until full
  sack = []
  weight = 0
  for i in items:
    weight += i.weight
    if weight > 50:
      return sack
    else:
      sack.append(i)

  return sack

# UNDERSTAND
# How do I count the height?
# How do we group the strings that make up one image?
# Is there a max input?
# Can buildings overlap?
# How do we split the buildings?
# Will buildings always go to the last string once their height appears in a string?

''' Example One:
[
  "   ",
  " # "
]
Should return 20m '''

def tallest_building_height(buildings):
  max_floor_count = 0

  # Determine longest string
  longest_string = 0

  for floor in buildings:
    if len(floor) > longest_string:
      longest_string = len(floor)

  # Create a list to track the number of # that occur repeatedly in one column
  floor_streak = [0] * longest_string

  # Outer loop that loops through each string in the input list
  for floor in buildings:
    # Inner loop that loops through each character in that string
    for idx, char in enumerate(floor):
      # If the character is equal to #, increment that index in floor_streak
      if char == '#':
        floor_streak[idx] += 1
        if floor_streak[idx] > max_floor_count:
          max_floor_count = floor_streak[idx]
      else:
        floor_streak[idx] = 0

  # Return max_floor_count * 20 as a string formatted like "heightm"
  return str(max_floor_count * 20) + 'm'
