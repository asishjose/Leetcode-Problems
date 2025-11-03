class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        x = target
        doubles = target//2
        while x>1:

            if maxDoubles==0:
                moves = moves+(x-1)
                return int(moves)

            if x%2 != 0:
                x-=1
            else:
                if maxDoubles!=0:
                    x = x/2
                    maxDoubles-=1
                else:
                    x-=1
            moves+=1
        return moves