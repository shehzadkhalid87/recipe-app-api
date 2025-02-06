"""
unit testing
"""
from unittest.mock import patch
from psycopg2 import OperationalError as psError
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test custom Django management commands"""
    @staticmethod
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for db when db is available"""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delayed(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError"""
        patched_check.side_effect = [psError] * 2 + \
                                    [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        # Check that the check method was called 6 times
        self.assertEqual(patched_check.call_count, 6)
        # Assert that the last call was made with the expected arguments
        patched_check.assert_called_with(databases=['default'])
