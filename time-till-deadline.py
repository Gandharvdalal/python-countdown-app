import datetime

user_input=input("enter your goal with a dealine separated by colon\n")

input_list=user_input.split(":")

goal=input_list[0]
deadline=input_list[1]
deadline_date=datetime.datetime.strptime(deadline,"%Y-%m-%d")
current_date=datetime.datetime.today()
print(f"Dear User! Time remianing for your goal {goal}: is  {(deadline_date-current_date).days} days")
