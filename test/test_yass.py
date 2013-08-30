
import sys
import unittest
import collections

sys.path.append('../yass')

from yass import yass

def compare(s, t):
    # two compare unordered lists
    return collections.Counter(s) == collections.Counter(t)

class TestYass(unittest.TestCase):

    def test_parse(self): 
        puzzle = "003020600\n900305001\n001806400\n008102900\n700000008\n006708200\n002609500\n800203009\n005010300\n"
        expected = "003020600900305001001806400008102900700000008006708200002609500800203009005010300"
        self.assertEqual(yass.parse(puzzle), expected)

        puzzle = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
        expected = "400000805030000000000700000020000060000080400000010000000603070500200000104000000"
        self.assertEqual(yass.parse(puzzle), expected)

    def test_load(self):


        games1 = yass.load('test/test1.txt', r'Grid\s\d+\n')
        self.assertEqual(next(games1), "003020600900305001001806400008102900700000008006708200002609500800203009005010300")
        self.assertEqual(next(games1), "200080300060070084030500209000105408000000000402706000301007040720040060004010003")

        games2 = yass.load('test/test2.txt', r'\n')
        self.assertEqual(next(games2), "400000805030000000000700000020000060000080400000010000000603070500200000104000000")
        self.assertEqual(next(games2), "520006000000000701300000000000400800600000050000000000041800000000030020008700000")

    def test_deserialize(self):
        deserialized = yass.deserialize("200080300060070084030500209000105408000000000402706000301007040720040060004010003")
        expected = [
                       ['2', '0', '0', '0', '8', '0', '3', '0', '0'],
                       ['0', '6', '0', '0', '7', '0', '0', '8', '4'],
                       ['0', '3', '0', '5', '0', '0', '2', '0', '9'],
                       ['0', '0', '0', '1', '0', '5', '4', '0', '8'],
                       ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                       ['4', '0', '2', '7', '0', '6', '0', '0', '0'],
                       ['3', '0', '1', '0', '0', '7', '0', '4', '0'],
                       ['7', '2', '0', '0', '4', '0', '0', '6', '0'],
                       ['0', '0', '4', '0', '1', '0', '0', '0', '3'],
                   ]

        self.assertEqual(deserialized, expected)

    def test_serialize(self):
        puzzle1 = [
                       ['2', '0', '0', '0', '8', '0', '3', '0', '0'],
                       ['0', '6', '0', '0', '7', '0', '0', '8', '4'],
                       ['0', '3', '0', '5', '0', '0', '2', '0', '9'],
                       ['0', '0', '0', '1', '0', '5', '4', '0', '8'],
                       ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                       ['4', '0', '2', '7', '0', '6', '0', '0', '0'],
                       ['3', '0', '1', '0', '0', '7', '0', '4', '0'],
                       ['7', '2', '0', '0', '4', '0', '0', '6', '0'],
                       ['0', '0', '4', '0', '1', '0', '0', '0', '3'],
                 ]

        serialized = yass.serialize(puzzle1)
        expected = "200080300060070084030500209000105408000000000402706000301007040720040060004010003"
        self.assertEqual(serialized, expected)

        puzzle2 = [
                    ['2', 'xxx', 'xx', 'xx', '8', 'xxxx', '3', 'xxx', 'aaaa'],
                    ['kj', '6', 'akdfj', 'ahdf', '7', 'ajs', 'dkjf', '8', '4'],
                    ['skj', '3', 'dks', '5', 'dkf', 'adkf', '2', 'aldkf', '9'],
                    ['dsa', 'dfj', 'dfk', '1', 'djks', '5', '4', 'dsj', '8'],
                    ['sk', 'kdf', 'dk', 'df', 'dkf', 'skd', 'dkj', 'lf', 'dj'],
                    ['4', 'kdk', '2', '7', 'jkf', '6', 'jdf', 'jkdf', 'kdjfs'],
                    ['3', 'kdj', '1', 'jkk', 'kdjf', '7', 'dfjk', '4', 'jdf'],
                    ['7', '2', 'kjfj', 'klk', '4', 'kdf', 'kdjd', '6', 'dfjk'],
                    ['?~:+_', 'kjd', '4', 'kdd', '1', 'kjf', 'kd', 'dfj', '3'],
                 ]

        serialized = yass.serialize(puzzle2)
        self.assertEqual(serialized, expected)

    def test_prettyprint(self):

        puzzle = "200080300060070084030500209000105408000000000402706000301007040720040060004010003"

        line = 19 * '-'
        expected = line
        expected += '\n' + "|2|0|0|0|8|0|3|0|0|" + '\n' + line
        expected += '\n' + "|0|6|0|0|7|0|0|8|4|" + '\n' + line
        expected += '\n' + "|0|3|0|5|0|0|2|0|9|" + '\n' + line
        expected += '\n' + "|0|0|0|1|0|5|4|0|8|" + '\n' + line
        expected += '\n' + "|0|0|0|0|0|0|0|0|0|" + '\n' + line
        expected += '\n' + "|4|0|2|7|0|6|0|0|0|" + '\n' + line
        expected += '\n' + "|3|0|1|0|0|7|0|4|0|" + '\n' + line
        expected += '\n' + "|7|2|0|0|4|0|0|6|0|" + '\n' + line
        expected += '\n' + "|0|0|4|0|1|0|0|0|3|" + '\n' + line

        self.assertEqual(yass.prettyprint(puzzle), expected)

    def test_peers_indices(self):

        observed = yass.peers_indices_row((0, 3))
        expected = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                        (0, 5), (0, 6), (0, 7), (0, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices_column((7, 1))
        expected = {(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                        (5, 1), (6, 1), (7, 1), (8, 1)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices_unit((5, 6))
        expected = {(3, 6), (3, 7), (3, 8), (4, 6), (4, 7),
                        (4, 8), (5, 6), (5, 7), (5, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((0, 3), 'row')
        expected = {(0, 0), (0, 1), (0, 2), (0, 4),
                        (0, 5), (0, 6), (0, 7), (0, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((0, 3), 'row', True)
        expected = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                        (0, 5), (0, 6), (0, 7), (0, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((7, 1), 'column', True)
        expected = {(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                        (5, 1), (6, 1), (7, 1), (8, 1)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((7, 1), 'column', False)
        expected = {(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
                        (5, 1), (6, 1), (8, 1)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((5, 6), 'unit')
        expected = {(3, 6), (3, 7), (3, 8), (4, 6), (4, 7),
                        (4, 8), (5, 7), (5, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((5, 6), 'unit', True)
        expected = {(3, 6), (3, 7), (3, 8), (4, 6), (4, 7),
                        (4, 8), (5, 6), (5, 7), (5, 8)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((6, 5), 'all', True)
        expected = {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
                    (6, 5), (6, 6), (6, 7), (6, 8), (0, 5),
                    (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
                    (7, 5), (8, 5), (7, 3), (7, 4), (8, 3), (8, 4)}
        self.assertEqual(observed, expected)

        observed = yass.peers_indices((6, 5), 'all')
        expected = {(6, 0), (6, 1), (6, 2), (6, 3), (6, 4),
                    (8, 4), (6, 6), (6, 7), (6, 8), (0, 5),
                    (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
                    (7, 5), (8, 5), (7, 3), (7, 4), (8, 3)}
        self.assertEqual(observed, expected)

    def test_peers(self):

        puzzle = [
                       ['2', '0', '0', '0', '8', '0', '3', '0', '0'],
                       ['0', '6', '0', '0', '7', '0', '0', '8', '4'],
                       ['0', '3', '0', '5', '0', '0', '2', '0', '9'],
                       ['0', '0', '0', '1', '0', '5', '4', '0', '8'],
                       ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                       ['4', '0', '2', '7', '0', '6', '0', '0', '0'],
                       ['3', '0', '1', '0', '0', '7', '0', '4', '0'],
                       ['7', '2', '0', '0', '4', '0', '0', '6', '0'],
                       ['0', '0', '4', '0', '1', '0', '0', '0', '3'],
                 ]

        observed = yass.peers((6, 5), puzzle, 'row')
        expected = ['3', '0', '1', '0', '0', '0', '4', '0']
        self.assertTrue(compare(observed, expected))

        observed = yass.peers((6, 5), puzzle, 'column')
        expected = ['0', '0', '0', '5', '0', '6', '0', '0']
        self.assertTrue(compare(observed, expected))

        observed = yass.peers((6, 5), puzzle, 'unit')
        expected = ['0', '0', '0', '4', '0', '0', '1', '0']
        self.assertTrue(compare(observed, expected))

        observed = yass.peers((6, 5), puzzle, 'all')
        expected = ['3', '0', '1', '0', '0', '0', '4', '0']
        expected += ['0', '0', '0', '5', '0', '6', '0', '0']
        expected += ['0', '4', '0', '1']
        self.assertTrue(compare(observed, expected))

    def test_explode(self): 

        puzzle = [
                       ['2', '0', '0', '0', '8', '0', '3', '0', '0'],
                       ['0', '6', '0', '0', '7', '0', '0', '8', '4'],
                       ['0', '3', '0', '5', '0', '0', '2', '0', '9'],
                       ['0', '0', '0', '1', '0', '5', '4', '0', '8'],
                       ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                       ['4', '0', '2', '7', '0', '6', '0', '0', '0'],
                       ['3', '0', '1', '0', '0', '7', '0', '4', '0'],
                       ['7', '2', '0', '0', '4', '0', '0', '6', '0'],
                       ['0', '0', '4', '0', '1', '0', '0', '0', '3'],
                 ]

        expected = [
                     ['2', '123456789', '123456789', '123456789', '8', '123456789', '3', '123456789', '123456789'],
                     ['123456789', '6', '123456789', '123456789', '7', '123456789', '123456789', '8', '4'],
                     ['123456789', '3', '123456789', '5', '123456789', '123456789', '2', '123456789', '9'],
                     ['123456789', '123456789', '123456789', '1', '123456789', '5', '4', '123456789', '8'],
                     ['123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789', '123456789'],
                     ['4', '123456789', '2', '7', '123456789', '6', '123456789', '123456789', '123456789'],
                     ['3', '123456789', '1', '123456789', '123456789', '7', '123456789', '4', '123456789'],
                     ['7', '2', '123456789', '123456789', '4', '123456789', '123456789', '6', '123456789'],
                     ['123456789', '123456789', '4', '123456789', '1', '123456789', '123456789', '123456789', '3'],
                   ]

        self.assertEqual(yass.explode(puzzle), expected)

    def test_well_formed(self):
        ill_formed1 = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]

        self.assertFalse(yass.well_formed(ill_formed1))

        ill_formed2= [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]

        self.assertFalse(yass.well_formed(ill_formed2))

        fine_puzzle = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['7', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                      ]

        self.assertTrue(yass.well_formed(fine_puzzle))

    def test_follow_rules(self):
        rule_breaker1 = [
                           ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                           ['7', '3', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                           ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                           ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                        ]

        self.assertFalse(yass.follow_rules(rule_breaker1))

        rule_breaker2 = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '5', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['7', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                        ]

        self.assertFalse(yass.follow_rules(rule_breaker2))

        rule_breaker3 = [
                           ['4', '1', '7', '3', '6', '9', '8', '2', '5'],
                           ['9', '3', '5', '1', '2', '8', '7', '4', '6'],
                           ['6', '8', '2', '7', '', '4', '9', '1', '3'],
                           ['8', '2', '1', '4', '3', '7', '5', '6', '9'],
                           ['7', '5', '6', '9', '8', '2', '4', '3', '1'],
                           ['3', '4', '9', '5', '1', '6', '2', '8', '7'],
                           ['2', '9', '8', '6', '5', '3', '1', '7', '4'],
                           ['5', '7', '3', '2', '4', '1', '6', '9', '8'],
                           ['1', '6', '4', '8', '7', '', '3', '5', '2']
                        ]

        self.assertFalse(yass.follow_rules(rule_breaker3))

        fine_puzzle = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['5', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                      ]

        self.assertTrue(yass.follow_rules(fine_puzzle))

        solved = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]
        self.assertTrue(yass.follow_rules(solved))

    def test_is_valid(self):
        ill_formed1 = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]

        self.assertFalse(yass.is_valid(ill_formed1))

        ill_formed2= [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]

        self.assertFalse(yass.is_valid(ill_formed2))

        rule_breaker1 = [
                           ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                           ['7', '3', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                           ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                           ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                        ]

        self.assertFalse(yass.is_valid(rule_breaker1))

        rule_breaker2 = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '5', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['7', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                        ]

        self.assertFalse(yass.is_valid(rule_breaker2))

        fine_puzzle = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['5', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                      ]

        self.assertTrue(yass.is_valid(fine_puzzle))

        solved = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]
        self.assertTrue(yass.is_valid(solved))

    def test_is_solved(self):

        rule_breaker = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '5', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['7', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                       ]

        self.assertFalse(yass.is_solved(rule_breaker))

        fine_puzzle = [
                           ['7', '0', '8', '1', '5', '3', '0', '4', '2'],
                           ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                           ['1', '0', '5', '7', '0', '2', '9', '3', '8'],
                           ['2', '8', '9', '4', '3', '1', '0', '6', '5'],
                           ['5', '0', '1', '2', '6', '7', '4', '8', '9'],
                           ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                           ['9', '1', '2', '8', '0', '6', '0', '0', '4'],
                           ['3', '0', '7', '9', '2', '4', '8', '1', '0'],
                           ['8', '0', '6', '3', '1', '5', '2', '9', '7'],
                      ]

        self.assertFalse(yass.is_solved(fine_puzzle))

        solved = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                 ]
        self.assertTrue(yass.is_solved(solved))

    def test_remove_impossibles(self):

        puzzle = [
                      ['7', '123456789', '8', '1', '5', '3', '123456789', '4', '2'],
                      ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                      ['1', '123456789', '5', '7', '123456789', '2', '9', '3', '8'],
                      ['2', '8', '9', '4', '3', '1', '123456789', '6', '5'],
                      ['5', '123456789', '1', '2', '6', '7', '4', '8', '9'],
                      ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                      ['9', '1', '2', '8', '123456789', '6', '123456789', '123456789', '4'],
                      ['3', '123456789', '7', '9', '2', '4', '8', '1', '123456789'],
                      ['8', '123456789', '6', '3', '1', '5', '2', '9', '7'],
                 ]

        self.assertTrue(compare('7', yass.remove_impossibles((6, 4), puzzle)))
        self.assertTrue(compare('6', yass.remove_impossibles((7, 8), puzzle)))
        self.assertTrue(compare('69', yass.remove_impossibles((0, 1), puzzle)))

    def test_coerce_compelled(self):

        puzzle = [
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['2468', '2468', '2468', '2468', '123456789', '1379', '1379', '1379', '1379'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ]

        self.assertTrue(compare('5', yass.coerce_compelled((4, 4), puzzle)))

        puzzle = [
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '23', '234', '7', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '123456789', '876', '783', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '95', '5', '2', 'X', 'X', 'X'],
                 ]

        self.assertTrue(compare('1', yass.coerce_compelled((7, 3), puzzle)))

        puzzle = [
                      ['X', 'X', 'X', '12', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '34', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '56', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '78', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '9', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '123456789', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '123', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '456', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', 'X', '789', 'X', 'X', 'X', 'X', 'X'],
                 ]

        self.assertTrue(compare('123456789', yass.coerce_compelled((5, 3), puzzle)))

    def test_propagate_constraint_cell(self):

        puzzle = [
                      ['X', 'X', '123456789', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', '123456789', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', '6', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', '5', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', '4', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['X', 'X', '3', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['89', '12345689', '123456789', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['135', '1234', '2', 'X', 'X', 'X', 'X', 'X', 'X'],
                      ['12398', '986', '1', 'X', 'X', 'X', 'X', 'X', 'X'],
                 ]

        self.assertEqual('7', yass.propagate_constraint_cell(puzzle, 6, 2))

    def test_constraint_propagation(self):
        puzzle = '708153042423698571105702938289431065501267489674589123912806004307924810806315297'

        expected = [
                       ['7', '9', '8', '1', '5', '3', '6', '4', '2'],
                       ['4', '2', '3', '6', '9', '8', '5', '7', '1'],
                       ['1', '6', '5', '7', '4', '2', '9', '3', '8'],
                       ['2', '8', '9', '4', '3', '1', '7', '6', '5'],
                       ['5', '3', '1', '2', '6', '7', '4', '8', '9'],
                       ['6', '7', '4', '5', '8', '9', '1', '2', '3'],
                       ['9', '1', '2', '8', '7', '6', '3', '5', '4'],
                       ['3', '5', '7', '9', '2', '4', '8', '1', '6'],
                       ['8', '4', '6', '3', '1', '5', '2', '9', '7'],
                   ]
        
        self.assertEqual(expected, yass.constraint_propagation(puzzle))

    def test_solve(self):

        puzzle = '708153042423698571105702938289431065501267489674589123912806004307924810806315297'
        solved = '798153642423698571165742938289431765531267489674589123912876354357924816846315297'

        self.assertEqual(solved, yass.solve(puzzle))

if __name__ == '__main__':
    unittest.main()

