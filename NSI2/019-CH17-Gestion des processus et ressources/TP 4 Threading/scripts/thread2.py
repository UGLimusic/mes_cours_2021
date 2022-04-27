import threading

compteur = 0


def f():
    global compteur
    for i in range(1000_000):
        compteur += 1


threads = []
for i in range(4):
    threads.append(threading.Thread(target=f))

for t in threads:
    t.start()

for t in threads:
    t.join()
print(compteur)
