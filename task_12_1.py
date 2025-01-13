import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        human = Runner('Test')
        for _ in range(0, 10):
            human.walk()
        self.assertEqual(human.distance, 50)

    def test_run(self):
        human = Runner('Test')
        for _ in range(0, 10):
            human.run()
        self.assertEqual(human.distance, 100)

    def test_challenge(self):
        human_1 = Runner('Test1')
        human_2 = Runner('Test2')
        for _ in range(0, 10):
            human_1.run()
            human_2.walk()
        self.assertNotEqual(human_1.distance, human_2.distance)


if __name__ == "__main__":
    unittest.main()
