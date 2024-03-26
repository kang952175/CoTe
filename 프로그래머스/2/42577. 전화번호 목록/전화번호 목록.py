def solution(phone_book):
    hash_map = dict.fromkeys(phone_book, 1)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # temp가 hash_map에 존재하고, temp가 현재의 phone_number가 아닌 경우
            if temp in hash_map and temp != phone_number:
                return False  
    return True 
