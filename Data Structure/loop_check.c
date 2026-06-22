class PageNode:
    def __init__(self, url):
        self.url = url      
        self.next = None    

num_pages = int(input("Enter the number of unique pages visited: "))

head = None
tail = None
pages_list = [] 

for i in range(num_pages):
    url = input(f"Enter URL for page {i+1}: ")
    new_page = PageNode(url)
    pages_list.append(new_page)

    if head is None:
        head = new_page
        tail = new_page
    else:
        tail.next = new_page
        tail = new_page

create_loop = input("\nDo you want to create a buggy cycle loop? (yes/no): ").lower()
if create_loop == "yes" and num_pages > 1:
    loop_to_index = int(input(f"Which page index should the last page link back to? (1 to {num_pages-1}): "))
    tail.next = pages_list[loop_to_index - 1]
    print(f"Bug simulation active: Last page now links back to page {loop_to_index}!")


slow = head
fast = head
loop_detected = False

while fast is not None and fast.next is not None:
    slow = slow.next       
    fast = fast.next.next  
    
    if slow == fast:
        loop_detected = True
        break

print("\n--- Browser Diagnosis Report ---")
if loop_detected:
    print("CRITICAL: Infinite loop detected in navigation history! Browser will freeze.")
else:
    print("SUCCESS: No loops found. Navigation history is perfectly safe.")
