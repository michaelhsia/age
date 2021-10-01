driving = input('請問你有沒也開過車？')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit
    
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗裡!!!')
    else:
        print('奇怪 你怎麼會開過車呢？')
elif driving == '沒有':
    if age >= 18:
        print('你可以去考駕照了')
    else:
        print('很好, 你再過幾年就能開車了')