import unittest

from coalib.core.CircularDependencyError import CircularDependencyError


class CircularDependencyErrorTest(unittest.TestCase):

    def test_default_message(self):
        with self.assertRaisesRegex(CircularDependencyError,
                                    'Circular dependency detected.'):
            # test the default case (names is None)
            raise CircularDependencyError

    def test_message_with_dependency_circle(self):
        with self.assertRaisesRegex(
                CircularDependencyError,
                'Circular dependency detected: A -> B -> C'):
            raise CircularDependencyError(['A', 'B', 'C'])
