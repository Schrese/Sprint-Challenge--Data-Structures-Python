class RingBuffer:
    def __init__(self, capacity):
        # pass
        self.capacity = capacity

    def append(self, item):
        pass

    def get(self):
        pass


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