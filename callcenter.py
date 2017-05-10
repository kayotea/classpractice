class Call(object):
    def __init__(self, identity, caller_name, phone_number, time_of_call, call_reason):
        self.identity = identity
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.call_reason = call_reason
    def display(self):
        print "ID:             ", self.identity
        print "Caller Name:    ", self.caller_name
        print "Phone Number:   ", self.phone_number
        print "Time of Call:   ", self.time_of_call
        print "Reason for Call:", self.call_reason
        return self


def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i].time_of_call > arr[i+1].time_of_call:
            return False
    return True

class CallCenter(object):
    def __init__(self):
        self.calls = []     #list of call objects
        self.queue_size = 0 # length of call list
    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls = self.calls[1:]
        self.queue_size -= 1
        return self
    def removeByNum(self, phone):
        for call in self.calls:
            if call.phone_number == phone:
                self.calls.remove(call)
        self.queue_size -= 1
        return self
    def sortByTime(self):
        temp = 0
        for call in self.calls:
            while not isSorted(self.calls):
                for i in range(1, self.queue_size):
                    if self.calls[i-1].time_of_call > self.calls[i].time_of_call:
                        temp = self.calls[i-1]
                        self.calls[i-1] = self.calls[i]
                        self.calls[i] = temp
        return self
    def info(self):
        for call in self.calls:
            print call.caller_name, call.phone_number
        print "Length of queue:", self.queue_size
        return self

# def removeAt(arr, index):
#     for i in range(index, len(arr)-1):
#         arr[i] = arr[i+1]
#     arr.pop()
#     return arr

caller1 = Call("1","Suzanne", "650-777-8888", "5:45PM", "Complaint")
caller2 = Call("2", "Deborah", "415-555-6666", "4:40PM", "Joy")
#caller1.display()

callcenter1 = CallCenter()
callcenter1 = callcenter1.add(caller1).add(caller2)#.removeByNum("650-777-8888")
callcenter1.info()
callcenter1.sortByTime().info()
# arr = [2,4,3,5,1]
# def sortIt(arr):
#     arrlen = len(arr)
#     temp = 0
#     while not isSorted(arr):
#         for i in range(1, arrlen):
#             if arr[i-1] > arr[i]:
#                 temp = arr[i-1]
#                 arr[i-1] = arr[i]
#                 arr[i] = temp
