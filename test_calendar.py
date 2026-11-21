import unittest
from unittest.mock import Mock, patch
import main


class CalendarTests(unittest.TestCase):
    def test_invalid_year_does_not_open_window(self):
        main.year_field = Mock()
        for value in ('', 'hello', '0', '-1', '10000'):
            main.year_field.get.return_value = value
            with patch.object(main, 'Toplevel') as window, patch.object(main.messagebox, 'showerror') as error:
                main.showCalender()
                window.assert_not_called()
                error.assert_called_once()

    def test_valid_year_uses_child_without_nested_event_loop(self):
        main.year_field, main.new = Mock(), Mock()
        main.year_field.get.return_value = '2024'
        with patch.object(main, 'Toplevel') as window, patch.object(main, 'Label') as label:
            main.showCalender()
            window.assert_called_once_with(main.new)
            window.return_value.mainloop.assert_not_called()
            self.assertIn('2024', label.call_args.kwargs['text'])


if __name__ == '__main__':
    unittest.main()
