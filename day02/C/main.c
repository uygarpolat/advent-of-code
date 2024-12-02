#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../../libft/libft.h"

int main(void) {
    int     fd;
    char    *filename = "input.txt";
    char    *line;
    int     counter = 0;

    fd = open(filename, O_RDONLY);

    while ((line = get_next_line(fd))) {
        int i = 0;
        char **split = ft_split(line, ' ');
        while(split[i] && split[i + 1]) {
            if (ft_atoi(split[i + 1]) > ft_atoi(split[i]) && ft_atoi(split[i + 1]) - ft_atoi(split[i]) <= 3) {
                i++;
                continue ;
            }
            else {
                counter--;
                break ;
            }
            i++;
        }
        counter++;
        i = 0;
        while(split[i] && split[i + 1]) {
            if (ft_atoi(split[i + 1]) < ft_atoi(split[i]) && ft_atoi(split[i]) - ft_atoi(split[i + 1]) <= 3) {
                i++;
                continue ;
            }
            else {
                counter--;
                break ;
            }
            i++;
        }
        counter++;
        free_void((void **)&line, NULL);
        free_2d_array((void ***)&split);
    }
    close(fd);
    printf("Counter is %d\n", counter);
    return 0;
}