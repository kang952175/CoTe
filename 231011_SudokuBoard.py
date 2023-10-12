# -*- coding: utf-8 -*-
class SudokuBoard:
	def __init__(self):
		self.MAX_ROW = 9
		self.MAX_COL = 9
		

	# 행의 번호를 계산
	def getRowByIndex(self, index):
		self.index = index
		row = (self.index - 1) // 9 + 1
		return row
	
	# 열의 번호를 계산
	def getColByIndex(self, index):
		self.index = index
		col = (self.index - 1) % 9 + 1 # zero base + 1 => raw
		return col
	
	# 그룹 번호를 계산
	def getGroupByIndex(self, index):
		self.index = index
		r = self.getRowByIndex(self.index)
		c = self.getColByIndex(self.index)
		return self.getGroupByPosition(r, c)

	# (행, 열)로 그룹 번호를 계산
	def getGroupByPosition(self, row, column):
		self.row = row
		self.column = column
		left = ( (self.row -1)//3 ) * 3 + 1 # 이 행이 속한 가장 왼쪽 그룹 번호
		offset = ( (self.column - 1)// 3) # 실제 이 열이 속한 그룹의 위치
		return left + offset
	
	# (행, 열)로 칸의 번호를 계산
	def getIndexByPosition(self, row, column):
		self.row = row
		self.column = column
		left = (self.row - 1) * 9 + 1
		offset = (self.column - 1)
		return left + offset

def testCase(caseIndex):
	board = SudokuBoard()
	index = int(input())

	row = board.getRowByIndex(index)
	col = board.getColByIndex(index)
	group = board.getGroupByIndex(index)

	print("Case #{}:".format(caseIndex))
	print("{} {} {}".format(row, col, group))

if __name__ == "__main__":
	caseSize = int(input())
	
	for caseIndex in range(1, caseSize+1):
		testCase(caseIndex)