import time

def time_convert(dt: float):
    """ convert time in seconds to hh:mm:ss

    Args:
        sec (int): _description_

    Returns:
        _type_: _description_
    """

    sec = int(dt)
    msec = int((dt - sec) * 1000)

    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    return int(hours), int(mins), sec, msec


if __name__ == '__main__':
    # input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    print("{:02d}:{:02d}:{:02d}.{:03d}".format(*time_convert(time_lapsed)))
