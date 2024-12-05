from collections import defaultdict
from functools import cmp_to_key

def check_batch_complies(batch, order_rules):
    for i in range(len(batch)-1, -1, -1):
        page = batch[i]
        for j in range(i-1, -1, -1):
            page_before = batch[j]
            if f"{page}|{page_before}" in order_rules:
                return False

    return True

def page_order(page1, page2):
    cmp_key = -1 if page2 in order_rules_combined[page1] else 1
    return cmp_key

if __name__ == "__main__":
    with open("day5.txt", "r") as f:
        order_rules, pages_to_print = f.read().split("\n\n")

    order_rules = order_rules.splitlines()
    pages_to_print = [batch.split(",") for batch in pages_to_print.splitlines()]

    sum_middle_pages = 0
    incorrect_batches = []
    for batch in pages_to_print:
        if check_batch_complies(batch, order_rules):
            sum_middle_pages += int(batch[int(len(batch)/2)])
        else:
            incorrect_batches.append(batch)
    print(f"Part 1: {sum_middle_pages}")

    order_rules_combined = defaultdict(set)
    for rule in order_rules:
        op1, op2 = rule.split("|")
        order_rules_combined[op1].add(op2)

    sum_middle_pages = 0
    for batch in incorrect_batches:
        sorted_batch = sorted(batch, key=cmp_to_key(page_order))
        sum_middle_pages += int(sorted_batch[int(len(batch)/2)])
    print(f"Part 2: {sum_middle_pages}")
        