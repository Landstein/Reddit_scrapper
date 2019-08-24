from API import get_submissions, filter_submissions, get_db_ids, clean_db_ids
import yagmail
import json

SUBREDDIT = "hardwareswap"

database_ids = get_db_ids()
print(database_ids)

# only will return new submissions
new_submissions = get_submissions(SUBREDDIT, database_ids, 1)
for i in new_submissions:
    print(i)

#
filter_submission_test = filter_submissions(
    new_submissions=new_submissions,
    subreddit_name=SUBREDDIT,
    include=["Surface"],
    exclude=[]
)
# ToDo Create format string so when sending to email it looks better (remove list)
email_list = []
for u in filter_submission_test:
    post_url = u.Submission.url
    post_title = u.Submission.__dict__["title"]
    sub_reddit = u.Submission.__dict__["subreddit_display_name"]
    email_list.append(post_url)
    email_list.append(post_title)
    email_list.append(sub_reddit)

email_list = [str(i) for i in email_list]

print("email List", email_list)


print("Filter:", filter_submission_test)

yag = yagmail.SMTP('pythonyagyag@gmail.com', 'PythonTest123')

contents = [
    "This is a test first email"
]
yag.send('emlandstein@gmail.com', 'Test', email_list)

# Alternatively, with a simple one-liner:
#yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', contents)


