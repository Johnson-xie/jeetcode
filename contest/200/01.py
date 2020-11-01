class Solution:
    def getWinner(self, arr, k: int) -> int:

        if k >= len(arr) - 1:
            return max(arr)

        win_cnt = 0
        cur = 0
        while k != win_cnt:
            if arr[cur] > arr[1]:
                win_cnt += 1
                arr = [arr[cur]] + arr[2:] + [arr[1]]
            else:
                win_cnt = 1
                arr = [arr[1]] + arr[2:] + [arr[0]]
        return arr[cur]


class Solution2:
    def minSwaps(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid)

        for i in range(n - 1):
            if sum(grid[i][i + 1:]) == 0:
                continue
            else:
                for j in range(i + 1, n):
                    if sum(grid[j][i + 1:]) == 0:
                        cnt += j - i
                        row = grid.pop(j)
                        grid.insert(i, row)
                        break
                else:
                    return -1

        return cnt


class Solution3:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        common_node = self.get_common_node(nums1, nums2)
        n1, n2 = 0, 0
        cur_max = 0

        if not common_node:
            return max(sum(nums1), sum(nums2))

        for n1_end, n2_end in common_node:
            path1 = sum(nums1[n1:n1_end])
            path2 = sum(nums2[n2:n2_end])
            cur_max += max(path1, path2)
            n1 = n1_end
            n2 = n2_end

        return (cur_max + max(sum(nums1[n1:]), sum(nums2[n2:]))) % (10 ** 9 + 7)

    def get_common_node(self, nums1, nums2):
        res = []
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                res.append((i, j))
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    # grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
    ret = Solution2().minSwaps(grid)
    print(ret)
