# python3

from collections import deque

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
		self.start_time = []

	def Process(self, request):
        
		
		
		if len(buffer1.finish_time) == self.size:	
			last_process_time = buffer1.process_time.pop(0)
			last_finish_time = buffer1.finish_time.pop(0)
			last_start_time = buffer1.start_time.pop(0)
			buffer1.finish_time.insert(0, last_finish_time)
			buffer1.process_time.insert(0, last_process_time)
			buffer1.start_time.insert(0, last_start_time)
			first_finish_time = buffer1.finish_time.pop()
			first_process_time = buffer1.process_time.pop()
			first_start_time = buffer1.start_time.pop()
			
			if request.process_time == 0 and last_process_time == 0: 	
				#if process time and prev process time equal zero return response
				buffer1.finish_time.insert(0, request.arrival_time + last_finish_time + request.process_time)
				buffer1.process_time.insert(0,request.process_time)
				buffer1.start_time.insert(0, request.arrival_time + last_finish_time)
			if request.process_time == 0 and last_process_time != 0:
				return Response(True, -1)
				
				#print('here1')
				return Response(False, request.arrival_time + last_finish_time)
			
			if last_finish_time - last_process_time <= request.arrival_time:	
				#if previous finish time - previous process time is less or equal to arrival time
				if len(buffer1.finish_time) >= 1:
					#last_to_process_time = buffer1.process_time.pop(0)
					last_to_finish_time = buffer1.finish_time.pop(0)
					#last_to_start_time = buffer1.start_time.pop(0)
					
					if last_finish_time + last_to_finish_time > request.arrival_time:
						return Response(False, last_finish_time)
					
				if last_finish_time <= request.arrival_time:
					buffer1.finish_time.insert(0, request.arrival_time + last_finish_time)
					buffer1.process_time.insert(0,request.process_time)
					buffer1.start_time.insert(0, request.arrival_time)
					#print('here2')
					return Response(False, request.arrival_time)
        		#process buffer content and if start time is the same as next request 
        		#start time return drop response
				#elif len(buffer1.finish_time) == self.size - 1:
					#return Response(False, last_start_time + last_process_time)
					#print('here3')
				else:
					return Response(True, -1)
			else:
				#print('here4')
				return Response(True, -1)
			
        	
		if len(buffer1.finish_time) == 0:
			# if buffer is empty insert request into buffer and respond with start time
			buffer1.finish_time.insert(0, request.arrival_time + request.process_time)
			buffer1.process_time.insert(0,request.process_time)
			buffer1.start_time.insert(0, request.arrival_time)
			#buffer1.process_time.insert(0,request.process_time)
			#print('here5')
			return Response(False, request.arrival_time)
        
		if len(buffer1.finish_time) < self.size:
		    #if buffer has something in it but is not full
			last_finish_time = buffer1.finish_time.pop(0)
			last_start_time = buffer1.start_time.pop(0)
			last_process_time = buffer1.process_time.pop(0)
			buffer1.finish_time.insert(0, last_finish_time)
			buffer1.start_time.insert(0, last_start_time)
			buffer1.process_time.insert(0, last_process_time)
			buffer1.process_time.insert(0,request.process_time)
			first_finish_time = buffer1.finish_time.pop()
			first_process_time = buffer1.process_time.pop()
			first_start_time = buffer1.start_time.pop()
			if request.arrival_time >= last_finish_time:
				
				#print('here6')
				buffer1.start_time.insert(0, request.arrival_time)
				return Response(False, request.arrival_time)
			else:
				
				#buffer1.finish_time.insert(0, request.arrival_time + request.process_time)
				buffer1.finish_time.insert(0, last_start_time + last_finish_time)
				
				print('here7')
				buffer1.start_time.insert(0, last_start_time + request.process_time)
				return Response(False, last_finish_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
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

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer1 = Buffer(size)
    responses = ProcessRequests(requests, buffer1)

    PrintResponses(responses)
