import argparse

def update_config(input_file, config_file):
    with open(config_file, 'r') as f:
        config_lines = f.readlines()

    with open(input_file, 'r') as f:
        input_lines = f.readlines()

    input_sets = []
    current_set = {}
    for line in input_lines:
        if line.strip() == '*':
            if current_set:
                input_sets.append(current_set)
                current_set = {}
        elif line.strip():
            key, value = line.strip().split('=')
            current_set[key.strip()] = value.strip()
    if current_set:
        input_sets.append(current_set)

    for i, input_dict in enumerate(input_sets):
        output_lines = []
        for line in config_lines:
            for key in input_dict:
                if line.strip().startswith(key):
                    key_end_index = line.index('=')
                    line = line[:key_end_index] + '= ' + input_dict[key] + '\n'
            output_lines.append(line)

        with open(f'output_{i+1}.txt', 'w') as f:
            f.writelines(output_lines)

def main():
    parser = argparse.ArgumentParser(description='Update config file based on input file.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--config', help='Config file name', required=True)

    args = parser.parse_args()

    update_config(args.input, args.config)

if __name__ == "__main__":
    main()
