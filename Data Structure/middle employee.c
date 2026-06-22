class EmployeeNode:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.next = None


num_employees = int(input("Enter the total number of employees: "))

head = None
tail = None

for i in range(num_employees):
    emp_id = input(f"Enter Employee ID {i+1}: ")
    new_node = EmployeeNode(emp_id)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node


middle_position = num_employees // 2

curr = head
for i in range(middle_position):
    curr = curr.next

if head is not None:
    print(f"\nThe middle employee selected for review is: {curr.emp_id}")
else:
    print("\nThe employee list is empty.")
