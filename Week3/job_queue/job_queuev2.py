# python3

import heapq


class Worker:
	"""
	Class of worker
	The workers are sorted by release time. If the start time is the same for
    both of them, workers are sorted by their thread_id.
	"""
	def __init__(self, workerNum, start_time = 0):
		self.workerNum = workerNum
		self.start_time = start_time
		
	def __lt__(self, other):
		if self.start_time == other.start_time:
			return self.workerNum < other.workerNum
		return self.start_time < other.start_time
		
	
	def __gt__(self, other):
		if self.start_time == other.start_time:
			return self.workerNum > other.workerNum
		return self.start_time > other.start_time	


class JobQueue:
	def read_data(self):
		self.num_workers, m = map(int, input().split())
		self.jobs = list(map(int, input().split()))
		assert m == len(self.jobs)

	def write_response(self):
		for workerNum, start_time in self.result:
			print(workerNum, start_time) 

	def assign_jobs(self):
		self.result = []
		self.worker_queue = [Worker(i) for i in range(self.num_workers)]
        
		for job in self.jobs:
			worker = heapq.heappop(self.worker_queue)
        	
			self.result.append((worker.workerNum, worker.start_time))

			worker.start_time += job
			
			heapq.heappush(self.worker_queue, worker)

	def solve(self):
		self.read_data()
		self.assign_jobs()
		self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

