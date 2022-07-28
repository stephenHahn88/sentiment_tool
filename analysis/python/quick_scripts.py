from pprint import pprint

def main():
    with open("../annotations/valence_annotation/op18_no1_mov4.csv", "r") as f:
        lines = [line for line in f.readlines()[0].split(",\\n") if line]
    pprint(lines)

    with open("../annotations/valence_annotation/op18_no1_mov4_clean.csv", "w") as f:
        for line in lines:
            time, category = line.split(" : ")
            f.write(f"{time},{category}\n")




if __name__ == "__main__":
    main()