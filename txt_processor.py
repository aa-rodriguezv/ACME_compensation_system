import hourly_compensation_API as hc
import sys


def process_file_workers_schedule(file_path='./test.txt'):
    file = open(file_path, 'rt')
    data = file.read()
    workers_record = data.split('\n')

    for worker in workers_record:
        print(hc.process_worker_compensation(worker))


if __name__ == '__main__':
    cmdr_args = sys.argv

    if len(cmdr_args) > 1:
        process_file_workers_schedule(cmdr_args[1])
    else:
        process_file_workers_schedule()

