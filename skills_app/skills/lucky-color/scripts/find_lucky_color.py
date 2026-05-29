import argparse
def find_lucky_color(age:int,gender:str):
    if age >18 and gender=="male":
        return "BLUE"
    else:
        return "PINK"
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--age", type=int)
  parser.add_argument("--gender", type=str)
  args = parser.parse_args()
  print(find_lucky_color(args.age,args.gender))