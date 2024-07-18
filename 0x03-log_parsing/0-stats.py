#!/usr/bin/python3

import re
import sys
import signal

metrics = {
    'File_size': 0,
    'Status_code': {},
}
line_count = 0


def print_metrics():
    print(f"File size: {metrics['File_size']}")
    for code in sorted(metrics['Status_code'].keys()):
        print(f"{code}: {metrics['Status_code'][code]}")


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

log_pattern = r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
for line in sys.stdin:
    match = re.match(log_pattern, line)
    if match:
        file_size = int(match.group(4))
        status_code = int(match.group(3))
        metrics['File_size'] += file_size
        current_count = metrics['Status_code'].get(status_code, 0)
        metrics['Status_code'][status_code] = current_count + 1
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
print_metrics()
