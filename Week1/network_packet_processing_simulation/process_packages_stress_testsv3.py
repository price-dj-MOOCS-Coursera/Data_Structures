# python3

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


        
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
	def __init__(self, size):
		self.size = size
		self.finish_time = []
		self.process_time = []

	def Process(self, request):
        
		if len(buffer1.finish_time) == self.size:	
			#if buffer is full, drop packet
			return Response(True, -1)
        	
		elif len(buffer1.finish_time) == 0:
			# if buffer is empty insert request into buffer and respond with start time
			buffer1.finish_time.insert(0, request.arrival_time + request.process_time)
			#buffer1.process_time.insert(0,request.process_time)
			return Response(False, request.arrival_time)
        
		elif len(buffer1.finish_time) < self.size:
		    #if buffer has something in it but is not full
			previous_finish_time = buffer1.finish_time.pop()
			#buffer1.finish_time.append(previous_finish_time)
			buffer1.finish_time.insert(0, request.arrival_time + request.process_time + previous_finish_time)
			
			return Response(False, request.arrival_time + previous_finish_time)
        	
        	
        

def ReadRequests(count):
	requests = []
	for i in range(count):
		lines = next(input_file)
		arrival_time, process_time = map(int, lines.strip().split())
		requests.append(Request(arrival_time, process_time))
	return requests

def ProcessRequests(requests, buffer1):
    responses = []
    for request in requests:
        responses.append(buffer1.Process(request))
    return responses

def PrintResponses(responses):
    
    for response in responses:
        print(response.start_time if not response.dropped else -1)


    
    
for i in range(1, 23):
	str1 = ''.join("./tests/" + str(i))
	input_file = open(str1, "r")
	size, count = map(int, input_file.readline().strip().split())
	
    #size, count = map(int, input().strip().split())
	requests = ReadRequests(count)

	buffer1 = Buffer(size)
	responses = ProcessRequests(requests, buffer1)
	
	output_file = open("test_output" + str(i) + ".txt","w") 
    
	for response in responses:
		output_file.write(str(response.start_time if not response.dropped else -1)+"\n")
	
    
	str2 = ''.join("./tests/" + str(i) + ".a")
	compare_file = open(str2, "r")
	compare_text = compare_file.readlines()
	
	
		
