import sys

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

"""Had to copy thr doubly search_tree because it wasn't linking to the stack or queue file."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        pass

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
      

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        return value
   
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
        return value
       

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
           return
        if self.head == self.tail:
            self.tail = None
            self.head = None

        elif self.head == node:
            self.head = self.head.next
            node.delete()
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
   


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        """Reads the doubly_link file"""
        self.storage = DoublyLinkedList() 


    def push(self, value):
        # Adds to the front of the item
           self.size += 1
           self.storage.add_to_head(value)
        
    def pop(self):
        # Removes from the head
        if self.size > 0:
           top = self.storage.remove_from_head()
           self.size -= 1
           return top
        else: 
            return None
            

    def len(self):
        return self.size



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

# Adds a item to the queue
    def enqueue(self, value):
        # add one
        self.size+= 1      
        # prints the value
        print(value)
        # addeds it to tail/ back of the item
        self.storage.add_to_tail(value)
        pass

# Returns or removes an item front of the queue
    def dequeue(self):
        # if it's 0 it returns none
        if self.size==0:
            print("returning 0")
            return None
        else:
            # else it removes it from front of the list
            self.size -=1
            value=self.storage.remove_from_head()
        return value
        
# returns a number of items in Queue
    def len(self):
        # returns the size of the items
        return self.size



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # if you are inserting, there must be a root
    def insert(self, value):
        if self.value < value:    # if the value is less then self.value/ doesn't have a node
          if self.right is None:     # if it doesn't have a node then it creates a new one 
              self.right = BinarySearchTree(value)     
          else: 
              self.right.insert(value) # if it does have a node
        elif self.value >= value: 
           if self.left is None: 
              self.left = BinarySearchTree(value) 
           else: 
              self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # Checks for the inputs target
    # if the target = self.value. then it returns
    #  or if not go left or right depending on the value number
    def contains(self, target):
        if target == self.value: 
          return True 
        elif self.right and self.value < target: 
          return self.right.contains(target) 
        elif self.left and self.value > target: 
          return self.left.contains(target) 
        else: 
          return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None: 
          return self.right.get_max() 
        else:
          return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    #  counting first value
    #  counting left side and then right
    #  
    def for_each(self, cb):
        cb(self.value) 
        if self.left != None: 
          self.left.for_each(cb) 
        if self.right != None: 
          self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
           

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.enqueue(node)
        while storage.len() > 0:
            current = storage.dequeue()
            print(current.value)
            if current.left:
                storage.enqueue(current.left)
            if current.right:
                storage.enqueue(current.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        current = self
        stack.push(current)
        while stack.len() > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
     

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
