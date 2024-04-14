import matplotlib.pyplot as plt

# Define the reviews and their corresponding sentiment scores for TripAdvisor
tripadvisor_reviews = ['Review 1', 'Review 2', 'Review 3', 'Review 4']
tripadvisor_sentiments = [0.569, -0.367, 0.3, -0.4]

# Plot the sentiment analysis results for TripAdvisor
plt.figure(figsize=(8, 5))
plt.bar(tripadvisor_reviews, tripadvisor_sentiments, color=['green' if score > 0 else 'red' if score < 0 else 'gray' for score in tripadvisor_sentiments])
plt.xlabel('Reviews')
plt.ylabel('Sentiment Polarity')
plt.title('Sentiment Analysis Results - TripAdvisor')
plt.axhline(0, color='black', linewidth=0.5)  # Add horizontal line at y=0 for reference
plt.ylim(-1, 1)  # Set y-axis limits
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Define the review and its corresponding sentiment score for Airlineratings.com
airlineratings_review = 'Review 5'
airlineratings_sentiment = [-0.006]

# Plot the sentiment analysis results for Airlineratings.com
plt.figure(figsize=(8, 5))
plt.bar([airlineratings_review], airlineratings_sentiment, color=['green' if score > 0 else 'red' if score < 0 else 'gray' for score in airlineratings_sentiment])
plt.xlabel('Reviews')
plt.ylabel('Sentiment Polarity')
plt.title('Sentiment Analysis Results - Airlineratings.com')
plt.axhline(0, color='black', linewidth=0.5)  # Add horizontal line at y=0 for reference
plt.ylim(-1, 1)  # Set y-axis limits
plt.yticks([-1, -0.5, 0, 0.5, 1])  # Adjust y-axis ticks for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()






import matplotlib.pyplot as plt

# Define the review and its corresponding sentiment score for Skytrax
skytrax_review = 'Review 6'
skytrax_sentiment = [-0.9]  # Adjust the sentiment score based on the analysis

# Plot the sentiment analysis results for Skytrax
plt.figure(figsize=(8, 5))
plt.bar([skytrax_review], skytrax_sentiment, color=['green' if score > 0 else 'red' if score < 0 else 'gray' for score in skytrax_sentiment])
plt.xlabel('Reviews')
plt.ylabel('Sentiment Polarity')
plt.title('Sentiment Analysis Results - Skytrax')
plt.axhline(0, color='black', linewidth=0.5)  # Add horizontal line at y=0 for reference
plt.ylim(-1, 1)  # Set y-axis limits
plt.yticks([-1, -0.5, 0, 0.5, 1])  # Adjust y-axis ticks for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()




import matplotlib.pyplot as plt

# Define review titles and their corresponding sentiment scores
reviews = ['Great Experience (TripAdvisor)', 'Disappointing Journey (TripAdvisor)', 'Pleasant Surprise (TripAdvisor)',
           'Unpleasant Experience (TripAdvisor)', 'Room for Improvement (Airlineratings.com)', 'Critical Assessment (Skytrax)']
sentiments = [0.569, -0.367, 0.3, -0.4, -0.006, -0.9]

# Create a color map for positive, negative, and neutral sentiments
colors = ['green' if score > 0 else 'red' if score < 0 else 'gray' for score in sentiments]

# Plot the sentiment analysis results
plt.figure(figsize=(10, 6))
plt.bar(reviews, sentiments, color=colors)
plt.xlabel('Reviews')
plt.ylabel('Sentiment Polarity')
plt.title('Sentiment Analysis Results for British Airways Reviews')
plt.axhline(0, color='black', linewidth=0.5)  # Add horizontal line at y=0 for reference
plt.ylim(-1, 1)  # Set y-axis limits
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better visualization
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()





from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text for TripAdvisor reviews
tripadvisor_reviews = [
    "Great experience with British Airways.",
    "Disappointing journey, not recommended.",
    "Pleasant surprise, exceeded expectations.",
    "Unpleasant experience overall."
]

# Combine all reviews into a single text
combined_text = " ".join(tripadvisor_reviews)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(combined_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('TripAdvisor Reviews Word Cloud')
plt.show()


# Sample text for Airlineratings.com review
airlineratings_text = "Room for improvement highlighted."

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(airlineratings_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Airlineratings.com Review Word Cloud')
plt.show()


# Sample text for Skytrax review
skytrax_text = "Service standards are poor. Product quality is perceived as cheap."

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(skytrax_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Skytrax Review Word Cloud')
plt.show()

