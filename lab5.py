# Kendra Ludwig (kel334)
# Rebecca Chavez (rlc397)


art = {'a one' : '***',
       'a two' : '* *',
       'a three' : '*****',
       'a four' : '*   *',
       'a five' : '*   *',
       'b one' : '*****',
       'b two' : '**  *',
       'b three' : '****',
       'b four' : '**  *',
       'b five' : '*****'
      }

       
def main():
    def tests():
       print(' ' + art['a one'] + '   ' + art['b one'])
       print(' ' + art['a two'] + '   ' + art['b two'])
       print(art['a three'] + '  ' + art['b three'])
       print(art['a four'] + '  ' + art['b four'])
       print(art['a five'] + '  ' + art['b five'])
    tests()


if __name__ == "__main__":
    main()
