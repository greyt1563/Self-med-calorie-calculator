def bmi_func(h, w):
    m = h/100
    bmi = w/(m**2)
    print("Your Body mass index is:- %0.2f" % bmi)
    return round(bmi, 2)


def Health_status(bmi):
    if bmi < 16:
        pr = "Health Status :- Severe Thinness"
    elif 16 <= bmi < 18.5:
        pr = "Health Status :- Moderate Thinness"
    elif 18.5 <= bmi < 25:
        pr = "Health Status :- Normal"
    elif 25 <= bmi < 30:
        pr = "Health Status :- OverWeight"
    elif 30 <= bmi < 35:
        pr = "Health Status :-Obese class 1"
    elif 35 <= bmi < 40:
        pr = "Health Status :- Obese class 2"
    elif bmi > 40:
        pr = "Health Status :- Obese class 3"
    return pr

def Health_statusimg(bmi):
    if bmi < 16:
        pr = ""
    elif 16 <= bmi < 18.5:
        pr = "static/bmic/lw1.jpeg"
    elif 18.5 <= bmi < 25:
        pr = "static/bmic/norm.jpeg"
    elif 25 <= bmi < 30:
        pr = "static/bmic/ow.jpeg"
    elif 30 <= bmi < 35:
        pr = "static/bmic/ob1.jpeg"
    elif 35 <= bmi < 40:
        pr = "static/bmic/ob2.jpeg"
    elif bmi > 40:
        pr = "static/bmic/ob3.jpeg"
    return pr

def ft_to_cm(ft):
    return ft*30.48


def body_fat1(p, q, r):
    # if q>21 and r == 1:
    #     BFP = 1.20 * p + 0.23 * q - 16.2
    # # elif q < 21 and r == 1:
    # #     BFP = 1.51 * p - 0.70 * q - 2.2
    # elif q > 21 and r == 2:
    #     BFP = 1.20 * p + 0.23 * q - 5.4
    # # elif q < 21 and r == 2:
    # #     BFP = 1.51 * p - 0.70 * q + 1.4

    bfp = -44.988 + (0.503 * q) + (10.689 * r) + (3.172 * p) - (0.026 * p**2) + (0.181 * p * r) - (
                0.02 * p * q) - (0.005 * p**2 * r) + (0.00021 * p**2 * q)
    x =  str(round(bfp, 2))

    return x


def calorieaw(i, j, k, p, gen):
    cal = 0
    if gen == 0:
        cal = (10 * j + 6.25 * k - 5 * i + 5)
    elif gen == 1:
        cal = (10 * j + 6.25 * k - 5 * i - 161)

    if p == 1:
        cal = cal*1.2
    elif p == 2:
        cal = cal*1.4
    elif p == 3:
        cal = cal*1.6
    elif p == 4:
        cal = cal*1.75
    elif p == 5:
        cal = cal*2
    elif p == 6:
        cal = cal * 2.3
    print("To maintain your present weight your calorie intake should be:- ", round(cal, 2))
    return cal

def ideal_w(h1,h2,w,g):
# g=int(input("Enter your gender 0-male 1-female"))
# h1=int(input("Enter your height in feet "))
# h2=int(input("Enter your height in inches "))
# w=int(input("Enter your weight in kg "))


    if h1>=5:
        if g==0:
            dm=50
            a=h2*2.3
            dm=dm+a
            print("Your ideal weight is",dm)
            
            if w<dm:
                b=dm-w
                lg = "You have to gain "+str(round(b,1))+" kg"
            elif w>dm:
                b=w-dm
                lg = "You have to loose "+str(round(b,1))+" kg"
            
        elif g==1:
            dm=45.5
            a=h2*2.3
            dm=dm+a
            print("Your ideal weight is",dm)
            if w<dm:
                b=dm-w
                lg = "You have to gain "+str(round(b,1))+" kg"
            elif w>dm:
                b=w-dm
                lg = "You have to loose "+str(round(b,1))+" kg"
    else:
            print("The calculations are only accurate for those who are at least 153 cm (5 ft) tall.")
            dm = "The calculations are only accurate for those who are at least 153 cm (5 ft) tall."
    return {'dm':dm,'lg':lg}


def ideal_wmax(h):
    if h>=5:
        maxi = 24.9 * (h**2)/10
        print("Your maximum weight should be", round(maxi))
    else:
        maxi= 0
    return maxi

def ideal_wmin(h):
    if h>=5:
        mini = 18.5 * (h**2)/10
        print("Your minimum weight should be", round(mini))
    else:
        mini = 0
    return mini


def ideal_image(g,w,e,f):   #e=max weight f=min w
    pr =""
    if g == 0:
        if w<f:
            pr = "static/iwi/thinb.jpeg"
        elif w>e:
            pr = "static/iwi/fatb.jpeg"
        else:
            pr = "static/iwi/norb.jpeg"
    elif g == 1:
        if w<f:
            pr = "static/iwi/thing.jpeg"
        elif w>e:
            pr = "static/iwi/fatg.jpeg"
        else:
            pr = "static/iwi/norg.jpeg"
    print(g)
    print(w)
    print(e)
    print(f)
    return pr  
    


    # if im < 16:
    #     pr = ""
    # elif 16 <= im < 18.5:
    #     pr = "static/bmic/lw1.jpeg"
    # elif 18.5 <= im < 25:
    #     pr = "static/bmic/norm.jpeg"
    # elif 25 <= im < 30:
    #     pr = "static/bmic/ow.jpeg"
    # elif 30 <= im < 35:
    #     pr = "static/bmic/ob1.jpeg"
    # elif 35 <= im < 40:
    #     pr = "static/bmic/ob2.jpeg"
    # elif im > 40:
    #     pr = "static/bmic/ob3.jpeg"
    # return pr

# def main():
#     hi = float(input("Enter your height in feet:- "))
#     wi = float(input("Enter your weight in kilogram:- "))
#     age = int(input("Enter your age:- "))
#     gen = int(input("Gender:- (0) Male (1) Female "))
#     print("Physical Activity:- \n(1)Sedentary lifestyle (little or no exercise)\n 
#(2)Slightly active lifestyle (light exercise or sports 1-2 days/week)\n 
#(3)Moderately active lifestyle (moderate exercise or sports 2-3 days/week) 
#\n(4)Very active lifestyle (hard exercise or sports 4-5 days/week)\n 
#(5)Extra active lifestyle (very hard exercise, physical job or sports 6-7 days/week)\n
#(6)Professional athlete ")
#     pa = int(input())
#     x = bmi_func(ft_to_cm(hi), wi)
#     y = body_fat(x, age, gen)
#     z = calorie(age, wi, ft_to_cm(hi), pa, gen)
#     w = ideal_w(ft_to_cm(hi))


# if __name__ == "__main__":
#     main()
