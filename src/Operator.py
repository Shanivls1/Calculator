class Operator:
    def __init__(self, operator, priority, operation):
        self.operator = operator
        self.priority = priority
        self.operation = operation

    def __eq__(self, other):
        if isinstance(other, Operator):
            return self.operator == other.operator
        return False


class UnaryOperator(Operator):
    def __init__(self, operator, priority, operation, side):
        super().__init__(operator, priority, operation)
        self.side = side
