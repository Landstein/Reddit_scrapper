#Possible Good source to follow:
#https://www.pythonforengineers.com/build-a-reddit-bot-part-2-reply-to-posts/

for submission in subreddit:
    if "Macbook Pro" in submission:
           submission.reply("I may be interested")

#Steps to Take:
#Commit top 1000 posts from a subreddit to DB
#Run filter on those results
#Collect filtered results and flag results with a tag
#If statement on filtered results to ensure they have what we are looking for
#respond to filtered results


#Functions
#Amount of search results and subreddit
#Filter Criteria
#Response text

#Filter Criteria
#subreddit_name, includes=[], excludes=[]


#ToDo
#Add relationship to comments



#DB State Info:

#Pending State (will be attached to DB session after a flush)
#When a DB is flushed it persists the data which is essentially saving it
#The object will still show up in queries of that session even if the code
#has not been flushed, but if a new session is started and that data was not
#flushed then it will not be in the database because it was never saved.



#Have the code request the submissions every hour and store the filtered results
#will need to use a persistant db
#upsert
