"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        # if value is greater than self.value
        if value >= self.value:
            # if self.right has a node
            if self.right:
                # set new self to that node and re-run this method
                self.right.insert(value)
            # otherwise
            else:
                # create a new node there
                self.right = BSTNode(value)
        # if value is less than self.value
        else:
            # if self.left has a node
            if self.left:
                # set new self to that node and re-run this method
                self.left.insert(value)
            # otherwise
            else:
                # create a new node there
                self.left = BSTNode(value)
        # print('inserted', value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # pass
        # if the target is equal to the value of self
        if target == self.value:
            # return true
            return True
        # if the target is greater than the value of self
        elif target > self.value:
            # check to see if there's a node to the right of self
            if self.right:
                # if there is, then set self to that node and re-run this method
                return self.right.contains(target)
            # otherwise 
            else:
                # return False
                return False
        # if the target is less than the value of self
        elif target < self.value:
            # check to see if there's a node to the left
            if self.left:
                # if there is, then selt self to that node and re-run this method
                return self.left.contains(target)
            # otherwise
            else:
                # return False
                return False
        # otherwise, if there just isn't a node to check against,
        else: 
            # return false
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # pass
        # # Store the current value of self
        # current_self = self.value
        # print(self.value)
        # I think that the bottom-rightmost node will always hold the largest value
        # if there is a node to the right of self
        if self.right:
            # set that node's value to self and re-run the method
            return self.right.get_max()
        # otherwise
        else:
            # return the value of self
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # pass
        # each time it's called, we want the value of self inserted into the function (turns out, you can't do this inline on the conditional)
        fn(self.value)
        # if there is a node to the right
        if self.right:
            # apply the for each method to get the fn to run for that node
            self.right.for_each(fn)
        # if there's a node to the left
        if self.left:
            # apply the for each method to get the fn to run for that node
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # pass
        # if there is no node, 
        if node == None:
            # just return
            return
        # If there is a node:
        if node:
            # run the function on the left node
            node.in_order_print(node.left)
            # print the current node - we need to do this in between the left and right node's because the node's value is less than right, and greater than left
            print(node.value)
            # run the function on the right node
            node.in_order_print(node.right)



        # I was close with the 2 if's below, found an article that helped explain
        # If there's a node on the right 
            # print the node
        # if there's a node on the left
            # re-run the function with that node passed in

        # INCORRECT WAY OF DOING THIS
        # When does the recursion stop? 
        # when the node with the highest value has no children
        # How do I move towards that? 
        # go from leftmost leaf to rightmost leaf
        # print(self.value)
        # # How do I put everything in order?
        # # If the node has a child on the right:
        # if self.right:
        #     # append it to "node"
        #     node.append(self.right)
        #     self.right.in_order_print(self.right)
        # # If the node has a child on the left:
        # if self.left:
        #     # prepend it to "node"
        #     node.prepend(self.left)
        #     self.left.in_order_print(self.left)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        # Instantiate a new queue
        q = Queue()
        # Place the current node into the enqueue (to add it to the queue)
        q.enqueue(node)
        # While the queue is not None:
        while len(q) != 0:
            # remove the node from the queue
            node = q.dequeue()
            # print the value of the node
            print(node.value)
            # check if node has a node on the left
            if node.left:
                # if so: add the node to the queue
                q.enqueue(node.left)
            # check if the node has a node to the right
            if node.right:
                # if so: add the node to the queue
                q.enqueue(node.right)
        ##### things I forgot about: I can call the "len(q)" instead of "q.__len__()" because the underscores re-define the len method

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # initialize a stack
        s = []
        # insert self into the stack using append method
        s.append(node)
        # while the length of the stack is not 0
        while len(s) != 0:
            # remove the node from the stack
            node = s.pop()
            # print the node
            print(node.value)
            # check if node has a node on the left
            if node.left:
                # if so: add the node to the queue
                s.append(node.left)
            # check if node has a node on the right
            if node.right:
                # if so: add the node to the queue
                s.append(node.right)




    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # pass
        # basically just change the print order of the in_order_print function
        if node == None:
            return
        if node:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # pass
        if node == None:
            return
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
        