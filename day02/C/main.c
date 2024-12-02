#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../../libft/libft.h"

int *split_to_int_array(char **split, int skip) {
    int count = 0;
    while (split[count])
        count++;
    int *array = ft_calloc(count + 1, sizeof(int));
    int i = -1;
    int k = -1;
    while(split[++i]) {
        if (i != skip)
            array[++k] = ft_atoi(split[i]);
    }
    i = -1;
    printf("Skip is %d. Array is ", skip);
    while(array[++i])
        printf("%d-", array[i]);
    printf("\n");
    return (array);
}

int check_ascending_damp(char **split)
{
    int *array;
    int i;
    int k;
    int count = 0;
    int flag;

    while (split[count])
        count++;
    k = 0;
    while (k < count)
    {
        flag = 0;
        i = 0;
        array = split_to_int_array(split, k);
        while(array[i] && array[i + 1]) {
            if (!(array[i + 1] > array[i] && array[i + 1] - array[i] <= 3))
                flag = 1;;
            i++;
        }
        if (!flag)
            return (1);
        free_void((void **)&array, NULL);
        k++;
    }
    return (0);
}

int check_descending_damp(char **split)
{
    int *array;
    int i;
    int k;
    int count = 0;
    int flag;

    while (split[count])
        count++;
    k = 0;
    while (k < count)
    {
        flag = 0;
        i = 0;
        array = split_to_int_array(split, k);
        while(array[i] && array[i + 1]) {
            if (!(array[i] > array[i + 1] && array[i] - array[i + 1] <= 3))
                flag = 1;
            i++;
        }
        if (!flag)
            return (1);
        free_void((void **)&array, NULL);
        k++;
    }
    return (0);
}

int check_ascending(int *array)
{
    int i;

    i = 0;
    while(array[i] && array[i + 1]) {
        if (!(array[i + 1] > array[i] && array[i + 1] - array[i] <= 3))
            return (0);
        i++;
    }
    return (1);
}

int check_descending(int *array)
{
    int i;

    i = 0;
    while(array[i] && array[i + 1]) {
        if (!(array[i] > array[i + 1] && array[i] - array[i + 1] <= 3))
            return (0) ;
        i++;
    }
    return (1);
}

int main(void) {
    int     fd;
    char    *filename = "input.txt";
    char    *line;
    int     counter = 0;
    int     dampener_counter = 0;

    fd = open(filename, O_RDONLY);

    while ((line = get_next_line(fd))) {
        char    **split = ft_split(line, ' ');
        int     *array = split_to_int_array(split, -1);
        if (check_ascending(array) || check_descending(array))
            counter++;
        if (check_ascending_damp(split) || check_descending_damp(split))
            dampener_counter++;
        free_void((void **)&line, NULL);
        free_void((void **)&array, NULL);
        free_2d_array((void ***)&split);
    }
    printf("%d reports are safe without the Problem Dampener\n", counter);
    printf("%d reports are safe with the Problem Dampener\n", dampener_counter);
    close(fd);
    return 0;
}