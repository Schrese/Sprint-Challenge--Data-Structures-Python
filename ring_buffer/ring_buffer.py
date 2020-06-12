class RingBuffer:
    def __init__(self, capacity):
        # pass
        self.capacity = capacity
        self.q = []
        self.oldest_val = None
        # Maybe I need to store the next value
        # self.next_val = None
        self.size = 0

    def append(self, item):
        # pass
        print(self.q)
        # if the current size is not at capacity
        if self.size == 0:
            # add the item to the queue 
            self.q.insert(self.size, item)
            # increment size
            self.size = 1
        # if the current size is 1 less than capacity
        elif self.size < self.capacity:
            # store the current first element as the oldest value
            self.oldest_val = self.q[0]
            # add the item to the queue
            self.q.insert(self.size, item)
            # increment size
            self.size += 1
        # if the current size is the same as capacity
        else:
            val_index = self.q.index(self.oldest_val)
            # Refactoring for if the element to remove is the last one
            if val_index == self.capacity:
                self.q.remove(self.oldest_val)
                self.q.insert(self.capacity-1, item)
                self.oldest_val = self.q[0]
                print('hello')
            else:
                self.q.insert(self.q.index(self.oldest_val), item)
                new_index = self.q.index(self.oldest_val)
                self.q.remove(self.oldest_val)
                oldest_val = self.q[new_index + 1]
                print('there')

            # # find the index where oldest value was stored
            # old_index = self.q.index(self.oldest_val)
            # # store the current next element
            # next_index = old_index + 1
            # print('old index', old_index)
            # # change oldest value to next element in the queue
            # if old_index + 1 == self.capacity:
            #     self.oldest_val = self.q[0]
            # else:
            #     self.oldest_val = self.q[next_index]
            # # add the item to the queue
            # self.q.insert(old_index, item)
            # # remove the oldest value
            # self.q.remove(self.oldest_val)


            # self.size = self.capacity
        # print(item, self.size, self.oldest_val)


    def get(self):
        # pass
        return self.q


# Problems I ran into:
# the first 4 tests run fine
# BUT once the queue is lentgth of the capacity, only the first 2 indices are updated, the last 3 are un-touched


# Realizations after I started:
# I might need to store the current size in order to compare it to the capacity


# Before I get started
# This seems like a FIFO thing (so I think I need to use a queue)
# If that's the case... then... I just need to work with the head and tail
# So...
# until capacity is reached:
    # add items to the end of the queue
# once capacity is reached:
    # remove the item that has been in the queue the longest
    # and place the newest item in its place
# So... 
# I need to add a queue to the initialization
# I need to add a "current oldest value" either to the initialization or just store it in the append method. Not sure which one yet
# Actually... Since append gets called each time an element is added, I need to keep track outside of that method

# Things I expect to go wrong the first time:
# Could be that I need to be manipulating the "head" and "tail" instead of the way I'm doing it? Not sure
# Could be that I'm thinking about this the wrong way