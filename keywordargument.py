# KEYWORD ARGUMENT = an argument preceed by an identifier 
                     #helps with redability 
                     # order of argument is doesn't matter


def hello (greeting,title,first,last):
    print(f"{greeting} {title} {first} {last}")

print(hello(greeting="hello",title="Mr",first="John",last="Doe"))


def get_number(country_code,area_code,first,last):
    print(f"{country_code}-{area_code}-{first}-{last}")

print(get_number(country_code=1,area_code=123,first=456,last=7890))