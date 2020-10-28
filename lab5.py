# Kendra Ludwig (kel334)
# Rebecca Chavez (rlc397)


# building blocks for the ASCII char
art = {'a one': '*****',
       'a two': '*   *',
       'a three': '*****',
       'a four': '*   *',
       'a five': '*   *',

       'b one': '*****',
       'b two': '*   *',
       'b three': '*****',
       'b four': '*   *',
       'b five': '*****',

       'c one': '*****',
       'c two': '*    ',
       'c three': '*    ',
       'c four': '*    ',
       'c five': '*****',

       'd one': '**** ',
       'd two': '*   *',
       'd three': '*   *',
       'd four': '*   *',
       'd five': '**** ',

       'e one': '*****',
       'e two': '*    ',
       'e three': '*****',
       'e four': '*    ',
       'e five': '*****',

       'f one': '*****',
       'f two': '*    ',
       'f three': '*****',
       'f four': '*    ',
       'f five': '*    ',

       'g one': '*****',
       'g two': '*    ',
       'g three': '* ***',
       'g four': '*   *',
       'g five': '*****',

       'h one': '*   *',
       'h two': '*   *',
       'h three': '*****',
       'h four': '*   *',
       'h five': '*   *',

       'i one': '*****',
       'i two': '  *  ',
       'i three': '  *  ',
       'i four': '  *  ',
       'i five': '*****',

       'j one': '    *',
       'j two': '    *',
       'j three': '*   *',
       'j four': '*   *',
       'j five': '*****',

       'k one': '*   *',
       'k two': '*  * ',
       'k three': '**   ',
       'k four': '* *  ',
       'k five': '*   *',

       'l one': '*    ',
       'l two': '*    ',
       'l three': '*    ',
       'l four': '*    ',
       'l five': '*****',

       'm one': '*   *',
       'm two': '** **',
       'm three': '* * *',
       'm four': '*   *',
       'm five': '*   *',

       'n one': '*   *',
       'n two': '**  *',
       'n three': '* * *',
       'n four': '*  **',
       'n five': '*   *',

       'o one': ' *** ',
       'o two': '*   *',
       'o three': '*   *',
       'o four': '*   *',
       'o five': ' *** ',

       'p one': '*****',
       'p two': '*   *',
       'p three': '*****',
       'p four': '*    ',
       'p five': '*     ',

       'q one': '*****',
       'q two': '*   *',
       'q three': '* * *',
       'q four': '*  **',
       'q five': '*****',

       'r one': '*****',
       'r two': '*   *',
       'r three': '**** ',
       'r four': '*   *',
       'r five': '*   *',

       's one': '*****',
       's two': '*    ',
       's three': '*****',
       's four': '    *',
       's five': '*****',

       't one': '*****',
       't two': '  *  ',
       't three': '  *  ',
       't four': '  *  ',
       't five': '  *  ',

       'u one': '*   *',
       'u two': '*   *',
       'u three': '*   *',
       'u four': '*   *',
       'u five': '*****',

       'v one': '*   *',
       'v two': '*   *',
       'v three': ' * * ',
       'v four': ' * * ',
       'v five': '  *  ',

       'w one': '*   *',
       'w two': '*   *',
       'w three': '* * *',
       'w four': '** **',
       'w five': '*   *',

       'x one': '*   *',
       'x two': ' * * ',
       'x three': '  *  ',
       'x four': ' * * ',
       'x five': '*   *',

       'y one': '*   *',
       'y two': ' * * ',
       'y three': '  *  ',
       'y four': '  *  ',
       'y five': '  *  ',

       'z one': '*****',
       'z two': '   * ',
       'z three': '  *  ',
       'z four': ' *   ',
       'z five': '*****'
       }


# get word and style from user
def main():
    print("Hello and welcome to the ASCII station!")
    direct = input("Please pick a direction, vertical or horizontal: ")
    word = input("Please enter a word: ")
    if direct == 'vertical':
        vertical(word)
    elif direct == 'horizontal':
        horizontal(word)


# display banner vertically
def vertical(word):
    for num in range(len(word)):
        print(art[word[num] + ' one'])
        print(art[word[num] + ' two'])
        print(art[word[num] + ' three'])
        print(art[word[num] + ' four'])
        print(art[word[num] + ' five'])
        print(' ')


# display banner horizontally
def horizontal(word):
    first_lines = ''
    second_lines = ''
    third_lines = ''
    fourth_lines = ''
    fifth_lines = ''
    for num in range(len(word)):
        first_lines += art[word[num] + ' one'] + ' '
        second_lines += art[word[num] + ' two'] + ' '
        third_lines += art[word[num] + ' three'] + ' '
        fourth_lines += art[word[num] + ' four'] + ' '
        fifth_lines += art[word[num] + ' five'] + ' '
    print(first_lines)
    print(second_lines)
    print(third_lines)
    print(fourth_lines)
    print(fifth_lines)


if __name__ == "__main__":
    main()
