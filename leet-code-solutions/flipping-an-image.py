class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image2 =[]
        for val in image:
            val = val[::-1]
            image2.append(val)
        
        for i in range(len(image2)):
            for j in range(len(image2[0])):
                if image2[i][j]==0:
                    image2[i][j]=1
                else:
                    image2[i][j]=0
        return image2
        """
        class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j]^=1
                
        return image
        """
    
        