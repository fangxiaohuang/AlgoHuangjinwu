import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        si, sj = ball
        ei, ej = hole
        directions = {"d": (1, 0), "l": (0, -1), "r": (0, 1), "u": (-1, 0)}
        path = [[None for _ in range(n)] for _ in range(m)]
        path[si][sj] = ""
        pq = []
        heapq.heappush(pq, ("", si, sj))
        while pq:
            p, i, j = heapq.heappop(pq)
            for k, v in directions.items():
                di, dj = v
                ni, nj = i, j
                while 0 <= ni+di < m and 0 <= nj+dj < n and maze[ni+di][nj+dj] == 0:
                    ni, nj = ni+di, nj+dj
                    if ni == ei and nj == ej:
                        break
                np = p + k
                if path[ni][nj] is None or np < path[ni][nj]:
                    path[ni][nj] = np
                    heapq.heappush(pq, (np, ni, nj))
        return path[ei][ej] if path[ei][ej] is not None else -1


