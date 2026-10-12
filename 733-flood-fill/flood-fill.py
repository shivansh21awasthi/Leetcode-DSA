class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        if original == newColor:  
            return image

        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = newColor

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                    image[nr][nc] = newColor
                    queue.append((nr, nc))

        return image
