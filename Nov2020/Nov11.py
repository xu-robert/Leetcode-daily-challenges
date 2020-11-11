"""
valid square
dumb question

"""

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        
        def is_square(a,b,c,d):
            
            x = ((a[0] - b[0])**2 + (a[1]-b[1])**2)**0.5
            y = ((c[0] - d[0])**2 + (c[1]-d[1])**2)**0.5
            
            if x != y: return False
            
            if a[0] < b[0]: s1 = (b[1]-a[1])/(b[0]-a[0]) 
            else: s1 = (a[1]-b[1])/(a[0]-b[0]) if b[0] != a[0] else 1
            
            if c[0] < d[0]: s2 = (d[1]-c[1])/(d[0]-c[0])
            else: s2 = (c[1]-d[1])/(c[0]-d[0]) if c[0] != d[0] else 1
            
            if (s1==0 and s2!=1) or (s2==0 and s1 != 1):
                return False
            
            if (s1 != 0 and s2 != 0) and round(s1, 10) != round(-1/s2, 10): 
                return False            
            
            xx = (a[0]+b[0])/2
            xy = (a[1]+b[1])/2
            yx = (c[0]+d[0])/2
            yy = (c[1]+d[1])/2
            
            if (xx,xy) == (yx,yy): return True
        
        return is_square(p1,p2,p3,p4) or is_square(p1,p3,p2,p4) or is_square(p1,p4,p3,p2)

a = Solution()
b = a.validSquare([0,0],[5,0],[5,4],[0,4])
x = a.validSquare([1,0],[-1,0],[0,1],[0,-1])
y = a.validSquare([-2009,2747],[-1566,2436],[-2320,2304],[-1877,1993])
z = a.validSquare([-658,-2922],[-965,-4209],[-2252,-3902],[-1945,-2615])