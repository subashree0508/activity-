class Solution:
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(start, path, total):
            if total == target:
                result.append(path)
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                backtrack(i, path + [candidates[i]], total + candidates[i])
        backtrack(0, [], 0)
        return result
