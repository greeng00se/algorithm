# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/

def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    new_logs = []
    for log in logs:
        s, e = map(str_to_int, log.split('-'))
        new_logs.append((s, e))
        
    psum = [0] * (play_time + 1)
    
    for s, e in new_logs:
        psum[s] += 1
        psum[e] -= 1
        
    # 누적 재생 구간 갯수
    for i in range(1, play_time):
        psum[i] += psum[i - 1]
        
    # 한 번더 for문을 사용하면 누적 재생시간 합
    # for i in range(1, play_time):
    #     psum[i] = psum[i] + psum[i - 1]
        
    max_value, answer = sum(psum[:adv_time]), 0
    cur_value = max_value
    for i in range(1, play_time + 1 - adv_time):
        cur_value = cur_value - psum[i - 1] + psum[i + adv_time - 1]
        if cur_value > max_value:
            max_value = cur_value
            answer = i

    return int_to_str(answer)

def str_to_int(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

def int_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str((time % 3600) // 60).zfill(2)
    s = str(time % 60).zfill(2)
    return ":".join([h, m, s])

print(solution("00:00:05", "00:00:02", ["00:00:01-00:00:03"]))