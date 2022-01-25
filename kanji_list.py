#! python3
# -*- coding: utf-8 -*-

import csv
import codecs

with codecs.open('all_jlpt_joyo_news_2.csv', 'r', 'utf-8') as csv_file1: # JLPT
    csv_reader1 = csv.reader(csv_file1)
    my_list1 = list(csv_reader1)

    with codecs.open('leftovers.csv', 'w', 'utf-8') as new_file: # New List
        csv_writer = csv.writer(new_file)

        with codecs.open('extra.csv', 'r', 'utf-8') as csv_file2: # Newspaper
            csv_reader2 = csv.reader(csv_file2)
            my_list2 = list(csv_reader2)

            for line in my_list2:
                if line in my_list1:
                    pass
                else:
                    csv_writer.writerow(line)
