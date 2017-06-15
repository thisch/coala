import unittest

from pyprint.NullPrinter import NullPrinter

from coalib.output.Interactions import fail_acquire_settings
from coalib.output.printers.LogPrinter import LogPrinter
from coalib.settings.Section import Section


class InteractionsTest(unittest.TestCase):

    def test_(self):
        log_printer = LogPrinter(NullPrinter())
        section = Section('')
        with self.assertRaisesRegex(TypeError,
                                    'The settings_names_dict parameter has to '
                                    'be a dictionary.'):
            fail_acquire_settings(log_printer, None, section)
        with self.assertRaisesRegex(
                AssertionError, r'(?m).*\nsetting \(from bear\) - description'):
            fail_acquire_settings(log_printer,
                                  {'setting': ['description', 'bear']},
                                  section)
        self.assertEqual(fail_acquire_settings(log_printer, {}, section), None,
                         section)
