from time import sleep , ctime
import multiprocessing

def super_player(file_, time):
    for i in range(2):
        print('Start playing: %s %s' %(file_, ctime()))
        sleep(time)

lists = {'爱情买卖.mp3':3, '阿凡达.mp4':5, '我和你.mp3':4}

threads = []
files = range(len(lists))

# 创建进程
for file_, time in lists.items():
    t = multiprocessing.Process(target=super_player, args=(file_, time))
    threads.append(t)

if __name__ == '__main__':
    # 启动进程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s' % ctime())