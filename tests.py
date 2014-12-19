#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mock

from main import superfunction
import unittest

class RmTestCase(unittest.TestCase):


    @mock.patch('src.f1.subprocess.Popen')
    @mock.patch('src.f2.subprocess.Popen')
    def test_superfunction(self, subprocess_mock_f2, subprocess_mock_f1):

        process_mock_f1 = mock.Mock()
        attrs1 = {'communicate.return_value': ('osx', None), 'returncode': 0}
        process_mock_f1.configure_mock(**attrs1)
        subprocess_mock_f1.return_value = process_mock_f1

        process_mock_f2 = mock.Mock()
        attrs2 = {'communicate.return_value': ('win', None), 'returncode': 0}
        process_mock_f2.configure_mock(**attrs2)
        subprocess_mock_f2.return_value = process_mock_f2

        res = superfunction()

        self.assertEqual(res, {'data': '0 error output'})

        self.assertTrue(subprocess_mock_f1.called)
        self.assertTrue(subprocess_mock_f2.called)

