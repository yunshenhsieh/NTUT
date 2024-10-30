import datetime
from threading import Thread
def matrixMaker() -> [[]]:
    list_a = [[0 for x in range(80)] for z in range(50)]
    list_b = [[0 for x in range(50)] for z in range(80)]

    for i in range(50):
        for j in range(80):
            list_a[i][j] = 6.5 * (i + 1) - 1.8 * (j + 1)

    for i in range(80):
        for j in range(50):
            list_b[i][j] = 30 - 12.1 * (j + 1) + 5.5 * (i + 1)

    return list_a, list_b

def matrixCheck(args: list):
    for i in range(len(args)):
        # if 0 in args[i]:
        #     print(args[i])
        #     print("Have 0")
        #     print(i)
        print(i, args[i])
    pass

def funLoop(list_a: list, list_b: list):
    list_c = [[0 for x in range(50)] for z in range(50)]
    for k in range(50):
        for i in range(50):
            tot_n = 0
            for j in range(80):
                tmp = list_a[i][j] * list_b[j][i]
                tot_n = tot_n + tmp

            list_c[k][i] = tot_n
    pass

def funMultiThread(start_n: int, end_n: int, list_a: list, list_b: list, list_c: list):
    for k in range(start_n, end_n):
        for i in range(50):
            tot_n = 0
            for j in range(80):
                tmp = list_a[i][j] * list_b[j][i]
                tot_n = tot_n + tmp
            list_c[k][i] = tot_n
    pass

