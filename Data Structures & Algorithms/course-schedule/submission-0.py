class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #plot all prereqs on a graph and detect for a cycle 
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for crs, prqs in prerequisites:
            preMap[crs].append(prqs)

        seen = set()

        def dfs(course):
            if course in seen: 
                return False 
            if preMap[course] == []:
                return True 
            seen.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            preMap[course] = []
            return True
        
        #what if graphs are not connected
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True 
                
            

