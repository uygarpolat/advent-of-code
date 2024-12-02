#include "libft.h"
#include <string.h>
#include <stdio.h>
#include <ctype.h>

void tester_ft_isalpha()
{
	printf("Test results for ft_isalpha:\n");
	printf("%d-%d", isalpha('A'), ft_isalpha('A'));
}

void tester_ft_isdigit()
{
		printf("Test results for ft_isdigit:\n");
	printf("%d-%d\n", isdigit('2'), ft_isdigit('2'));
}

void tester_ft_isalnum()
{
	printf("Test results for ft_isalnum:\n");
	printf("%d-%d\n", isalnum('A'), ft_isalnum('A'));
	printf("%d-%d\n", isalnum('Z'), ft_isalnum('Z'));
	printf("%d-%d\n", isalnum('a'), ft_isalnum('a'));
	printf("%d-%d\n", isalnum('z'), ft_isalnum('z'));
	printf("%d-%d\n", isalnum('0'), ft_isalnum('0'));
	printf("%d-%d\n", isalnum('9'), ft_isalnum('9'));
	printf("%d-%d\n", isalnum('M'), ft_isalnum('M'));
	printf("%d-%d\n", isalnum('m'), ft_isalnum('m'));
	printf("%d-%d\n", isalnum('&'), ft_isalnum('&'));
	printf("%d-%d\n", isalnum('\n'), ft_isalnum('\n'));
	printf("\n----------\n");
}

void tester_ft_isascii()
{
		printf("Test results for ft_isascii:\n");
	printf("%d-%d", isascii('\n'), ft_isascii('\n'));
}

void tester_ft_isprint()
{
			printf("Test results for ft_isprint\n");
		int	i;

	i = 0;
	while (i <= 1000)
	{
		if (isprint(i) != ft_isprint(i))
		{
			printf("ft_isprint doesn't work because of ASCII char #%d.\n", i);
			return ;
		}
		i++;
	}
	printf("ft_isprint works!\n");
}

void tester_ft_strlen()
{
		printf("Test results for ft_strlen:\n");
	printf("%zu|%zu", strlen("Hello!"), ft_strlen("Hello!"));
}

void tester_ft_memset()
{
	
}

void tester_ft_bzero()
{
	
}

void tester_ft_memcpy()
{
		printf("Test results for ft_memcpy:\n");
	int		intsrc;
	int		intdest;
	char	charsrc[] = "Helloworld";
	char	chardest[20];

	intsrc = 123456;
	ft_memcpy(&intdest, &intsrc, sizeof(int));
	printf("Dest integer: %d\n", intdest);
	ft_memcpy(chardest, charsrc, sizeof(charsrc));
	printf("Dest string: %s\n", chardest);

}

void tester_ft_memmove()
{
	
}

void tester_ft_strlcpy()
{
	printf("Test results for ft_strlcpy:\n");
		char			source1[6] = "Hello";
	char			dest1[6];
	size_t			len1;
	char			source2[6] = "Hello";
	char			dest2[6];
	size_t			len2;
	size_t			size1;
	unsigned int	size2;

	size1 = 6;
	size2 = 6;
	len1 = strlcpy(dest1, source1, size1);
	len2 = ft_strlcpy(dest2, source2, size2);
	printf("for    strlcpy, dest is %s and return value is %zu\n", dest1, len1);
	printf("for ft_strlcpy, dest is %s and return value is %zu\n", dest2, len2);

	char src[] = "coucou";
	char dest3[10]; memset(dest3, 'A', 10);
	printf("%d\n", ft_strlcpy(dest3, src, 0) == strlen(src) && dest3[0] == 'A');
	printf("%s\n", dest3);

}

