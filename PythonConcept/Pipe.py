#exchaning objects between processes
import multiprocessing
from multiprocessing import Process , Pipe

def f(conn):
    conn.send(['hello','im','rohith'])
    conn.close()

if __name__ == "__main__":
    parent_conn , child_conn = Pipe()
    p = Process(target = f , args = (child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()

