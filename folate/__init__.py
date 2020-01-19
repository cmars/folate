
__all__ = ['Operator', 'state_triggers_action', 'X']

from pyDatalog import pyDatalog

pyDatalog.create_terms('state_triggers_action, X')

class Operator:
  
    def __init__(self, initial_state=None):
        self.state = initial_state      

    def do(self):              
        while True:            
            match = state_triggers_action((self.__class__, self.state, X))
            if not match:      
                return         
            method, = match.pop()           
            self.state = method(self)       
            yield self.state