void tester_ft_strlcat()
{
	printf("Test results for ft_strlcat:\n");
		char	str1[15] = "Hello ";
	char	str2[15] = "Hello ";

	printf("%lu\n", strlcat(str1, "World!", sizeof(str1)));
	printf("%s\n", str1);
	printf("%zu\n", ft_strlcat(str2, "World!", sizeof(str2)));
	printf("%s\n", str2);

	char	str3[7] = "Hello ";
	char	str4[7] = "Hello ";

	printf("%lu\n", strlcat(str3, "World!", 7));
	printf("%s\n", str3);
	printf("%zu\n", ft_strlcat(str4, "World!", 7));
	printf("%s\n", str4);

	char	str5[1] = "";
	char	str6[1] = "";

	printf("%lu\n", strlcat(str5, "World!", sizeof(str5)));
	printf("%s\n", str5);
	printf("%zu\n", ft_strlcat(str6, "World!", sizeof(str6)));
	printf("%s\n", str6);

	char	str7[7] = "Hello ";
	char	str8[7] = "Hello ";

	printf("%lu\n", strlcat(str7, "Worldddd!", 2));
	printf("%s\n", str7);
	printf("%zu\n", ft_strlcat(str8, "Worldddd!", 2));
	printf("%s\n", str8);

	char	dest[50] = "Whataworld";
	char	dest_ft[50] = "Whataworld";
	char	src[50] = "Hello, ";
	int		buf;

	buf = 2;
	printf("    strlcat-> %lu, %s\n", strlcat(dest, src, buf), dest);
	printf("ft_strlcat -> %zu, %s", ft_strlcat(dest_ft, src, buf), dest_ft);
}

void tester_ft_toupper()
{
	printf("Test results for ft_toupper:\n");
	printf("%c-%c\n", toupper('d'), ft_toupper('d'));	
}

void tester_ft_tolower()
{
	printf("Test results for ft_tolower:\n");
	printf("%c-%c\n", tolower('D'), ft_tolower('D'));
}

void tester_ft_strchr()
{
	printf("Test results for ft_strchr:\n");
		char s[] = "tripouille";
	printf("%s|%s\n", strchr("abc", '\0'), ft_strchr("abc", '\0'));
	printf("%d|", strchr(s, 't' + 512) == s);
	printf("%d\n", ft_strchr(s, 't' + 512) == s);
	printf("%c\n", 't' + 512);
	printf("%s\n", ft_strchr("teste", '\0'));
}

void tester_ft_strrchr()
{
	printf("Test results for ft_strrchr:\n");
	printf("   strrchr returns: %s\nft_strrchr returns: %s\n",
		strrchr("abcdefgcdef", 'a'),ft_strrchr("abcdefgcdef", 'a'));	
}

void tester_ft_strncmp()
{
	printf("Test results for ft_strncmp:\n");
		printf("%d|%d\n", strncmp("Whynot", "Why",
		6), ft_strncmp("Whynot", "Why", 6));
	printf("%d|%d\n",strncmp("test\200", "test\0", 6),
		ft_strncmp("test\200", "test\0", 6));

}

void tester_ft_memchr()
{
	printf("Test results for ft_memchr:\n");
	int tab[7] = {-49, 49, 1, -1, 0, -2, 2};
    printf("%s|", (char *)memchr(tab, -1, 7));
    printf("%s\n", (char *)ft_memchr(tab, -1, 7));	
}

void tester_ft_memcmp()
{
	printf("Test results for ft_memcmp:\n");
	char s[] = {-128, 0, 127, 0};
	char s2[] = {0, 0, 127, 0};
	printf("%d|", memcmp(s, s2, 1));
	printf("%d\n", ft_memcmp(s, s2, 1));
	
	printf("%d|", memcmp(s2, s, 1));
	printf("%d\n", ft_memcmp(s2, s, 1));	
}

void tester_ft_strnstr()
{
	printf("Test results for ft_strnstr:\n");
	printf("%s\n", ft_strnstr("12345678901234567890", "89", 8));
	printf("%s\n", strnstr("lorem ipsum dolor sit amet", "dolor", 0));
	printf("%s\n", ft_strnstr("lorem ipsum dolor sit amet", "dolor", 0));	
}

void tester_ft_atoi(int argc, char**argv)
{
	printf("Test results for ft_atoi:\n");
	if (argc == 2)
	{	
		printf("   atoi returns: %d\nft_atoi returns: %d\n",
			atoi(argv[1]), ft_atoi(argv[1]));
	}	
}

