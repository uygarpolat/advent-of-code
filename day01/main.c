#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "libft/libft.h"

void    bubble_sort(int *list)
{
    int list_size = 0;

    while (list[list_size])
        list_size++;
    int i = -1;
    while (++i < list_size - 1)
    {
        int k = 0;
        while (k < list_size - 1 - i) 
        {
            if (list[k] > list[k + 1])
            {
                int c = list[k];
                list[k] = list[k + 1];
                list[k + 1] = c;
            }
            k++;
        }
    }
}

void    print_total_distance(int *list1, int *list2, int list_size) {
    long total_distance = 0;
    for (int k = 0; k < list_size; k++)
        total_distance += abs(list1[k] - list2[k]);
    printf("total distance is %ld\n", total_distance);
}

int get_list_size (char *filename) {
    int     list_size = 0;
    int     fd;
    char    *line;

    fd = open(filename, O_RDONLY);
    if (fd == -1)
        return -1;

    while ((line = get_next_line(fd))) {
        list_size++;
        free_void((void **)&line, NULL);
    }
    close(fd);
    return list_size;
}

void    print_similarity_score(int *list1, int *list2, int list_size) {

    long similarity_score = 0;
    int i = 0;
    while (i < list_size) {
        int k = 0;
        while (k < list_size) {
            if (list1[i] == list2[k])
                similarity_score += list1[i];
            k++;
        }
        i++;
    }
    printf("similarity score is %ld\n", similarity_score);
}

int main(void) {
    int     *list1;
    int     *list2;
    char    *line;
    int     fd;
    int     list_size;
    int     i = 0;
    char    *filename = "input.txt";

    list_size = get_list_size(filename);
    if (list_size == -1)
        return 1;

    list1 = ft_calloc((list_size + 1), sizeof(int));
    if (list1 == NULL)
        return 1;
    list2 = ft_calloc((list_size + 1), sizeof(int));
    if (list2 == NULL)
        return (free_void((void **)&list1, NULL), 1);

    fd = open(filename, O_RDONLY);
    if (fd == -1 ) {
        free_void((void **)&list1, NULL);
        free_void((void **)&list2, NULL);
        return 1;
    }

    while ((line = get_next_line(fd)))
    {
        char **split_line = ft_split(line, ' ');
        list1[i] = ft_atoi(split_line[0]);
        list2[i] = ft_atoi(split_line[1]);
        i++;
        free_2d_array((void ***)&split_line);
        free_void((void **)&line, NULL);
    }
    close(fd);

    printf(" Pre-sort ");
    print_total_distance(list1, list2, list_size);
    printf(" Pre-sort ");
    print_similarity_score(list1, list2, list_size);

    bubble_sort(list1);
    bubble_sort(list2);

    printf("Post-sort ");
    print_total_distance(list1, list2, list_size);
    printf("Post-sort ");
    print_similarity_score(list1, list2, list_size);

    free_void((void **)&list1, NULL);
    free_void((void **)&list2, NULL);

    return 0;
}