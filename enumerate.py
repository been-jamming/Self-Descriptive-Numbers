import math

def is_solution(s):
	#print("verifying " + str(s))
	for i in range(len(s)):
		if s[i] != sum([1 if digit is i else 0 for digit in s]):
			return False
	return True

def search(current_num, max_length, current_sum):
	#print("searching len " + str(max_length) + " " + str(current_num))
	#input()
	if current_sum == max_length and len(current_num) == max_length and is_solution(current_num):
		print(str(max_length) + ": " + ", ".join([str(digit) for digit in current_num]))
	elif len(current_num) != max_length and len(current_num) != 0:
		for digit in range(math.ceil((max_length - current_sum)/len(current_num)) + 1):
			search(current_num + [digit], max_length, current_sum + digit*len(current_num))
	elif len(current_num) != max_length:
		for digit in range(max_length):
			search(current_num + [digit], max_length, current_sum)

if __name__ == "__main__":
	for i in range(1, 20):
		search([], i, 0);
