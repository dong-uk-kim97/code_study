import collections
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stopped = collections.defaultdict(int)
    
    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stopped[b]+=1
    
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stopped[user]>=k:
                mail+=1
        answer.append(mail)
    
    return answer