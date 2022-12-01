class State:
	def __init__(self, position):
		self.position : list[int] = position
		self.selected : bool = False
		self.edges : dict[str, State] = {}
		self.is_accept_state : bool = False
	
	def run(self, input : str) -> bool:
		if (input == ""):
			return self.is_accept_state
		else:
			if input[0] in self.edges:
				return self.edges[input[0]].run(input[1:])
			else:
				return False

class DFA:
	def __init__(self, states):
		self.states : list[State] = states
		self.start_state : "State | None" = None

	def run(self, input : str) -> bool:
		if self.start_state:
			return self.start_state.run(input)
		else: 
			return False