class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        block, column = ['']*3, ['']*9
        for index, strs in enumerate(board):
            if self.isrepeat(strs):
                return False
            for i in range(3):
                block[i] = block[i] + strs[i*3] + strs[i*3 + 1] + strs[i*3 + 2]
            
            for i in range(9):
                column[i] += strs[i]
            if index in [2, 5, 8]:
                for i in block:
                    if self.isrepeat(i):
                        return False
                block = ['', '', '']
        for strs in column:
            if self.isrepeat(strs):
                return False

        return True

    def isrepeat(self, strs):
        temp = []
        for ch in strs:
            if ch != '.' and ch not in temp:
                temp.append(ch)
            elif ch in temp:
                return True

