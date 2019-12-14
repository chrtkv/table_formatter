#! /usr/bin/env python3
import sys


def find_column_size(links, columns):
    '''
    find divisible without remainder to calculate
    max quantity with equal-size columns
    '''
    links_quantity = len(links)

    def find_divisible(links_quantity):
        if links_quantity % columns == 0:
            return links_quantity
        return find_divisible(links_quantity + 1)
    return int(find_divisible(links_quantity) / columns)


def sort_by_description(links):
    # for link in list(links):
    #     print(link)
    '''
    alphabeticaly sort links by description
    '''
    return sorted(links, key=lambda x: x[1].strip('"'))


def divide_description(links):
    '''
    divide url and description, remove new lines
    '''
    def cb(link):
        return link.rstrip('\n').split(' ', maxsplit=1)
    return map(cb, links)


def make_rows(links, column_size):
    '''
    links must be sorted
    make lines for table rows
    '''
    def row_number(link):
        index = links.index(link)
        return index % column_size

    rows_list = []
    for i in range(column_size):
        rows_list.append([])

    for link in links:
        rows_list[row_number(link)] += [link]

    return rows_list


def create_table(rows):
    def cb(row):
        result = ''
        for link in row:
            result += "(({} {} ))|".format(link[0], link[1])
        return result
    markuped_links = map(cb, rows)

    def cb2(row):
        return "||{}|".format(row)
    markuped_rows = '\n'.join(map(cb2, markuped_links))

    return "#||\n{}\n||#".format(markuped_rows)


def main(links, columns):
    column_size = find_column_size(links, columns)
    links_list = divide_description(links)
    sorted_list = sort_by_description(links_list)
    rows = make_rows(sorted_list, column_size)
    return create_table(rows)


if __name__ == '__main__':
    columns = int(sys.argv[1])
    with open('links.txt', 'r') as file:
        links = file.readlines()
    with open('table.txt', 'w') as file:
        file.write(main(links, columns))
