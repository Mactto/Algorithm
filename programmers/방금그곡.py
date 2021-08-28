def changecode(music_):

    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')
    music_ = music_.replace('E#', 'e')
    return music_


def solution(m, musicinfos):
    answer = []
    m = changecode(m)

    for music in musicinfos:
        music = music.split(',')
        music[3] = changecode(music[3])
        start_time = int(music[0].split(':')[0]) * \
            60 + int(music[0].split(':')[1])
        end_time = int(music[1].split(':')[0]) * \
            60 + int(music[1].split(':')[1])
        play_time = end_time - start_time

        if play_time < len(music[3]):
            melody = music[3][:play_time]
        else:
            melody = (music[3] * (play_time // len(music[3])))[:play_time]

        if m in melody:
            answer.append([music[2], play_time])

    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    if answer:
        return answer[0][0]
    else:
        return "(None)"


if __name__ == "__main__":
    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    print(solution(m, musicinfos))
