The two programs here are preliminary processing for Facebook message data and GMAIL mbox exports in preparation for more detailed analysis. Each takes a filename as a command line argument and parses the message columns: date, sender, header (for email), and message.

Additionally, the Facebook parser runs sentiment analysis on the text using the sentiment method within TextBlob, which returns both a polarity (positive and negative sentiment) and subjectivity score.
