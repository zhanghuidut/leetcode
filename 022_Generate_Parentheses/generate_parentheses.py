# backtrack排列树 Time Limit Exceeded 
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(dep):
            if dep >= h:
                if self.isValid(sets):
                    res.append(''.join(sets))
            else:
                for i in range(dep, h+1):
                    if i == dep:
                        backtrack(dep+1)
                    elif sets[dep] != sets[i]:
                        sets[dep], sets[i] = sets[i], sets[dep]
                        backtrack(dep+1)
                        sets[dep], sets[i] = sets[i], sets[dep]

        sets, h, res = ['(', ')']*n, n*2-1, []
        backtrack(0)
        return list(set(res))
    
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == ')':
                try:
                    tmp = stack.pop() 
                except IndexError:
                    return False
                else:
                    if tmp != '(':
                        return False
            else:
                stack.append(ch)

        return False if stack else True

# backtrack组合树 AC
class Solution(object):
    # 递归
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(path):
            if len(path) >= hei:
                if self.isValid(path):
                    res.append(path)
            else:
                for ch in '()':
                    backtrack(path+ch)

        res, hei = [], 2*n
        backtrack('')
        return res

    # 迭代
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, dep = [], 0
        index = [-1]*(2*n)
        tmp = ''
        while dep > -1:
            index[dep] += 1
            if index[dep] < 2:
                tmp += '(' if index[dep] == 0 else ')'
                if dep == 2*n-1:
                    if self.isValid(tmp):
                        res.append(tmp)
                    tmp = tmp[:-1]
                else:
                    dep += 1
                    index[dep] = -1
            else:
                dep -= 1
                tmp = tmp[:-1]
        return res

    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == ')':
                try:
                    tmp = stack.pop() 
                except IndexError:
                    return False
                else:
                    if tmp != '(':
                        return False
            else:
                stack.append(ch)

        return False if stack else True
