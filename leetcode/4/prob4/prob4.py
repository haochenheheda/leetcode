class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        ind1 = 0
        ind2 = 0
        tmp = 0
        tmp1 = 0
        if (len1 + len2)%2 == 1:
            while (ind1 + ind2) <= (len1 + len2)/2:
            	if ind1 == len1:
            		tmp = nums2[ind2]
            		ind2 += 1
            	elif ind2 == len2:
            		tmp = nums1[ind1]
            		ind1 += 1
            	else:
            		if nums1[ind1] <= nums2[ind2]:
            			tmp = nums1[ind1]
            			ind1 += 1
            		else:
            			tmp = nums2[ind2]
            			ind2 += 1
        else:
            while (ind1 + ind2) <= (len1 + len2)/2:
            	if ind1 == len1:
            		tmp1 = tmp
            		tmp = nums2[ind2]
            		ind2 += 1
            	elif ind2 == len2:
            		tmp1 = tmp
            		tmp = nums1[ind1]
            		ind1 += 1
            	else:
            		if nums1[ind1] <= nums2[ind2]:
            			tmp1 = tmp
            			tmp = nums1[ind1]
            			ind1 += 1
            		else:
            			tmp1 = tmp
            			tmp = nums2[ind2]
            			ind2 += 1
        if (len1 + len2)%2 == 1:
            return float(tmp)
        else:
            return float(tmp+tmp1)/2
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		len1 = len(nums1)
		len2 = len(nums2)
		if len1 > len2:
			len1,len2 = len2,len1
			tmp = nums1
			nums1 = nums2
			nums2 = tmp


		ind1 = len1/2
		mid_num = (len1+len2)/2
		ind2 = mid_num - ind1
		l = 0
		r = len1
		while True:
			flag = 't'
			if ind1 > 0 and ind2 < len2:
				if nums1[ind1-1] > nums2[ind2]:
					flag = 'l'

			if ind1 < len1 and ind2 > 0:
				if nums1[ind1] < nums2[ind2-1]:
					flag = 'r'
			if flag == 't':
				break
			elif flag == 'l':
				r = ind1
				ind1 = (r + l)/2
				ind2 = mid_num - ind1
			elif flag == 'r':
				l = ind1
				ind1 = (l+r)/2 + 1
				ind2 = mid_num - ind1
		if ind1 == 0:
			tmp1 = nums2[ind2-1]
		elif ind2 == 0:
			tmp1 = nums1[ind1-1]
		else:
			tmp1 = max(nums1[ind1-1],nums2[ind2-1])
		if ind1 == len1:
			tmp2 = nums2[ind2]
		elif ind2 == len2:
			tmp2 = nums1[ind1]
		else:
			tmp2 = min(nums1[ind1],nums2[ind2])

		if (len1+len2)%2:
			return float(tmp2)
		else:
			return float(tmp1 + tmp2)/2



        	# while True:


if __name__ == '__main__':
	nums1 = [1,2]
	nums2 = [3,5,6]
	a = Solution1() 
	print(a.findMedianSortedArrays(nums1,nums2))