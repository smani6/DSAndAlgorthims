if __name__ == "__main__":
    vowels_list = ['a','e','i','o','u']
    no_of_testcases = int(raw_input())
    for i in xrange(no_of_testcases):
        count = 0;
        str = raw_input().lower()
        for ele in str:
            if ele in vowels_list:
                count = count +1

        print count