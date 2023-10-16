used = []
length = 0

def TicketTable(table_length):
    global length, used
    length = table_length
    used = [False] * length

# 번호가 이미 사용 중인지 여부를 반환
def isUsed(ticketIndex):
    return used[ticketIndex]

# 티켓 사용 여부를 갱신
def setUsed(index, status):
    used[index] = status
    
# 사용자의 회원 번호로 지급받게 될 행운권 번호를 계산
def findEmptyIndexByUserId(userId):
    global length, used
    index = userId % length
    
    while isUsed(index) == True:
        index = (index + 1) % length
        
    return index

def getTicketNumbers(n, m, ids):
    tickets = []
    
    TicketTable(n)
    
    for i in range(m):
        user_id = ids[i]
        ticket_index = findEmptyIndexByUserId(user_id)
        
        tickets.append(ticket_index)
        setUsed(ticket_index, True)

    return tickets

if __name__ == "__main__":
	n, m = map(int, input().split())  # n 전체 티켓의 수, m 요청 고객의 수

	ids = []
	for _ in range(m):
		ids.append(int(input()))

	tickets = getTicketNumbers(n, m, ids)

	for index in tickets:
		print(index)