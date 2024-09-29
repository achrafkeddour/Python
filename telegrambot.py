import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Reading documents from "file.txt", treating each line as a separate document
def load_documents(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

documents = load_documents('file.txt')

# 2. Representing documents using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# 3. Function to search based on user query
def search(query, documents, vectorizer, tfidf_matrix):
    query_vec = vectorizer.transform([query])
    cos_sim = cosine_similarity(query_vec, tfidf_matrix)
    sorted_indices = np.argsort(cos_sim[0])[::-1]

    results = []
    for idx in sorted_indices:
        if cos_sim[0][idx] > 0.3:
            results.append(f"\nDoc {idx+1}: {documents[idx].strip()} (Similarity: {cos_sim[0][idx]:.2f})")
    
    if not results:
        return "No relevant documents found."
    return '\n'.join(results)

# 4. Start command handler
async def start(update: Update, context):
    await update.message.reply_text("Ahla 7bibna wech rak ! labes ? \n chouf khouna ana bot created by Achraf Keddour \n khassek moussa3ada ? clicki /help ")

# 5. Help command handler
async def help_command(update: Update, context):
    await update.message.reply_text("chouf kho , nta ab3etli questions about students ta3 RT/IMSI (dof3a li 9ra fiha achraf) \n wana rani hna nmedlek des informations 3lihoum wach tes7a9 wziyada hahahahaha \n abda abda ")

# 6. Search query handler
async def handle_message(update: Update, context):
    user_query = update.message.text
    result = search(user_query, documents, vectorizer, tfidf_matrix)
    await update.message.reply_text(result)

# 7. Main function to run the bot
def main():
    # Get your bot token from BotFather
    bot_token = 'something'

    # Create Application instance
    app = ApplicationBuilder().token(bot_token).build()

    # Log all errors
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Define command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Handle text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
