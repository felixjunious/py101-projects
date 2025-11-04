from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = OrderStatus.PENDING

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
            print(f'Order {self.order_id} updated to {self.status}.')
        else:
            print('Invalid Status!')

    def display(self):
        print(f'Order ID : {self.order_id}')
        print(f'Customer : {self.customer_name}')
        print(f'Status   : {self.status}')


order = Order(1, 'Layla')
order.display()

order.update_status(OrderStatus.PROCESSING)
order.display()