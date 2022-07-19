def solution(id_list, report, k):

    id_list_tuple = tuple(id_list)

    reported_count = {}
    receive_mail = {}
    for i in id_list_tuple:
        reported_count[i] = 0
        receive_mail[i] = 0

    for r in set(report):
        a, b = r.split()
        reported_count[b] += 1

    for r in set(report):
        a, b = r.split()
        if reported_count[b] >= k:
            receive_mail[a] += 1

    answer = list(receive_mail.values())

    return answer

# Best Answer below

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}
#
#     for r in set(report):
#         reports[r.split()[1]] += 1
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1
#
#     return answer