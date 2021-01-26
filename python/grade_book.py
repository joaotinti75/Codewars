def get_grade(s1, s2, s3):
    mean = (s1+s2+s3) // 3

    if 90 <= mean <= 100:
        return 'A'
    elif 80 <= mean < 90:
        return 'B'
    elif 70 <= mean < 80:
        return 'C'
    elif 60 <= mean < 70:
        return 'D'
    else:
        return "F"

    