void tester_ft_calloc()
{
	printf("Test results for ft_calloc:\n");
    // Define the number of elements and size of each element
    size_t num_elements = 5;
    size_t element_size = sizeof(int);

    // Allocate memory using ft_calloc
    int *arr = ft_calloc(num_elements, element_size);
    if (arr == NULL) {
        printf("Memory allocation failed\n");
    }

    // Verify that all fields are populated by zeroes
    int all_zeroes = 1;
    for (size_t i = 0; i < num_elements; ++i) {
        if (arr[i] != 0) {
            all_zeroes = 0;
            break;
        }
    }

    // Output the result
    if (all_zeroes) {
        printf("All fields are populated by zeroes\n");
    } else {
        printf("Fields are not properly initialized\n");
    }

    // Free the allocated memory
    free(arr);

	
}

void tester_ft_strdup(int argc, char **argv)

{
	printf("Test results for ft_strdup:\n");
	char	*str;
	char	*str_dup;
	char	*ft_str_dup;

	if (argc == 2)
	{
		str = argv[1];
		str_dup = strdup(str);
		ft_str_dup = ft_strdup(str);
		printf("%s-%s\n", strdup(str_dup), ft_strdup(ft_str_dup));
		free(str_dup);
		free(ft_str_dup);
	}	
}

void tester_ft_substr()
{
	printf("Test results for ft_substr:\n");
		printf("%s\n", ft_substr("Hello World!", 15, 11));
	char *s = ft_substr("tripouille", 100, 1);
	printf("%d|", !strcmp(s, ""));
	char *s2 = ft_substr("tripouille", 0, 42000);
	printf("%d\n", !strcmp(s2, "tripouille"));
	printf("%s\n", ft_substr("01234", 10, 10));
}

void tester_ft_strjoin(int argc, char **argv)
{
	printf("Test results for ft_strjoin:\n");
	if (argc == 3)
		printf("%s\n", ft_strjoin(argv[1], argv[2]));
}

void tester_ft_strtrim(int argc, char **argv)
{
	printf("Test results for ft_strtrim:\n");
		if (argc == 3)
			printf("%s\n", ft_strtrim(argv[1], argv[2]));
}

void tester_ft_split(int argc, char **argv)
{
	printf("Test results for ft_split:\n");
	int		i;
	char	**str;

	if (argc == 3)
	{
		str = ft_split(argv[1], argv[2][0]);
		i = 0;
		while (str[i])
		{
			printf("Word %d: %s\n", i + 1, str[i]);
			i++;
		}
	}
}

void tester_ft_itoa()
{
	printf("Test results for ft_itoa:\n");
	char	*str;
	int		nbr;

	nbr = 10000034;
	str = ft_itoa(nbr);
	printf("%s\n", ft_itoa(nbr));
	free(str);

	
}
char	increase_char(unsigned int i, char c)
{
	(void)i;
	return (c + 1);
}
void tester_ft_strmapi()
{
	printf("Test results for ft_strmapi:\n");
		char	input[] = "Hello, World!";
	char	*result;
	
	result = ft_strmapi(input, &increase_char);

	if (result == NULL)
		return ;
	printf("Original string: %s\n", input);
	printf("Modified string: %s\n", result);
	free(result);

}
	void	ft_write(unsigned int i, char *str)
	{
		(void)i;
		write(1, str, 1);
	}
void tester_ft_striteri(int argc, char **argv)
{
	printf("Test results for ft_striteri:\n");
	if (argc == 2)
	{
		ft_striteri(argv[1], ft_write);
	}
}

void tester_ft_putchar_fd()
{
	
}

void tester_ft_putstr_fd(int argc, char **argv)
{
	printf("Test results for ft_putstr_fd:\n");
	if (argc == 2)
		ft_putstr_fd(argv[1], 1);	
}

void tester_ft_putendl_fd(int argc, char **argv)
{
	printf("Test results for ft_putendl_fd\n");
	if (argc == 2)
		ft_putendl_fd(argv[1], 1);

}

void tester_ft_putnbr_fd()
{
	printf("Test results for ft_putnbr_fd:\n");
	ft_putnbr_fd(-57, 1);	
}

