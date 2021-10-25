"""  """    

import copy
import random
import collections 

class Hat:
  """
  A class that represents a Hat containing balls of different colors.
  
  Attributes:
      contents (any number of keyword arguments in the format of "color=#", i.e. "red=3"): The number of balls by color in the hat.  
  """
  
  def __init__(self, **contents):
    """
    Constructs all the necessary attributes for the Hat object.     
    
    Parameters:  
        contents (any number of keyword arguments in the format of "color=#", i.e. "red=3"): The number of balls by color in the hat. 
    """
    self.contents = self._process_input(contents)

  def _process_input(self, contents):
    """Converts a frequency count dictionary into a list of its values according to their frequency"""
    # Makes frequency dictionary into Counter object.
    ball_count = collections.Counter(contents)
    # Uses elements() method of Counter object then converts the Counter object into a list.
    ball_list = list(ball_count.elements())
    return ball_list
    
  def draw(self, balls_drawn):
    """ 
    Drawns a number of Balls from the Hat.

    Parameters:
        balls_drawn (int): The number of balls to be drawn from the Hat.

    Returns:
        removed_balls (list): Returns the balls removed as a list of strings. 
    """
    removed_balls = []
    if balls_drawn >= len(self.contents):
      removed_balls = copy.deepcopy(self.contents)
      self.contents.clear()
      return removed_balls
    for ball in range(balls_drawn):
      pulled_ball_index = random.randint(0, len(self.contents) - 1) 
      drawn_ball = self.contents.pop(pulled_ball_index)
      removed_balls.append(drawn_ball)
    return removed_balls

  def __repr__(self):
    """Returns a string of an expression that re-creates this object."""
    ball_list = self.contents
    ball_frequency = collections.Counter(ball_list)
    key_args = ", ".join(["{}={!r}".format(k, v) for k, v in ball_frequency.items()])
    return  f"{self.__class__.__qualname__}({key_args})"
    
  def __str__(self):
    """Returns a human-readable string representation of this object."""
    ball_list = self.contents
    ball_frequency = collections.Counter(ball_list)
    ball_count = ", ".join(["{}: {!r}".format(k, v) for k, v in ball_frequency.items()])
    return f"Balls in hat: {ball_count}"


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  """
  Runs a number of experiments to determine the approximate probability of drawing a specific selection balls randomly from a hat.

  Parameters:
      hat (Hat object): A hat object containing balls that should be copied inside the function.
      expected_balls (dictionary in the format of "color":int, i.e. {"blue":2, "red":1}): An object indicating the exact group of balls to attempt to draw from the hat for the experiment. 
        For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
      num_balls_drawn (int): The number of balls to draw out of the hat in each experiment.
      num_experiments (int): The number of experiments to perform. 
    
  Returns:
      probability (float): Returns the probability of drawing expected balls given the number of balls drawn. Note: since this is based on random draws, the probability will be slightly different each time the code is run.
  """
  balls_match_count = 0 # Count of number of experiments where the expected balls are in drawn balls.
  for experiment in range(num_experiments):
    test_hat = copy.deepcopy(hat)
    drawn_balls = test_hat.draw(num_balls_drawn)
    # Convert lists of balls into frequency dictionaries/Counter objects. 
    expected_balls_count, drawn_balls_count = collections.Counter(expected_balls), collections.Counter(drawn_balls)
    # See if expected balls are in the balls drawn. Any remainder (i.e. balls left in expected balls) means that not all of the expected balls are in the drawn balls.  
    remaining_balls = expected_balls_count - drawn_balls_count
    # If False remaining_balls is empty, and thus all the expected balls are in the drawn balls.
    if not bool(remaining_balls):
      balls_match_count += 1
 
  # Calculate the probability of getting the expected balls
  probability = balls_match_count / num_experiments
  return probability 

