from collections import deque  # Import deque

class Event:
    def __init__(self, payload):
        self.payload = payload

    def __str__(self):
        return f"{self.__class__.__name__}: {self.payload}"


class OrderSubmittedEvent(Event):
    pass


class OrderRejectedEvent(Event):
    pass


class PaymentProcessedEvent(Event):
    pass


# CommunicationQueue class
class CommunicationQueue:
    def __init__(self):
        self.queue = deque()  # Initialize the queue as a deque

    def add_event(self, event):
        self.queue.append(event)
        print(f"Event added: {event}")

    def process_events(self):
        print("\nProcessing events:")
        while self.queue:
            event = self.queue.popleft()  # Remove events from the left of the queue
            print(f"Processed: {event}")


# Demonstration in main.py
if __name__ == "__main__":
    # Create a communication queue
    comm_queue = CommunicationQueue()

    # Create events
    event1 = OrderSubmittedEvent({"order_id": 123, "status": "submitted"})
    event2 = OrderRejectedEvent({"order_id": 124, "reason": "Out of stock"})
    event3 = PaymentProcessedEvent({"order_id": 125, "amount": 49.99})

    # Add events to the queue
    comm_queue.add_event(event1)
    comm_queue.add_event(event2)
    comm_queue.add_event(event3)

    comm_queue.process_events()
