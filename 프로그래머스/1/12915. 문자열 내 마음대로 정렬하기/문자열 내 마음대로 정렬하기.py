# def solution(strings, n):
#     answer = [0]*len(strings)
#     n_list = []
#     n_list_sort = []
#     n_list_sort_uni = []
#     idx = []
#     non_uni = []
#     count = 0
#     idx_uni = []
    
#     strings.sort()
    
#     for i in strings:
#         n_list.append(i[n])
    
#     n_list_sort = sorted(n_list)
    
#     for i in n_list_sort:
#         idx.append(n_list.index(i))
      
#     set_n_list = list(set(n_list_sort))
    
#     for i in set_n_list:
#         if n_list_sort.count(i) > 1:
#             non_uni.append(i)
    
#     for i in idx:
#         if i not in idx_uni:
#             idx_uni.append(i)
    
#     for i in n_list_sort:
#         if i not in n_list_sort_uni:
#             n_list_sort_uni.append(i)
    
#     if len(set(n_list_sort)) == len(n_list_sort):
#         for i in range(len(strings)):
#             answer[idx[i]] = strings[i]
#     else: 
#         for i in range(len(idx_uni)):
#             if n_list_sort_uni[i] in non_uni:
#                 for j in range(n_list_sort.count(n_list_sort_uni[i])):
#                     idx[i+j+count] = idx_uni[i]+j
#                 count += 1
#         for i in range(len(strings)):
#             answer[i] = strings[idx[i]]
                
#     return answer

def solution(strings, n):
    
    strings.sort(key=lambda x:(x[n], x))
    
    return strings

