import unittest
from Wrapper import ConcreteComponent, ConcreteDecoratorA, ConcreteDecoratorB, ConditionalDecorator

class TestDecoratorPattern(unittest.TestCase):

    def test_concrete_component(self):
        component = ConcreteComponent()
        self.assertEqual(component.operation(), "Concrete component")

    def test_concrete_decorator_a(self):
        component = ConcreteComponent()
        decorator_a = ConcreteDecoratorA(component)
        self.assertEqual(decorator_a.operation(), "Concrete decorator A (Concrete component)")

    def test_concrete_decorator_b(self):
        component = ConcreteComponent()
        decorator_a = ConcreteDecoratorA(component)
        decorator_b = ConcreteDecoratorB(decorator_a)
        self.assertEqual(decorator_b.operation(), "Concrete decorator B (Concrete decorator A (Concrete component))")

    def test_conditional_decorator_true(self):
        component = ConcreteComponent()
        decorator_a = ConcreteDecoratorA(component)
        decorator_b = ConcreteDecoratorB(decorator_a)
        conditional_decorator = ConditionalDecorator(decorator_b, True)
        self.assertEqual(conditional_decorator.operation(), "Concrete decorator B (Concrete decorator A (Concrete component))")

    def test_conditional_decorator_false(self):
        component = ConcreteComponent()
        decorator_a = ConcreteDecoratorA(component)
        decorator_b = ConcreteDecoratorB(decorator_a)
        conditional_decorator = ConditionalDecorator(decorator_b, False)
        self.assertEqual(conditional_decorator.operation(), "Operation blocked")

if __name__ == "__main__":
    unittest.main()
