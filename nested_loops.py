if __name__ == '__main__':
    nested_list=[]
    score_list=[]  
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list= [ name, score]
        nested_list.append(name_score_list)
        score_list.append(score)
    second_lowest_score= sorted(list(set(score_list)))[1]
    new_name=[]
    for name,score in nested_list:
        if score==second_lowest_score:
            new_name.append(name)
    new_name.sort()
    for names in new_name:
        print(names)
            
            
        
