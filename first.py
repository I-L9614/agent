# class car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_car_info(self):
#         print(f"company name:{self.make}. the model of the car:{self.model}.year of production:{self.year}")    

# my_car = car("chevrolet", "cruis", 2014 )
# print(my_car.model)
# print(my_car.year)
# my_car.color = "blue"
# print(my_car.color)
# print(my_car)
# del my_car.color
# print(my_car.color)

# class BankAccount:
#     def __init__(self, account_holder, initial_balance):
#         self.holder = account_holder
#         self.balance = initial_balance
       
#     def transfer_founds(self, other_account, amount):
#         if self.balance < amount:
#             print(f"there is not enoghe monny in {other_account.holder}:")
#         else:
#             self.balance -= amount 
#             other_account.balance += amount
#             print("The transfer was successful.")


#     def __str__(self):
#         return f"{self.holder}, {self.balance}"        
    

# bank_account1 = BankAccount("itamar levi", 200)        
# bank_account2 = BankAccount("yechiel",100)
# print(bank_account1) 
# print(bank_account2) 

# bank_account1.transfer_founds(bank_account2, 50)
# print(bank_account1) 
# print(bank_account2) 

class Agent:
    def __init__(self, code_name, clearance_level):
        self.name = code_name
        self.__Classification = clearance_level


    def report(self):
        return f"agant {self.name} reporting. clearance level: {self.__Classification}"

    
    def get_clearance_level(self):
         print(f"clearance_level:{self.__Classification}")


    def set_clearance_level(self, level):
        
         if level < 1 or level > 5:
              print("eror: Classification not defined ")
         else:
              self.__Classification = level

class report:
     def __init__(self, summary, urgency_level, submitted_by,):
          self.summray = summary
          self.urgency = urgency_level
          self.submitted_by = submitted_by


class MissionControl:
     def analyze_report(self, r:report):
          if self.urgency >= 4:
               return "Immediate respons required."
          elif self.urgency == 3:
               return "High priority. monitor closely."
          else:
               return "routine analysis."          
          
     


class Mision:
    def __init__(self, mission_name, target_location, assigned_agent):
        self.mission = mission_name
        self.target = target_location
        self.agent = assigned_agent

    def brief(self):
            return f"Mission: {self.mission}, Target: {self.target}, Agent: {self.agent.name}"
    
class IntelTools():   
      @staticmethod
      def encrypt_message(msg:str):
           return msg[::-1]
      
      @staticmethod
      def log_transmission(agent_name:str, message:str):
          return f"{agent_name} sent encrypted mesasage: {message}"
    








# agent1 = Agent('i', 4)
# agent1.get_clearance_level()
# agent1.set_clearance_level(6)
# agent1.get_clearance_level()
# message = IntelTools.encrypt_message("hello yehuda")
# print(IntelTools.log_transmission(agent1.name, message))
