import numpy as np

def is_report_safe(report_diff):
    return (all(report_diff > 0) or all(report_diff < 0)) and all(abs(report_diff) < 4)

if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        unusual_data = [[int(level) for level in line.strip().split()] for line in f.readlines()]

    report_diffs = [np.diff(report) for report in unusual_data]
    print(f"Part 1: {sum([is_report_safe(np.diff(report)) for report in unusual_data])}")

    safe_count = 0
    for report in unusual_data:
        for i in range(len(report)):
            report_diff = np.diff(report[:i] + report[i+1:])
            safe = (all(report_diff > 0) or all(report_diff < 0)) and all(abs(report_diff) < 4)
            if safe:
                safe_count += 1
                break

    print(f"Part 2: {safe_count}")