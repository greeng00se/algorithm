def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    new_logs = []
    for log in logs:
        s, e = map(str_to_int, log.split('-'))
        new_logs.append((s, e))
        
    s_psum = [0] * (play_time + 1)
    e_psum = [0] * (play_time + 1)
    
    for s, e in new_logs:
        s_psum[s] += 1
        e_psum[e] += 1
        
    s_count = 0
    e_count = 0
    for i in range(1, play_time):
        s_count += s_psum[i]
        e_count += e_psum[i]
        s_psum[i] = s_count + s_psum[i - 1]
        e_psum[i] = e_count + e_psum[i - 1]
        
    result = 0
    answer = 0
    for i in range(adv_time, play_time):
        a = s_psum[i] - s_psum[i - adv_time]
        b = e_psum[i] - e_psum[i - adv_time]
        if a - b > result:
            answer = i - adv_time + 1
            if i == adv_time:
                answer = 0
            result = a - b

    return int_to_str(answer)


def str_to_int(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def int_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str((time % 3600) // 60).zfill(2)
    s = str(time % 60).zfill(2)
    return ":".join([h, m, s])

# 해당 풀이 프로그래머스 통과했지만 아래 부분 문제 있음
# 통과는 했지만 테스트 케이스 추가해서 확인해보면 사실 상 틀린 답
print(solution("00:00:05", "00:00:02", ["00:00:01-00:00:03"]))