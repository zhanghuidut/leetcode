第一种方法时间复杂度：O(m*n+k), k是与board中字母重复次数有关的指数
第二种方法时间复杂度：O(m*n*l), l=pow(4, len(word))
虽然第一种TLE，但是平均来说第一种应该优于第二种？
# TLE
'''
["aaaa","aaaa","aaaa","aaaa","aaab"]
"aaaaaaaaaaaaaaaaaaaa"
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        nums = {}
        for i in range(m):
            for j in range(n):
                if board[i][j] in word:
                    if board[i][j] in nums:
                        nums[board[i][j]].append((i, j))
                    else:
                        nums[board[i][j]] = [(i, j)]
        index = [-1]*len(word)
        visited = [[0]*n for _ in range(m)]
        dep = 0
        last = [(-1, -1)]
        while dep > -1:
            index[dep] += 1
            if word[dep] not in nums:
                return False
            if index[dep] < len(nums[word[dep]]):
                i, j = nums[word[dep]][index[dep]]
                li, lj = last[-1]
                if dep == 0 or ((i-li, j-lj) in [(1, 0), (0, 1), (-1, 0), (0, -1)] and not visited[i][j]):
                    if dep == len(word)-1:
                        return True
                    else:
                        last.append((i, j))
                        visited[i][j] = 1
                        dep += 1
                        index[dep] = -1
            else:
                dep -= 1
                if dep > -1:
                    fir, sec = last.pop()
                    visited[fir][sec] = 0
        return False

# AC
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.helper(board, word, i, j):
                    return True
        return False
        
    def helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            board[i][j] = ''
            if not word[1:]:
                return True
            if i+1 < len(board) and self.helper(board, word[1:], i+1, j):
                return True
            if j+1 < len(board[0]) and self.helper(board, word[1:], i, j+1):
                return True
            if i-1 >= 0 and self.helper(board, word[1:], i-1, j):
                return True
            if j-1 >= 0 and self.helper(board, word[1:], i, j-1):
                return True
            board[i][j] = word[0]
        
