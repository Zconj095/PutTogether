import time

fin = open("Language_Early_Stage.py", "r+")
lines = fin.readlines()
main_statement = lines[0].strip()
syntax = main_statement.split(",")

e = time.time()

if syntax[0] == "CREATE" and syntax[1] == "NEW" and syntax[2] == "CLASS:":
  # We know its a class creation startement now.
  with open("tempRunner.py", "w+") as fout:
    fout.write("from dataclasses import dataclass\n@dataclass\n")
    variables = [n.strip().split('"') for n in lines[3:-1]]
    for n in range(len(variables)):
      fout.write("class ")
      fout.write(f"{(variables[n][-1] + variables[n][-2]).replace(',', '')}:\n  pass\n")

    fout.write("class ")
  temp = open('tempRunner.py', 'r')
  temp_lines = temp.readlines()
  temp.close()
  temp_lines = [x for x in temp_lines if x != '  pass\n']

  name = lines[1].strip().split('"')[1].replace(".", "_")
  with open("tempRunner.py", "a+") as fout:
    fout.write(f"{name}:\n")
    fout.write(f'''  """Classs definition created by EdgeLore\n     Creation Time: {time.time() - e:.6f}"""\n''')
    for n in range(len(variables)):
      fout.write(f"  var{n}: {temp_lines[n+2].split('class')[1].split(':')[0].replace(' ', '')}\n")