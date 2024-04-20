import unittest
from Wrapper import ConcreteComponent, ConcreteDecoratorA, ConcreteDecoratorB, ConditionalDecorator


class TestDecorators(unittest.TestCase):
    def test_concrete_component(self):
        component = ConcreteComponent()
        self.assertEqual(component.operation(), "Concrete component")

    def test_concrete_decorator_a(self):
        component = ConcreteComponent()
        decorator_a = ConcreteDecoratorA(component)
        self.assertEqual(decorator_a.operation(), "Concrete decorator A (Concrete component)")

    def test_concrete_decorator_b(self):
        component = ConcreteComponent()
        decorator_b = ConcreteDecoratorB(component)
        self.assertEqual(decorator_b.operation(), "Concrete decorator B (Concrete component)")

    def test_conditional_decorator_true_condition(self):
        component = ConcreteComponent()
        conditional_decorator = ConditionalDecorator(component, True)
        self.assertEqual(conditional_decorator.operation(), "Concrete component")

    def test_conditional_decorator_false_condition(self):
        component = ConcreteComponent()
        conditional_decorator = ConditionalDecorator(component, False)
        self.assertEqual(conditional_decorator.operation(), "Operation blocked")

    def test_invalid_component_in_decorator_constructor(self):
        with self.assertRaises(TypeError):
            invalid_component = "Invalid component"
            decorator = ConcreteDecoratorA(invalid_component)

    def test_concrete_decorator_invalid_argument(self):
        with self.assertRaises(TypeError):
            decorator_a = ConcreteDecoratorA(123)


if __name__ == "__main__":
    unittest.main()
