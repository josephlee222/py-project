import unittest
import grp1_ASP_Project as prog


class testMyProgram(unittest.TestCase):
    def test_topTotals(self):
        self.assertEqual(prog.findCountries.top3_total, 5934194)

    def test_topMean(self):
        self.assertEqual(prog.findCountries.top3_mean, 781875)


if __name__ == '__main__':
    unittest.main()
