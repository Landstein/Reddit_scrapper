import praw
from database.models import Submission, Subreddit, Comment
from database.db_init import session
from datetime import datetime, timezone


#from db import Submission


client_id = "WKfANfqtJZEuhg"
client_secret = "ruYIIrAlQYS816YCZQVQ8t7MExQ"
app_name = "Python Practice"
username = "Python_integrated"
password = "Python123"

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=client_id,
                     username='Python_integrated',
                     password='Python123')

def get_submissions(subreddit_name, db_ids, limit=1):
    """
    Takes arguments Subreddit name and Limit.  subreddit_name selects the
    subreddit that submissions will be pulled from and Limit is the amount of
    submissions that will be pulled.
    """
    subreddit = reddit.subreddit(subreddit_name)

    if subreddit.id not in db_ids:

        subreddit_row = Subreddit(
            id=subreddit.id,
            display_name=subreddit.display_name,
            subscribers=subreddit.subscribers

        )
        session.add(subreddit_row)
    return_submission = []

    for submission in subreddit.hot(limit=limit):
        if submission.id not in db_ids:
            submission_row = Submission(
                id=submission.id,
                author_fullname=getattr(submission, "author_fullname", None),
                title=submission.title,
                subreddit_display_name=submission.subreddit.display_name,
                subreddit_id=subreddit.id,
                url=submission.url,
                created_utc=datetime.fromtimestamp(submission.created_utc, timezone.utc)
            )
            session.add(submission_row)
            return_submission.append(submission_row)

        for comment in submission.comments:
            if comment.id not in db_ids:
                comment_row = Comment(
                    id=comment.id,
                    author=getattr(comment, "author.name", None),
                    body=getattr(comment, "body", None),
                    score=getattr(comment, "score", None),
                    link_id=getattr(comment, "link_id", None),
                    submission_id=submission.id
                )
                session.add(comment_row)
    session.flush()
    session.commit()

    return return_submission

def filter_submissions(subreddit_name, include=[], exclude=[]):
    filters = []

    for i in include:
        filters.append(Submission.title.ilike(f'%{i}%'))

    for i in exclude:
        filters.append(~Submission.title.ilike(f'%{i}%'))



    submissions = session.query(
        Submission,
        Subreddit
    ).select_from(
        Submission
    ).join(
        Subreddit,
        Subreddit.id == Submission.subreddit_id
    ).order_by(
        Submission.title
    ).filter(
        Subreddit.display_name == subreddit_name,
        *filters
        #expands contents of the filters list
    )

    return submissions.all()


def get_db_ids():
    submission_ids = session.query(
        Submission.id
    ).all()
    subreddit_ids = session.query(
        Subreddit.id
    ).all()
    comment_ids = session.query(
        Comment.id
    ).all()
    print(submission_ids)
    return clean_db_ids([*submission_ids, *subreddit_ids, *comment_ids])


def clean_db_ids(ids):
    clean_submission_ids = []
    for i in ids:
        clean_submission_ids.append(i[0])

    return clean_submission_ids







    #hardwareswap '.['US NYC', 'Macbook Pro']

#select_from is a select from the Submission table.
#Step 1 grabs a row from the submission table
#Step 2 because of the join condition it starts scanning the subreddit table
#step 3 scans the subreddit table until it finds an ID that matches the
#submission subreddit ID (the relationship we have given it in line 73)
#






























#
#
# # session.flush()
# # print(subreddit_table)
# #print(comment_table)
#
# #Put the code to grab a submission and comments into a function
# #look into ways python can send you a notification
# #Look for ways for the bot to post on subreddit post I am interested in
# #clean up comments / Codes
#
#
#
#
#
# # db_query = db.session.query(
# #     db.Submission
# # ).order_by(
# #     db.Submission.created_utc,
# #     db.Submission.title
# # ).filter(
# #     db.Submission.title.ilike('%python%'),
# #     db.Submission.title.ilike('%game%')
# #)
#
# submissions = session.query(
#     Submission,
#     Subreddit
# ).join(
#     Subreddit,
#     Subreddit.id == Submission.subreddit_id
# ).order_by(
#     Submission.title
# ).filter(
#     Submission.title.ilike('%Macbook Pro%'),
#     Submission.title.ilike('%[USA-NY]%')
# )
#
# for i in submissions.all():
#     print(i)
#
# #~ does the opposite of the filter.  For example a ~ before db.Submission.title.ilike('%python%')
# # will find all titles without python
#
# #Lazy Loading:
# #The query won't execute until one of the return methods are called
#
# # for instance in db_query:
# #     print("Date", instance.created_utc, instance.subreddit, instance.title)
# #
# #
# # db.session.flush()
#
# #time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
# #from datetime import datetime, timezone
# #datetime.fromtimestamp(timestamp, timezone.utc)









