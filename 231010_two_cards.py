from bisect import bisect_left
 
def BinarySearch(a, x):
	i = bisect_left(a, x)
	
	if i != len(a) and a[i] == x:
		return i
	else:
		return -1
	
def Solution(n, m, cards, target):
	
	answer = 0
	
	cards.sort()
	
	for k in target:
		
		possible = False
		for p in cards:
			q = k - p
			
			if BinarySearch(cards, q) >= 0:
				possible = True
				break
		
		if possible:
			answer += 1
	
	return answer

if __name__ == "__main__":
	n, m = map(int, input().split())
	cards = list(map(int, input().split()))
	target = list(map(int, input().split()))
	print(Solution(n, m, cards, target))