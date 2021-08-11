Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [12,-7,5,64,-14]
>>> list2 = [12,14,-95,3]
>>> for num in list1:
	if num >= 0:
		print(num, end = " ")

		
12 5 64 
>>> for num in list2:
	if num >= 0:
		print(num, end = " ")

		
12 14 3 
>>> 