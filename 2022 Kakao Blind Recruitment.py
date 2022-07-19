def solution(id_list, report, k):

    # create a dictionary with id_list as key and a list of len(id_list) + 1
    id_tuple = tuple(id_list)

    reported_dict = {}
    count_dict = {}
    mailsent_dict = {}
    for i in id_tuple:
        reported_dict[i] = 0
        count_dict[i] = [0]*len(id_list)
        mailsent_dict[i] = 0

    # create a list with unique reports
    unique_report = []
    for i in report:
        if i not in unique_report:
            unique_report.append(i)

    
    for i in range(0, len(id_list)):
        for j in range(0, len(unique_report)):
    # when reported, count and store the value as the first element of the list associated with the key value        
            if id_list[i] == unique_report[j][len(unique_report[j]) - len(id_list[i]):]:
                reported_dict[id_list[i]] += 1
                
    # when the id reports another id, add 1 to the column of where the id is...
            if id_list[i] == unique_report[j][:len(id_list[i])]:
                right_position = id_list.index(unique_report[j][len(id_list[i])+1:])
                count_dict[id_list[i]][right_position] = 1

    # check the ids that have been reported more than k
    reported_ids_index = []
    for i in id_list:
        if reported_dict[i] >= k:
            reported_ids_index.append(id_list.index(i))

    # calculate how many mails each id will receive
    for i in id_list:
        for j in reported_ids_index:
            if count_dict[i][j] == 1:
                mailsent_dict[i] += 1
    
    answer = list(mailsent_dict.values()) 
    return answer 
