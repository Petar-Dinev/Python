# nums = list(map(int, input().split(', ')))
# list_with_indices_and_no = list(map(lambda x: x if nums[x] % 2 == 0 else 'no', range(len(nums))))
# even_indices = list(filter(lambda x: x != 'no', list_with_indices_and_no))
# print(even_indices)


nums2 = [int(num) for num in input().split(', ')]
even_indices = [i for i, value in enumerate(nums2) if value % 2 == 0]
print(even_indices)
