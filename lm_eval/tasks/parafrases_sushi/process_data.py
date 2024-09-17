def process_data():
    with open("data.txt", "r") as f:
        data = f.readlines()

    with open("data.csv", "w") as f:
        f.write("sentence1,sentence2,label\n")
        for line in data:
            line = line.strip()
            if line:
                sentence1, sentence2, label = line.split("\t")
                f.write(f"{sentence1},{sentence2},{label}\n")


if __name__ == "__main__":
    process_data()
