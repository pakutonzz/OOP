def add_score(subject_score, student, subject, score) :
    if student not in subject_score :
        subject_score[student] = {}
    subject_score[student][subject] = score

    return subject_score

def calc_average_score(subject_score) :
    average_scores = {}
    for student in subject_score :
        sum = 0
        for key in subject_score[student] :
            sum += subject_score[student][key]
        average_scores[student] = f"{sum / len(subject_score[student]):.2f}"
    return average_scores