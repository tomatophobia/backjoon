def no_sharp(m):
    mp = ''
    for i in range(len(m)):
        if m[i] == '#':
            mp = mp[:-1] + mp[-1].lower()
        else:
            mp += m[i]
    return mp


def solution(m, musicinfos):
    mp = no_sharp(m)

    answer = ''
    maxTime = 0
    for s in musicinfos:
        info = s.split(',')

        t2 = list(map(int, info[1].split(':')))
        t1 = list(map(int, info[0].split(':')))

        sec = 0
        if (t2[1] - t1[1] < 0):
            sec += 60 + (t2[1] - t1[1])
            t2[0] -= 1
        else:
            sec += t2[1] - t1[1]
        sec += 60 * (t2[0] - t1[0])

        lp = no_sharp(info[3])

        music = lp * (sec // len(lp)) + lp[:sec % len(lp)]

        if mp in music and sec > maxTime:
            answer = info[2]
            maxTime = sec

    return answer

print(solution("ABCDEFG", ["12:00,15:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	))