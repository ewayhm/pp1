#zad.28

values = [61,47,37,32,26,26,14,14,9,7]
languages = ['Java', 'Python', 'JavaScript', 'C++', 'C#','Ruby','Perl','PHP','C','Android']

output = dict(zip(languages, values))
for key in output:
    print("{:>10}:{}{}k".format(key,"#"*output[key],
             output[key]))








