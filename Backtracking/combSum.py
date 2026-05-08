def combinationSum(candidates, target):
    all_combinations = []
    def dfs(index, current_combination, current_sum):
        if current_sum == target:
            all_combinations.append(current_combination)
            return
        if index >= len(candidates) or current_sum > target:
            return
    dfs(0, [], 0)
    return all_combinations