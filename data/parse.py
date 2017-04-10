"""
Parse iob files
"""
import sys

def main():
    """ Main function """
    file_name = sys.argv[1]
    file = open(file_name, 'r')
    data = []

    for line in file:

        data.append(line.split())

    file.close()

    label = []
    seq_in = []
    seq_out = []

    for line in data:

        label.append(line[-1])

        eos_idx = line.index('EOS')

        seq_in.append(' '.join(line[1:eos_idx]))
        seq_out.append(' '.join(line[eos_idx+2:-1]))

    train_label_file = open('./ATIS/train/train.label', 'w')
    valid_label_file = open('./ATIS/valid/valid.label', 'w')
    test_label_file = open('./ATIS/test/test.label', 'w')

    train_label_file.write('\n'.join(label[0:3200]))
    valid_label_file.write('\n'.join(label[3200:4000]))
    test_label_file.write('\n'.join(label[4000:]))

    train_seq_in_file = open('./ATIS/train/train.seq.in', 'w')
    valid_seq_in_file = open('./ATIS/valid/valid.seq.in', 'w')
    test_seq_in_file = open('./ATIS/test/test.seq.in', 'w')

    train_seq_in_file.write('\n'.join(seq_in[0:3200]))
    valid_seq_in_file.write('\n'.join(seq_in[3200:4000]))
    test_seq_in_file.write('\n'.join(seq_in[4000:]))

    train_seq_out_file = open('./ATIS/train/train.seq.out', 'w')
    valid_seq_out_file = open('./ATIS/valid/valid.seq.out', 'w')
    test_seq_out_file = open('./ATIS/test/test.seq.out', 'w')

    train_seq_out_file.write('\n'.join(seq_out[0:3200]))
    valid_seq_out_file.write('\n'.join(seq_out[3200:4000]))
    test_seq_out_file.write('\n'.join(seq_out[4000:]))

if __name__ == '__main__':

    main()
