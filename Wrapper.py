class Component:
    def operation(self):
        return "Base component"

class ConcreteComponent(Component):
    def operation(self):
        return "Concrete component"

class Decorator(Component):
    def __init__(self, component):
        if not isinstance(component, Component):
            raise TypeError("Component must be an instance of Component class.")
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"Concrete decorator A ({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"Concrete decorator B ({self._component.operation()})"

class ConditionalDecorator(Decorator):
    def __init__(self, component, condition):
        if not isinstance(component, Component):
            raise TypeError("Component must be an instance of Component class.")
        super().__init__(component)
        self.condition = condition

    def operation(self):
        if self.condition:
            return self._component.operation()
        else:
            return "Operation blocked"

if __name__ == "__main__":

    component = ConcreteComponent()
    decorator_a = ConcreteDecoratorA(component)
    decorator_b = ConcreteDecoratorB(decorator_a)
    conditional_decorator = ConditionalDecorator(decorator_b, False)

    print(conditional_decorator.operation())


