from API import get_submissions, filter_submissions, get_db_ids, clean_db_ids

database_ids = get_db_ids()
print(database_ids)

bot_test = get_submissions("nosleep", database_ids, 5)
for i in bot_test:
    print(i)

filter_submission_test = filter_submissions(
    subreddit_name='nosleep',
    include=["regretting"],
    exclude=[]
)

print("Filter:", filter_submission_test)




