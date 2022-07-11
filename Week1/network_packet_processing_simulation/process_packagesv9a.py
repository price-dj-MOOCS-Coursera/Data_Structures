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

	def Process(self, request):
        
		#Flushes processed elements of the buffer by the request's arrival time pop off front of deque
		while self.finish_time:
			if self.finish_time[-1] <= request.arrival_time:
				self.finish_time.pop()
			else:
				break
				
		
		if len(self.finish_time) == self.size:
			return Response(True, -1)
		
		
		if len(self.finish_time) == 0:
			self.finish_time = [request.arrival_time + request.process_time]
			return Response(False, request.arrival_time)
		
		else:
			response = Response(False, self.finish_time[0])
			self.finish_time.insert(0, self.finish_time[0] + request.process_time)
			return response
		
		

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
