class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        area=0
        width=0
        obstacles=0
        while i<len(height)-1:
            max_height=height[i]
            k=i+1
            if max(height[k::])<max_height:
                max_height=max(height[k::])
            while  k<len(height)-1 and height[k]<max_height :
                obstacles+=height[k]
                width+=1
                k+=1
            area+=max_height*width-obstacles
            width=0
            obstacles=0
            i=k
        return area
        