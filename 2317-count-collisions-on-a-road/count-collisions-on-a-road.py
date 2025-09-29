class Solution:
    def countCollisions(self, directions: str) -> int:
        rem=directions.lstrip('L').rstrip('R')

        return len(rem)-rem.count('S')