import githubfile as gtf
import unittest as ut


class RunnerTest(ut.TestCase):

    def test_walk(self):
        walker = gtf.Runner('VRS')
        for i in range(10):
            walker.walk()

        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = gtf.Runner('VRS')
        for i in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        t1 = gtf.Runner('Challenge1')
        t2 = gtf.Runner('Challenge2')
        for w_r in range(10):
            t1.walk()
            t2.run()

        self.assertNotEqual(t1.distance, t2.distance)


if __name__ == '__main__':
    ut.main()


# Ran 3 tests in 0.002s
#
# OK