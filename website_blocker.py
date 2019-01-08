import time
from datetime import datetime as dt
hosts_path = "/private/etc/hosts"
ip_address = "127.0.0.1"
websites = ["www.facebook.com",
            "facebook.com",
            "www.instagram.com",
            "instagram.com",
            # "www.youtube.com",
            # "youtube.com",
            "www.linkedin.com",
            "linkedin.com",
            "www.netflix.com",
            "netflix.com"]

start_time = dt(dt.now().year, dt.now().month, dt.now().day, 3)
stop_time = dt(dt.now().year, dt.now().month, dt.now().day, 4)


def calc_seconds_til_stop():
    time_left = (stop_time-dt.now()).seconds
    return time_left
# Calculates time left between stop time and the time I open my computer


def calc_seconds_til_start():
    if dt.now().hour < start_time.hour:
        time_left = (start_time-dt.now()).seconds
        return time_left
    elif dt.now().hour > start_time.hour:
        return (dt(dt.now().year, dt.now().month, dt.now().day+1, 8)-dt.now()).seconds
# Calculates time left between start time and the time I open my computer


while True:
    if start_time <= dt.now() < stop_time:
        with open(hosts_path, "r") as file1:
            contents = file1.read()
        count = 0
        contents_split = contents.split("\n")
        for thing in contents_split:
            if ".com" in thing:
                count += 1
        if count < len(websites):
            with open(hosts_path, "a") as file2:
                for site in websites:
                    if site not in contents:
                        file2.write("\n{}\t{}".format(ip_address, site))
        elif count > len(websites):
            with open(hosts_path, "w") as file3:
                for thing in contents_split:
                    if ".com" in thing and thing.split("\t")[len(thing.split("\t"))-1] not in websites:
                        contents_split.remove(thing)
                contents_return = "\n".join(contents_split)
                file3.seek(0)
                file3.truncate()
                file3.write(contents_return)
        time.sleep(calc_seconds_til_stop()+3)

    else:
        with open(hosts_path, "r") as file:
            contents = file.read()
        if websites[0] in contents:
            contents = contents.split("\n")
            contents2 = [item for item in contents if item.split(
                "\t")[len(item.split("\t"))-1] not in websites]
            with open(hosts_path, "w") as file2:
                file2.write("\n".join(contents2))
        time.sleep(calc_seconds_til_start()+3)
