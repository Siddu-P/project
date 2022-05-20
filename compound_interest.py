def compound_interest(p,t,r):#amt=p(1+r/100)^t #CI=amt-p                  
    amt=p*(pow((1+r/100),t))
    ci=amt-p
    print(ci)
compound_interest(10000,5,10.25)