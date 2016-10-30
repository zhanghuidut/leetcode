class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split("/")
        res = []
        for item in path_list:
            if item in [".."] and res:
                res.pop()
            elif item not in ["", "."]:
                res.append(item)
        return "/" + "/".join(res)
