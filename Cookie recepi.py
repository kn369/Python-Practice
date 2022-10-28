#this program calculates no. of cups of sugar , butter and flour to make given no. of cookies

no_cookies=int(input('Enter the number of cookies you want to make :'))
SugarCups=(1.5/48)*no_cookies
ButterCups=(1/48)*no_cookies
FlourCups=(2.75/48)*no_cookies
print('You will require',SugarCups,'cups of sugar')
print('You will require',ButterCups,'cups of butter')
print('You will require',FlourCups,'cups of flour')
