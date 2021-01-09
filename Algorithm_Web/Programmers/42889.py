def solution(N, stages):
    # stages size = n
    
    # O(nlog(n))
    stages = sorted(stages)
    
    # O(n)
    stopped = {stage_num:0 for stage_num in range(1,N+1)}
    for stopped_stage in stages :
        if stopped_stage > N :
            continue
        stopped[stopped_stage] += 1
    
    
    # over O(n) but N(under 500) is too small than n.
    total = {stage_num:0 for stage_num in range(1,N+1)}
    left_idx = 0
    all_person = len(stages)
    for stage_num in range(1, N+1):
        while left_idx < all_person and stage_num > stages[left_idx] :
            left_idx += 1
            
        total[stage_num] = all_person - (left_idx)
    
    
    # O(N)
    fail_percent = {}
    for stage_num in range(1, N+1) :
        if total[stage_num]:
            fail_percent[stage_num] = stopped[stage_num]/total[stage_num]
        else :
            fail_percent[stage_num] = .0

    # O(Nlog(N))
    return [stage_num for stage_num,_ in sorted(fail_percent.items(), key = lambda x :x[1], reverse=True)]
