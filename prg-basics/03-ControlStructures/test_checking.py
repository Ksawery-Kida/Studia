total_tasks = 20
tasks_ok = (20, 11, 10, 9, 0, 2, 3, 4, 5, 6, 11)
test_passed = False

if len(tasks_ok) >= 10 and total_tasks == 20:
    test_passed = True


if test_passed:
    print('Congratulations! You passed the test.')


else:
    print('Unfortunately, you failed the test.')
