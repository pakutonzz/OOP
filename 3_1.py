def add_score(subject_score, subject, score) :
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score) :
    sum = 0
    for key in subject_score :
        sum += subject_score[key]
    return "{:.2f}".format(sum / len(subject_score))

