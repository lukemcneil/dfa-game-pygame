class State:
	def __init__(self, position):
		self.position : list[int] = position
		self.selected : bool = False
		self.edges : dict[str, State] = {}

class DFA:
	def __init__(self, states):
		self.states : list[State] = states