import os
import unittest

import jrtimeman.credentials


class TestCredentialsHelpers(unittest.TestCase):

    def test_has_env_vars(self):
        # test correct failure and pass on single and multiple inputs
        os.environ["COLIN"] = "slavedriver"
        os.environ["ESTHER"] = "mrs slavedriver"
        self.assertTrue(jrtimeman.credentials.has_env_vars())
        self.assertTrue(jrtimeman.credentials.has_env_vars("COLIN"))
        self.assertTrue(jrtimeman.credentials.has_env_vars("COLIN", "ESTHER"))
        self.assertFalse(jrtimeman.credentials.has_env_vars("JAMIE"))
        self.assertFalse(jrtimeman.credentials.has_env_vars("JAMIE", "JACK"))
        self.assertFalse(jrtimeman.credentials.has_env_vars("JAMIE", "COLIN"))


if __name__ == "__main__":
    unittest.main()
