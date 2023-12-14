class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_path = {}
        for path in paths:
            splited_path = path.split()
            directory = splited_path[0] + "/"
            
            for i in range(1, len(splited_path)):
                index = splited_path[i].find("(")
                file_name = splited_path[i][:index]
                content = splited_path[i][index + 1: -1]
                
                if content in dict_path:
                    dict_path[content].append(directory + file_name)
                else:
                    dict_path[content] = [directory + file_name]
        
        return [files for files in dict_path.values() if len(files) > 1]