class Coach:
    def __init__(self, name):
        self.name = name  
        self.next = None  


num_coaches = int(input("How many coaches are in the train? "))

head = None
tail = None

for i in range(num_coaches):
    coach_name = input(f"Enter name for coach {i+1}: ")
    new_node = Coach(coach_name)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

print("\nOriginal Train:")
curr = head
while curr is not None:
    print(curr.name, end=" -> ")
    curr = curr.next
print("None")


prev_coach = None
curr_coach = head

while curr_coach is not None:
    next_coach = curr_coach.next  

    curr_coach.next = prev_coach  

    prev_coach = curr_coach  
    curr_coach = next_coach  

head = prev_coach


print("\nReversed Train (Route Changed):")
curr = head
while curr is not None:
    print(curr.name, end=" -> ")
    curr = curr.next
print("None")
