


def make_name_sentence_sensitive():
  x = input('What is your name?' + '\n' + "Please begin with 'My name is' and then enter name:"+ '\n')
  
  replace_text = x.replace(x[14:], 'xxxx')
  print(replace_text)
  
make_name_sentence_sensitive()
