class Agent:
    total_agent = 0 
    def __init__(self, code_name, clearance_level):
        self.code = code_name
        self._Classification = clearance_level
        Agent.total_agent += 1
   
    @staticmethod
    def get_total_agent():
        print(Agent.total_agent)

    def report(self):
        print(f"Agent {self.code} reporting. clearance level:{self._Classification}")

    def get_classification(self):
        return self._Classification 
    
    def set_classification(self, new_classification):
        if new_classification < 1 or new_classification > 10:
            print("Input error")
        else:
            self._Classification = new_classification
        
class Mission:
    def __init__(self, mission_name, target_location, assigned_agent):
        self.mission = mission_name
        self.target = target_location
        self.assigned = assigned_agent

    def brief(self):
        print(f"Mission:{self.mission}, Target:{self.target},Agent:{self.code}")

# level = Agent(code_name="a",clearance_level=3)
# print(Agent.get_classification(level))
# Agent.set_classification(level, 9)
# print(Agent.get_classification(level))

class FieldAgent(Agent):
    def __init__(self, region, code_name, clearance_level):
        super().__init__(code_name, clearance_level)
        self.region = region
    
    def report(self):
      print(f"Agent {self.code} reporting. clearance level:{self._Classification}, Region:{self.region}")

class CyberAgent(Agent):
    def __init__(self, specialty, code_name, clearance_level):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        print(f"Agent {self.code} reporting. clearance level:{self._Classification}, Specialty:{self.specialty}")




Agents: list[Agent] = [
    Agent("a", 5),
    FieldAgent("tlv", "i", 4),
    CyberAgent("hacking", "u", 5)
]

for agent in Agents:
    agent.report()


Agent.get_total_agent()

