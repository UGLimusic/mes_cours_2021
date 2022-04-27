for i in range(len(H)):
    if H[i] - H[i - 1] == 1 or H[i + 1] - H[i] == 1:
        print(H[i - 1], ', ', H[i], ' et ', H[i + 1], ' sont 3 nombres Harshad consécutifs.')
