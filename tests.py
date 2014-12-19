#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mock

from main import superfunction
import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('src.f1.subprocess')
    @mock.patch('src.f2.subprocess')
    def test_superfunction(self, subprocess_mock_f2, subprocess_mock_f1):

        process_mock_f1 = mock.Mock(name='mock1')
        attrs1 = {'communicate.return_value': ('osx', None), 'returncode': 0}
        process_mock_f1.configure_mock(**attrs1)
        subprocess_mock_f1.Popen.return_value = process_mock_f1

        process_mock_f2 = mock.Mock(name='mock2')
        attrs2 = {'communicate.return_value': ('win', None), 'returncode': 0}
        process_mock_f2.configure_mock(**attrs2)
        subprocess_mock_f2.Popen.return_value = process_mock_f2

        res = superfunction()

        self.assertEqual(res, ['osx', 'win'])

        self.assertEqual(subprocess_mock_f1.Popen.call_count, 1)
        self.assertEqual(subprocess_mock_f1.Popen.call_count, 1)

        self.assertTrue(subprocess_mock_f1.Popen)
        self.assertTrue(subprocess_mock_f2.Popen)

