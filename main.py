"""
Connor Cox
U3 Lab 3
Merge Sort
"""

def merge_sort(list):
  if len(list) == 1:
    return list

  
  middle = int(len(list) / 2)
  left = list[:middle]
  right = list[middle:]
  left = merge_sort(left)
  right = merge_sort(right)
  sorted = []
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      sorted.append(left[0])
      del left[0]
    elif right[0] < left[0]:
      sorted.append(right[0])
      del right[0]
    else:
      sorted.append(right[0])
      del right[0]
      sorted.append(left[0])
      del left[0]

  if len(left) == 0:
    sorted.extend(right)
    return sorted
  elif len(right) == 0:
    sorted.extend(left)
    return sorted


def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()