import os
import pickle

def input_scores():
    scores = []
    n = 1
    while True:
        score = int(input(f'#{n}? '))
        if score >= 0:
            scores.append(score)
            n += 1
        else:
            return scores

def get_average(scores):
    score = 0
    for i in scores:
        score += i
    return score/len(scores)

def show_scores(scores):
    for i in scores:
        print(i, end = ' ')

def load():
    filename = 'score.bin'
    if os.path.exists(filename):
        print('[파일 읽기]')
        with open(filename, 'rb') as file:
            li = pickle.load(file)
            avg = pickle.load(file)
        print('\n[점수 출력]\n개인 점수:', end = '')
        show_scores(li)
        print(f'\n평균:{avg}')
        return True
    else:
        with open(filename, 'wb') as file:
           return False

def save(scores, avg):
     filename = 'score.bin'
     with open('score.bin', 'wb') as file:
         pickle.dump(scores,file)
         pickle.dump(avg,file)

  

if not load():
    print('[점수 입력]')
    scores = input_scores()
    avg = get_average(scores)
    print('\n[점수 출력]\n개인 점수:', end = '')
    show_scores(scores)
    print(f'\n평균:{avg}')
    save(scores, avg)