void tester_ft_lstnew()
{
	printf("Test results for ft_lstnew:\n");
	t_list *mylist = ft_lstnew("context");
	char* str = (char *)(mylist->content);
	printf("%s\n", str);	
}

void tester_ft_lstadd_front()
{
	printf("Test results for ft_lstadd_front:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew("context");
	t_list *mylist3 = ft_lstnew("out of ");
	mylist = &mylist2;
	ft_lstadd_front(mylist, mylist3);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	printf("%s", str);
	printf("%s\n", str2);	
}

void tester_ft_lstsize()
{
	printf("Test results for ft_lstsize:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew("out of ");
	t_list *mylist3 = ft_lstnew("context ");
	t_list *mylist4 = ft_lstnew("quotes");
	mylist = &mylist4;
	ft_lstadd_front(mylist, mylist3);
	ft_lstadd_front(mylist, mylist2);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	char *str3 = (char *) (*mylist)->next->next->content;
	printf("%s", str);
	printf("%s", str2);
	printf("%s\n", str3);
	(*mylist)->next->next->next = NULL;
	printf("Size of list is : %d\n", ft_lstsize(*mylist));	
}

void tester_ft_lstlast()
{
	printf("Test results for ft_lstlast:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew("out of ");
	t_list *mylist3 = ft_lstnew("context ");
	t_list *mylist4 = ft_lstnew("quotes");
	mylist = &mylist4;
	ft_lstadd_front(mylist, mylist3);
	ft_lstadd_front(mylist, mylist2);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	char *str3 = (char *) (*mylist)->next->next->content;
	printf("%s", str);
	printf("%s", str2);
	printf("%s\n", str3);
	(*mylist)->next->next->next = NULL;
	printf("Size of list is: %d\n", ft_lstsize(*mylist));
	printf("Last element's content is: quotes\n       ft_lstlast returns: %s\n", (char *) ft_lstlast(*mylist)->content);	
}

void tester_ft_lstadd_back()
{
	printf("Test results for ft_lstadd_back:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew("out of ");
	t_list *mylist3 = ft_lstnew("context ");
	t_list *mylist4 = ft_lstnew("quotes");
	t_list *mylist5 = ft_lstnew("mislead");
	mylist = &mylist4;
	ft_lstadd_front(mylist, mylist3);
	ft_lstadd_front(mylist, mylist2);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	char *str3 = (char *) (*mylist)->next->next->content;
	printf("%s", str);
	printf("%s", str2);
	printf("%s\n", str3);
	(*mylist)->next->next->next = NULL;
	printf("Size of list is: %d\n", ft_lstsize(*mylist));
	printf("Last element's content is: quotes\n       ft_lstlast returns: %s\n", (char *) ft_lstlast(*mylist)->content);
	ft_lstadd_back(mylist, mylist5);
	char *str4 = (char *) (*mylist)->next->next->next->content;
	printf("%s\n", str4);	
}

static void	del(void* content)
	{	
		free(content);
	}
void tester_ft_lstdelone()
{
	printf("Test results for ft_lstdelone:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew(ft_strdup("out of "));
	t_list *mylist3 = ft_lstnew(ft_strdup("context "));
	t_list *mylist4 = ft_lstnew(ft_strdup("quotes"));
	t_list *mylist5 = ft_lstnew(ft_strdup("mislead"));
	mylist = &mylist4;
	ft_lstadd_front(mylist, mylist3);
	ft_lstadd_front(mylist, mylist2);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	char *str3 = (char *) (*mylist)->next->next->content;
	printf("%s", str);
	printf("%s", str2);
	printf("%s\n", str3);
	(*mylist)->next->next->next = NULL;
	printf("Size of list is: %d\n", ft_lstsize(*mylist));
	printf("Last element's content is: quotes\n       ft_lstlast returns: %s\n", (char *) ft_lstlast(*mylist)->content);
	ft_lstadd_back(mylist, mylist5);
	char *str4 = (char *) (*mylist)->next->next->next->content;
	printf("%s\n", str4);
	ft_lstdelone((*mylist)->next, &del);	
}
void tester_ft_lstclear()
{
	printf("Test results for ft_lstclear:\n");
	t_list **mylist;
	t_list *mylist2 = ft_lstnew(ft_strdup("out of "));
	t_list *mylist3 = ft_lstnew(ft_strdup("context "));
	t_list *mylist4 = ft_lstnew(ft_strdup("quotes"));
	t_list *mylist5 = ft_lstnew(ft_strdup("mislead"));
	mylist = &mylist4;
	ft_lstadd_front(mylist, mylist3);
	ft_lstadd_front(mylist, mylist2);
	char *str = (char *) (*mylist)->content;
	char *str2 = (char *) (*mylist)->next->content;
	char *str3 = (char *) (*mylist)->next->next->content;
	printf("%s", str);
	printf("%s", str2);
	printf("%s\n", str3);
	(*mylist)->next->next->next = NULL;
	printf("Size of list is: %d\n", ft_lstsize(*mylist));
	printf("Last element's content is: quotes\n       ft_lstlast returns: %s\n", (char *) ft_lstlast(*mylist)->content);
	ft_lstadd_back(mylist, mylist5);
	char *str4 = (char *) (*mylist)->next->next->next->content;
	printf("%s\n", str4);
	//ft_lstdelone((*mylist)->next, &del);
	ft_lstclear(mylist, &del);	
}

void tester_ft_lstiter()
{
	
}

void tester_ft_lstmap()
{
	
}

int main(int argc, char **argv)
{
	tester_ft_isalpha();
	printf("\n-----------------------\n");
	tester_ft_isdigit();
	printf("\n-----------------------\n");
	tester_ft_isalnum();
	printf("\n-----------------------\n");
	tester_ft_isascii();
	printf("\n-----------------------\n");
	tester_ft_isprint();
	printf("\n-----------------------\n");
	tester_ft_strlen();
	printf("\n-----------------------\n");
	tester_ft_memset();
	printf("\n-----------------------\n");
	tester_ft_bzero();
	printf("\n-----------------------\n");
	tester_ft_memcpy();
	printf("\n-----------------------\n");
	tester_ft_memmove();
	printf("\n-----------------------\n");
	tester_ft_strlcpy();
	printf("\n-----------------------\n");
	tester_ft_strlcat();
	printf("\n-----------------------\n");
	tester_ft_toupper();
	printf("\n-----------------------\n");
	tester_ft_tolower();
	printf("\n-----------------------\n");
	tester_ft_strchr();
	printf("\n-----------------------\n");
	tester_ft_strrchr();
	printf("\n-----------------------\n");
	tester_ft_strncmp();
	printf("\n-----------------------\n");
	tester_ft_memchr();
	printf("\n-----------------------\n");
	tester_ft_memcmp();
	printf("\n-----------------------\n");
	tester_ft_strnstr();
	printf("\n-----------------------\n");
	tester_ft_atoi(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_calloc();
	printf("\n-----------------------\n");
	tester_ft_strdup(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_substr();
	printf("\n-----------------------\n");
	tester_ft_strjoin(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_strtrim(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_split(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_itoa();
	printf("\n-----------------------\n");
	tester_ft_strmapi();
	printf("\n-----------------------\n");
	tester_ft_striteri(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_putchar_fd();
	printf("\n-----------------------\n");
	tester_ft_putstr_fd(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_putendl_fd(argc, argv);
	printf("\n-----------------------\n");
	tester_ft_putnbr_fd();
	printf("\n-----------------------\n");
	tester_ft_lstnew();
	printf("\n-----------------------\n");
	tester_ft_lstadd_front();
	printf("\n-----------------------\n");
	tester_ft_lstsize();
	printf("\n-----------------------\n");
	tester_ft_lstlast();
	printf("\n-----------------------\n");
	tester_ft_lstadd_back();
	printf("\n-----------------------\n");
	tester_ft_lstdelone();
	printf("\n-----------------------\n");
	tester_ft_lstclear();
	printf("\n-----------------------\n");
	tester_ft_lstiter();
	printf("\n-----------------------\n");
	tester_ft_lstmap();
	printf("\n-----------------------\n");
	return (0);
}
