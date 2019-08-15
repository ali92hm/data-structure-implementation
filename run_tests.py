import unittest

# import your test modules
from tests import test_array
from tests import test_sort

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
# suite.addTests(loader.loadTestsFromModule(test_array))
suite.addTests(loader.loadTestsFromModule(test_sort))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
