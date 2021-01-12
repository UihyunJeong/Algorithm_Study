def solution(record):
    answer = []
    
    user_id = {}  # key : uid, val : last_id
    
    for user_record in  record :
        user_record = user_record.split()
        if user_record[0] == 'Leave' :
            continue
        else :
            user_id[user_record[1]] = user_record[2]
    
    for user_record in record :
        user_record = user_record.split()
        if user_record[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(user_id[user_record[1]]))
        elif user_record[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(user_id[user_record[1]]))
            
        
    return answer
