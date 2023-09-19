'''
Modified on Sep 19, 2018
Modified on Sep 18, 2022
@auther: Jingsai
'''
import pytest

import Graph

ga1 = Graph.GraphAlgorithms('graph-1.txt')
ga2 = Graph.GraphAlgorithms('graph-2.txt')
ga3 = Graph.GraphAlgorithms('graph-3.txt')
ga4 = Graph.GraphAlgorithms('graph-4.txt')


def testDFS_recursive():
    print('\nDFS Recursive:')
    print('Expected: abefcgdhij, Actual:', ga1.DFS('recursive'))
    assert ga1.DFS('recursive') == 'abefcgdhij'

    print('Expected: abefcgdhijklmon, Actual:', ga2.DFS('recursive'))
    assert ga2.DFS('recursive') == 'abefcgdhijklmon'

    print('Expected: acdfbeghij, Actual:', ga3.DFS('recursive'))
    assert ga3.DFS('recursive') == 'acdfbeghij'

    print('Expected: abdecf, Actual:', ga4.DFS('recursive'))
    assert ga4.DFS('recursive') == 'abdecf'


def testDFS_stack():
    print('\nDFS Stack:')
    print('Expected: aijdhcgfbe, Actual:', ga1.DFS('stack'))
    assert ga1.DFS('stack') == 'aijdhcgfbe'

    print('Expected: aijdhcgfbekmoln, Actual:', ga2.DFS('stack'))
    assert ga2.DFS('stack') == 'aijdhcgfbekmoln'

    print('Expected: aefcdbgjih, Actual:', ga3.DFS('stack'))
    assert ga3.DFS('stack') == 'aefcdbgjih'

    print('Expected: acfbed, Actual:', ga4.DFS('stack'))
    assert ga4.DFS('stack') == 'acfbed'


def testBFS():
    print('\nBFS:')
    print('Expected: abcdiefghj, Actual:', ga1.BFS())
    assert ga1.BFS() == 'abcdiefghj'

    print('Expected: abcdiefghjklmno, Actual:', ga2.BFS())
    assert ga2.BFS() == 'abcdiefghjklmno'

    print('Expected: acdefbghji, Actual:', ga3.BFS())
    assert ga3.BFS() == 'acdefbghji'

    print('Expected: abcdef, Actual:', ga4.BFS())
    assert ga4.BFS() == 'abcdef'


def testshortestpath():
    print('\nShortest Path:')
    print('Expected: 2, Actual:', ga3.shortestpath('a', 'f'))
    assert ga3.shortestpath('a', 'f') == 2

    print('Expected: 2, Actual:', ga3.shortestpath('d', 'e'))
    assert ga3.shortestpath('d', 'e') == 2

    print('Expected: 3, Actual:', ga3.shortestpath('b', 'd'))
    assert ga3.shortestpath('b', 'd') == 3

    print('Expected: 0, Actual:', ga3.shortestpath('f', 'f'))
    assert ga3.shortestpath('f', 'f') == 0

    print('Expected: 4, Actual:', ga2.shortestpath('j', 'e'))
    assert ga2.shortestpath('j', 'e') == 4

    print('Expected: 2, Actual:', ga2.shortestpath('i', 'c'))
    assert ga2.shortestpath('i', 'c') == 2

    print('Expected: 3, Actual:', ga2.shortestpath('n', 'o'))
    assert ga2.shortestpath('n', 'o') == 3


def testhasCycle():
    print('\nHas Cycle:')

    print('Expected: TRUE, Actual:', ga1.hasCycle())
    assert ga1.hasCycle()

    print('Expected: TRUE, Actual:', ga2.hasCycle())
    assert ga2.hasCycle()

    print('Expected: TRUE, Actual:', ga3.hasCycle())
    assert ga3.hasCycle()

    print('Expected: FALSE, Actual:', ga4.hasCycle())
    assert not ga4.hasCycle()


