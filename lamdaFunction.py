def run():
    def palindrome(string):
        return string == string[::-1]

    print(palindrome("Juan"))
    
    lamda_palindrome = lambda string: string == string[::-1]

    print(lamda_palindrome("ana"))

if __name__ == "__main__":
    run()