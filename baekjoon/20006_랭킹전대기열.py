p, m = map(int, input().split())

class Room:
    creator_level: int
    participate_limit: int
    participate_count: int
    participate: list
    status: int

    def __init__(self, creator_level: int) -> None:
        self.participate_limit = m
        self.creator_level = creator_level
        self.participate_count = 0
        self.participate = []
        self.status = 0

    def particiate(self, level: int, nickname: str) -> None:
        self.participate_count += 1
        self.participate.append([level, nickname])

        if self.participate_count == self.participate_limit:
            self.status = 1

    def get_participate(self) -> list:
        participate_list = sorted(self.participate, key=lambda x: x[1])
        return participate_list
    
    def get_status(self) -> int:
        return self.status
    
room_list = []
for _ in range(p):
    level, nickname = map(str, input().split())
    level = int(level)

    if len(room_list) == 0:
        new_room = Room(creator_level=level)
        new_room.particiate(level, nickname)
        room_list.append(new_room)
    else:
        for idx in range(len(room_list)):
            room: Room = room_list[idx]
            if room.get_status() == 0 and room.creator_level - 10 <= level <= room.creator_level + 10:
                room.particiate(level, nickname)
                break
            elif idx == len(room_list)-1:
                new_room = Room(creator_level=level)
                new_room.particiate(level, nickname)
                room_list.append(new_room)

for r in room_list:
    print("Started!" if r.get_status() == 1 else "Waiting!")
    for pl in r.get_participate():
        print(pl[0], pl[1])
