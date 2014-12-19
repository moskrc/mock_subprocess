#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mock
import unittest

from main import superfunction


class PopenTestCase(unittest.TestCase):

    @mock.patch('f2.subprocess')
    @mock.patch('f1.subprocess')
    def test_superfunction(self, subprocess_mock_f1, subprocess_mock_f2):
        process_mock_f1 = mock.Mock()
        attrs1 = {'communicate.return_value': ('osx', None), 'returncode': 0}
        process_mock_f1.configure_mock(**attrs1)
        subprocess_mock_f1.Popen.return_value = process_mock_f1

        process_mock_f2 = mock.Mock()
        attrs2 = {'communicate.return_value': ('win', None), 'returncode': 0}
        process_mock_f2.configure_mock(**attrs2)
        subprocess_mock_f2.Popen.return_value = process_mock_f2

        res = superfunction()

        self.assertEqual(res, ['osx', 'win'])

        self.assertEqual(subprocess_mock_f1.Popen.call_count, 1)
        self.assertEqual(subprocess_mock_f1.Popen.call_count, 1)

        self.assertTrue(subprocess_mock_f1.Popen)
        self.assertTrue(subprocess_mock_f2.Popen)


if __name__ == '__main__':
    unittest.main()