def funMT50(list_a: list, list_b: list):
    list_c = [[0 for x in range(50)] for z in range(50)]
    mt_1 = Thread(target=funMultiThread, args=(0, 1, list_a, list_b, list_c))
    mt_2 = Thread(target=funMultiThread, args=(1, 2, list_a, list_b, list_c))
    mt_3 = Thread(target=funMultiThread, args=(2, 3, list_a, list_b, list_c))
    mt_4 = Thread(target=funMultiThread, args=(3, 4, list_a, list_b, list_c))
    mt_5 = Thread(target=funMultiThread, args=(4, 5, list_a, list_b, list_c))
    mt_6 = Thread(target=funMultiThread, args=(6, 7, list_a, list_b, list_c))
    mt_7 = Thread(target=funMultiThread, args=(7, 8, list_a, list_b, list_c))
    mt_8 = Thread(target=funMultiThread, args=(8, 9, list_a, list_b, list_c))
    mt_9 = Thread(target=funMultiThread, args=(9, 10, list_a, list_b, list_c))
    mt_10 = Thread(target=funMultiThread, args=(10, 11, list_a, list_b, list_c))
    mt_11 = Thread(target=funMultiThread, args=(11, 12, list_a, list_b, list_c))
    mt_12 = Thread(target=funMultiThread, args=(12, 13, list_a, list_b, list_c))
    mt_13 = Thread(target=funMultiThread, args=(13, 14, list_a, list_b, list_c))
    mt_14 = Thread(target=funMultiThread, args=(14, 15, list_a, list_b, list_c))
    mt_15 = Thread(target=funMultiThread, args=(15, 16, list_a, list_b, list_c))
    mt_16 = Thread(target=funMultiThread, args=(16, 17, list_a, list_b, list_c))
    mt_17 = Thread(target=funMultiThread, args=(17, 18, list_a, list_b, list_c))
    mt_18 = Thread(target=funMultiThread, args=(18, 19, list_a, list_b, list_c))
    mt_19 = Thread(target=funMultiThread, args=(19, 20, list_a, list_b, list_c))
    mt_20 = Thread(target=funMultiThread, args=(20, 21, list_a, list_b, list_c))
    mt_21 = Thread(target=funMultiThread, args=(21, 22, list_a, list_b, list_c))
    mt_22 = Thread(target=funMultiThread, args=(22, 23, list_a, list_b, list_c))
    mt_23 = Thread(target=funMultiThread, args=(23, 24, list_a, list_b, list_c))
    mt_24 = Thread(target=funMultiThread, args=(24, 25, list_a, list_b, list_c))
    mt_25 = Thread(target=funMultiThread, args=(25, 26, list_a, list_b, list_c))
    mt_26 = Thread(target=funMultiThread, args=(26, 27, list_a, list_b, list_c))
    mt_27 = Thread(target=funMultiThread, args=(27, 28, list_a, list_b, list_c))
    mt_28 = Thread(target=funMultiThread, args=(28, 29, list_a, list_b, list_c))
    mt_29 = Thread(target=funMultiThread, args=(29, 30, list_a, list_b, list_c))
    mt_30 = Thread(target=funMultiThread, args=(30, 31, list_a, list_b, list_c))
    mt_31 = Thread(target=funMultiThread, args=(31, 32, list_a, list_b, list_c))
    mt_32 = Thread(target=funMultiThread, args=(32, 33, list_a, list_b, list_c))
    mt_33 = Thread(target=funMultiThread, args=(33, 34, list_a, list_b, list_c))
    mt_34 = Thread(target=funMultiThread, args=(34, 35, list_a, list_b, list_c))
    mt_35 = Thread(target=funMultiThread, args=(35, 36, list_a, list_b, list_c))
    mt_36 = Thread(target=funMultiThread, args=(36, 37, list_a, list_b, list_c))
    mt_37 = Thread(target=funMultiThread, args=(37, 38, list_a, list_b, list_c))
    mt_38 = Thread(target=funMultiThread, args=(38, 39, list_a, list_b, list_c))
    mt_39 = Thread(target=funMultiThread, args=(39, 40, list_a, list_b, list_c))
    mt_40 = Thread(target=funMultiThread, args=(40, 41, list_a, list_b, list_c))
    mt_41 = Thread(target=funMultiThread, args=(41, 42, list_a, list_b, list_c))
    mt_42 = Thread(target=funMultiThread, args=(42, 43, list_a, list_b, list_c))
    mt_43 = Thread(target=funMultiThread, args=(43, 44, list_a, list_b, list_c))
    mt_44 = Thread(target=funMultiThread, args=(44, 45, list_a, list_b, list_c))
    mt_45 = Thread(target=funMultiThread, args=(45, 46, list_a, list_b, list_c))
    mt_46 = Thread(target=funMultiThread, args=(46, 47, list_a, list_b, list_c))
    mt_47 = Thread(target=funMultiThread, args=(47, 48, list_a, list_b, list_c))
    mt_48 = Thread(target=funMultiThread, args=(48, 49, list_a, list_b, list_c))
    mt_49 = Thread(target=funMultiThread, args=(49, 50, list_a, list_b, list_c))
    mt_50 = Thread(target=funMultiThread, args=(5, 6, list_a, list_b, list_c))

    mt_1.start()
    mt_2.start()
    mt_3.start()
    mt_4.start()
    mt_5.start()
    mt_6.start()
    mt_7.start()
    mt_8.start()
    mt_9.start()
    mt_10.start()
    mt_11.start()
    mt_12.start()
    mt_13.start()
    mt_14.start()
    mt_15.start()
    mt_16.start()
    mt_17.start()
    mt_18.start()
    mt_19.start()
    mt_20.start()
    mt_21.start()
    mt_22.start()
    mt_23.start()
    mt_24.start()
    mt_25.start()
    mt_26.start()
    mt_27.start()
    mt_28.start()
    mt_29.start()
    mt_30.start()
    mt_31.start()
    mt_32.start()
    mt_33.start()
    mt_34.start()
    mt_35.start()
    mt_36.start()
    mt_37.start()
    mt_38.start()
    mt_39.start()
    mt_40.start()
    mt_41.start()
    mt_42.start()
    mt_43.start()
    mt_44.start()
    mt_45.start()
    mt_46.start()
    mt_47.start()
    mt_48.start()
    mt_49.start()
    mt_50.start()

    mt_1.join()
    mt_2.join()
    mt_3.join()
    mt_4.join()
    mt_5.join()
    mt_6.join()
    mt_7.join()
    mt_8.join()
    mt_9.join()
    mt_10.join()
    mt_11.join()
    mt_12.join()
    mt_13.join()
    mt_14.join()
    mt_15.join()
    mt_16.join()
    mt_17.join()
    mt_18.join()
    mt_19.join()
    mt_20.join()
    mt_21.join()
    mt_22.join()
    mt_23.join()
    mt_24.join()
    mt_25.join()
    mt_26.join()
    mt_27.join()
    mt_28.join()
    mt_29.join()
    mt_30.join()
    mt_31.join()
    mt_32.join()
    mt_33.join()
    mt_34.join()
    mt_35.join()
    mt_36.join()
    mt_37.join()
    mt_38.join()
    mt_39.join()
    mt_40.join()
    mt_41.join()
    mt_42.join()
    mt_43.join()
    mt_44.join()
    mt_45.join()
    mt_46.join()
    mt_47.join()
    mt_48.join()
    mt_49.join()
    mt_50.join()

    # for i in range(50):
    #     mt = Thread(target=funMultiThread(i, i+1, list_a, list_b, list_c))
    #     mt.start()
    #     mt.join()
    pass

def funMT10(list_a: list, list_b: list):
    list_c = [[0 for x in range(50)] for z in range(50)]
    mt_1 = Thread(target=funMultiThread, args=(0, 10, list_a, list_b, list_c))
    mt_2 = Thread(target=funMultiThread, args=(10, 20, list_a, list_b, list_c))
    mt_3 = Thread(target=funMultiThread, args=(20, 30, list_a, list_b, list_c))
    mt_4 = Thread(target=funMultiThread, args=(30, 40, list_a, list_b, list_c))
    mt_5 = Thread(target=funMultiThread, args=(40, 50, list_a, list_b, list_c))

    mt_1.start()
    mt_2.start()
    mt_3.start()
    mt_4.start()
    mt_5.start()

    mt_1.join()
    mt_2.join()
    mt_3.join()
    mt_4.join()
    mt_5.join()
    pass

if __name__ == "__main__":
    list_a, list_b = matrixMaker()
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    funLoop(list_a, list_b)
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    funMT50(list_a, list_b)
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
    funMT10(list_a, list_b)
    print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
