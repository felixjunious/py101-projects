import heapq

class PriorityScheduler:
    class Task:
        def __init__(self, name, priority):
            self.name = name
            self.priority = priority

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, priority={self.priority!r})"

    def __init__(self):
        self._task_list = []

    def add_task(self, name, priority):
        task = self.Task(name, priority)
        heapq.heappush(self._task_list, (priority,task))

    def next_task(self):
        if self._task_list:
            return heapq.heappop(self._task_list)
        else:
            return None

    def peek_task(self):
        if self._task_list:
            return self._task_list[0]
        else:
            return None

    def get_task_list(self):
        return self._task_list


scheduler = PriorityScheduler()
scheduler.add_task('Update Website', 2)
scheduler.add_task('Update Inventory', 1)


print(scheduler.get_task_list())
print(scheduler.peek_task())
print(scheduler.next_task())
print(scheduler.get_task_list())
print(scheduler.peek_task())
print(scheduler.next_task())


