NAME = day01
CC = cc
CFLAGS = -Wall -Wextra -Werror

SOURCES = main.c

OBJECTS = $(SOURCES:.c=.o)

libft_dir := ../../libft
libft := $(libft_dir)/libft.a

INCLUDES = -I./include -I$(libft_dir)

all: $(NAME)

$(NAME): $(OBJECTS) # $(libft)
	cc $(CFLAGS) $(INCLUDES) $(OBJECTS) -L$(libft_dir) -lft -o $@

# $(libft):
# 	$(MAKE) -C $(libft_dir)

%.o: %.c
	cc $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(OBJECTS)
#	make -C $(libft_dir) clean

fclean: clean
	rm -f $(NAME)
#	make -C $(libft_dir) fclean

re: fclean all

.PHONY: all clean fclean re