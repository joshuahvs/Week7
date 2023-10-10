# def reverse(list):
#     new_list = []
#     for i in range(1, len(list)+1):
#         new_List += [(list[-i])]
#     return new_list

# print(reverse([1,2,3]))

def reverse(a:list):
  new_list = []
  for i in range(1, len(a)+1):
    new_list += [(a[-i])]
  return new_list

print(reverse([1,2,3]))