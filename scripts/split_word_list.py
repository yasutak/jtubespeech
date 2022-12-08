import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Split word list into multiple files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text_path", type=str, help="path for word list file")
    parser.add_argument("num_files", type=int, help="number of files to split")

    return parser.parse_args(sys.argv[1:])


def split_word_list(text_path, num_files):
    with open(text_path, "r") as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_lines_per_file = num_lines // num_files
        if not os.path.exists("splitted_files"):
            os.mkdir("splitted_files")
        for i in range(num_files):
            if i == num_files - 1:
                lines_to_write = lines[i * num_lines_per_file :]
            else:
                lines_to_write = lines[i * num_lines_per_file : (i + 1) * num_lines_per_file]
            word_list_name = os.path.basename(text_path).split(".")[0]
            file_name = os.path.join("splitted_files", f"{word_list_name}_{i}.txt")
            with open(file_name, "w") as f_out:
                f_out.writelines(lines_to_write)


if __name__ == "__main__":
    args = parse_args()
    split_word_list(args.text_path, args.num_files)
