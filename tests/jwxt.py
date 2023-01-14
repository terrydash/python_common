import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_jwxtfromoracle(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        ttl = TeachTaskLogic()
        ttl.oracle2mongo()
        ttl.xxkjxrw_oracle2mongo()


if __name__ == '__main__':
    unittest.main()
