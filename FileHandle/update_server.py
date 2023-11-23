def update_server_file(path, key, value):
    with open(path, "r") as file:
        lines = file.readlines()

    with open(path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)


update_server_file("./server.conf", "MAX_CONNECTIONS", "500")
