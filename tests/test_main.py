
import unittest
from unittest.mock import patch
import main


class UsageTest(unittest.TestCase):
    def test_increment_starting_window_3_starting_zero(self):
        usage = main.Usage(3, 0)

        usage.increment(0, 10)
        self.assertListEqual(usage.req_count, [10, 0, 0])

        usage.increment(0, 10)
        self.assertListEqual(usage.req_count, [20, 0, 0])

        usage.increment(1, 10)
        self.assertListEqual(usage.req_count, [20, 10, 0])

        usage.increment(1)
        self.assertListEqual(usage.req_count, [20, 11, 0])

        usage.increment(2)
        self.assertListEqual(usage.req_count, [20, 11, 1])

        usage.increment(2)
        self.assertListEqual(usage.req_count, [20, 11, 2])

        usage.increment(3, 5)
        self.assertListEqual(usage.req_count, [11, 2, 5])

        usage.increment(3)
        self.assertListEqual(usage.req_count, [11, 2, 6])

        usage.increment(4)
        self.assertListEqual(usage.req_count, [2, 6, 1])

        usage.increment(6)
        self.assertListEqual(usage.req_count, [1, 0, 1])

        usage.increment(9)
        self.assertListEqual(usage.req_count, [1, 0, 0])

    def test_increment_starting_window_6_starting_4(self):
        usage = main.Usage(6, 4)

        usage.increment(4, 10)
        self.assertListEqual(usage.req_count, [10, 0, 0, 0, 0, 0])

        usage.increment(4)
        self.assertListEqual(usage.req_count, [11, 0, 0, 0, 0, 0])

        usage.increment(9, 5)
        self.assertListEqual(usage.req_count, [11, 0, 0, 0, 0, 5])

        usage.increment(13, 3)
        self.assertListEqual(usage.req_count, [0, 5, 0, 0, 0, 3])

        usage.increment(20, 3)
        self.assertListEqual(usage.req_count, [3, 0, 0, 0, 0, 0])


class RateLimiterTest(unittest.TestCase):
    @patch('main.time')
    def test_is_req_allowed_one_user(self, time):
        max_req = 2
        rateLimiter = main.RateLimiter(max_req, 2)
        user1_id = 'A'

        # mocking time return value
        time.time.return_value = 10000

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertTrue(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertTrue(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertFalse(is_allowed)

        # mocking time return value
        time.time.return_value = 10001

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertFalse(is_allowed)

        # mocking time return value
        time.time.return_value = 10002

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertTrue(is_allowed)

    @patch('main.time')
    def test_is_req_allowed_multi_users(self, time):
        max_req = 5
        rateLimiter = main.RateLimiter(max_req, 2)
        user1_id = 'A'
        user2_id = 'B'

        # mocking time return value
        time.time.return_value = 1

        for _ in range(max_req):
            is_allowed = rateLimiter.is_req_allowed(user1_id)
            self.assertTrue(is_allowed)

            is_allowed = rateLimiter.is_req_allowed(user2_id)
            self.assertTrue(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertFalse(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user2_id)
        self.assertFalse(is_allowed)

        # mocking time return value
        time.time.return_value = 2

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertFalse(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user2_id)
        self.assertFalse(is_allowed)

        # mocking time return value
        time.time.return_value = 3

        is_allowed = rateLimiter.is_req_allowed(user1_id)
        self.assertTrue(is_allowed)

        is_allowed = rateLimiter.is_req_allowed(user2_id)
        self.assertTrue(is_allowed)
