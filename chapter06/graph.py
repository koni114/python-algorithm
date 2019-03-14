from collections import defaultdict
test = defaultdict(0)


# 인접 리스트를 python 으로 구현
graph = {'A' : set(['B', 'C']),
         'B' : set(['A', 'D', 'E']),
         'C' : set(['A', 'F']),
         'D' : set(['B']),
         'E' : set(['B', 'F']),
         'F' : set(['C', 'E'])
}

# dfs






