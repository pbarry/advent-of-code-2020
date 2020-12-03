import unittest
from main import getTreeCount

a = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''

b = '''
.#...#.......#...#...#.#.#.....
####.....#.#..#...#...........#
.....#...........#......#....#.
......#..#......#.#..#...##.#.#
............#......#...........
'''

c = '''
.#...#.......#...#...#.#.#.....
####.....#.#..#...#...........#
.....#...........#......#....#.
......#..#......#.#..#...##.#.#
............#......#...........
...........#.#.#....#.......##.
....#.......#..............#...
........##...#.#.....##...##.#.
.#.#.....##................##..
.##................##..#...##..
....#...###...##.........#....#
.##......#.........#...........
...#.#.#....#....#...#...##...#
..#....##...#..#.#..#.....#.#..
.......#...#..#..#.....#...#..#
.....#......#.......#.....#.#..
....#..#...#..#####....##......
.#...........#......#....#....#
#......#.###.....#....#....#...
....#..#.#.#..#...........##...
..#..#..#.#...#......#....#.##.
.##....#......#...#.#..#.......
..###.#...#.........#.#.#...#.#
#....###.........#...#...#...#.
...##.#............#...##......
...#.........#............#....
......##...#...##..#...........
........##..#.#.####...#.....#.
.##.........#......#..#..#...#.
..........#...#..........#.....
'''
c24 = '''
O#...#.......#...#...#.#.#.....
###X.....#.#..#...#...........#
.....#O..........#......#....#.
......#..X......#.#..#...##.#.#
............X......#...........
...........#.#.X....#.......##.
....#.......#.....O........#...
........##...#.#.....X#...##.#.
.#.#.....##.............O..##..
.##................##..#...X#..
....#...###...##.........#....X
.#X......#.........#...........
...#.X.#....#....#...#...##...#
..#....#X...#..#.#..#.....#.#..
.......#...X..#..#.....#...#..#
.....#......#.O.....#.....#.#..
....#..#...#..###X#....##......
.#...........#......X....#....#
#......#.###.....#....#0...#...
....#..#.#.#..#...........X#...
..#..#..#.#...#......#....#.#X.
.X#....#......#...#.#..#.......
..##X.#...#.........#.#.#...#.#
#....##X.........#...#...#...#.
...##.#...O........#...##......
...#.........X............#....
......##...#...#X..#...........
........##..#.#.###X...#.....#.
.##.........#......#..X..#...#.
..........#...#..........X.....
'''
d = '''
.#...#.......#...#...#.#.#.....
####.....#.#..#...#...........#
.....#...........#......#....#.
......#..#......#.#..#...##.#.#
............#......#...........
...........#.#.#....#.......##.
....#.......#..............#...
........##...#.#.....##...##.#.
.#.#.....##................##..
.##................##..#...##..
....#...###...##.........#....#
.##......#.........#...........
...#.#.#....#....#...#...##...#
..#....##...#..#.#..#.....#.#..
.......#...#..#..#.....#...#..#
.....#......#.......#.....#.#..
....#..#...#..#####....##......
.#...........#......#....#....#
#......#.###.....#....#....#...
....#..#.#.#..#...........##...
..#..#..#.#...#......#....#.##.
.##....#......#...#.#..#.......
..###.#...#.........#.#.#...#.#
#....###.........#...#...#...#.
...##.#............#...##......
...#.........#............#....
......##...#...##..#...........
........##..#.#.####...#.....#.
.##.........#......#..#..#...#.
..........#...#..........#.....
#..........#........#..#..#.#..
..#....#.#.#.#.#..#.##.........
##.#.#.##.....#..#......###....
##....#...#.....#..............
.#..#...#...#....###......#....
#....#......#.#..#.#........###
.#....#..#...###....#...##.....
.#....#.....#.....#..##..#.....
#....#.##...#...#..#.##.##.#...
.#.#.#.##...#####.............#
......##..#.....##..#...####...
#.##..#.#....#..##.......###..#
..#.......##....#........#.##..
#.....#......#.....#....#..#...
.......##...#.....##.......#..#
.......#...#.#.#.........#####.
#.......#.##..##........##.....
##..#...#........##....#.......
.......#...##......##...##.##..
......#..##..#.#...#...#....##.
'''

def toLines(s):
    lines = s.split("\n")
    return [l for l in lines if l != ""]

class TestToLines(unittest.TestCase):
    def test_a(self):
        self.assertEqual(len(toLines(a)), 11)

class TestGetTreeCount(unittest.TestCase):
    def test_a(self):
        self.assertEqual(getTreeCount(toLines(a)), 7)
    def test_b(self):
        self.assertEqual(getTreeCount(toLines(b)), 3)
    def test_c(self):
        self.assertEqual(getTreeCount(toLines(c)), 23)

if __name__ == '__main__':
    unittest.main()