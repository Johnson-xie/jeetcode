class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        def help(heights, bricks, ladders, p):
            while p <= len(heights)-1:
                if p == len(heights) - 1:
                    return p
                elif heights[p] >= heights[p + 1]:
                    p += 1
                else:
                    break
            height = heights[p+1]-heights[p]
            if bricks >= height and ladders:
                return max(help(heights, bricks-height, ladders, p+1), help(heights, bricks, ladders-1, p+1))
            elif bricks > height:
                return help(heights, bricks-height, ladders, p+1)
            elif ladders > 0:
                return help(heights, bricks, ladders-1, p+1)
            else:
                return p
        return help(heights, bricks, ladders, 0)


if __name__ == '__main__':
    heights = [3, 19]
    bricks = 87
    ladders = 1
    # 优化思路，如果砖头大于所有差，就直接用砖头
    ret = Solution().furthestBuilding(heights, bricks, ladders)
    print(ret)
