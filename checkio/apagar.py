def count_occurrences(main_string: str, substring: str) -> int:
    main_string = main_string.lower()
    substring = substring.lower()
    count = start = 0
    while start < len(main_string):
        pos = main_string.find(substring, start)
        print("aas", pos)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            print("sisi")
            break
    return count


count_occurrences("hello world hello", "hello")
