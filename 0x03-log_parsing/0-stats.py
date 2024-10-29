#!/usr/bin/python3
import sys
import signal
import re

# Initialize counters
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to parse the log line format
log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(signum, frame):
    """Handle keyboard interruption (CTRL+C) to print stats and exit."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from standard input
for line in sys.stdin:
    line_count += 1
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        
        # Update total file size and status code count
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
    
    # Print stats after every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if input ends without interruption
print_stats()
