import rapidapi_news
import gemini_summary
import webscrap
import datetime

def writefile(filename,response, link):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            #f.write(f"Detailed Summary - {datetime.date.today()}\n")
            #f.write("="*40 + "\n\n")
            f.write(response + "\n\n")
            f.write("reference " + link +"\n\n")
            f.write("="*40 + "\n\n")
    except IOError as e:
        print(f"❌ Error writing to file: {e}")

if __name__=="__main__":
    #get latest news link
    filename=f"news_sumamry.txt"
    newscontent = []
    news_data=rapidapi_news.get_news(topic="SCIENCE",websitelimit=5)
    for article in news_data["data"]:
        print(f"- Title: {article['title']}")
        print(f"  Link: {article['link']}")
        print_link=f"Link: {article['link']}"

        #scrap the web link
        article_text=webscrap.scrape(article['link'])
        print("\n" + "-"*50 + "\n")
        #call gemini to summarize
        # Truncate content if it's too long for the model's context window
        max_tokens = 1000  # A generous limit, adjust as needed
        if len(article_text.split()) > max_tokens:
            article_text = ' '.join(article_text.split()[:max_tokens]) + "..."
        # Summarize the content using Gemini-Flash
        prompt = f"Provide a concise linkedin post with icons:\n\n{article_text}"
        guardrails = f" Do not add introductory phrases or headers like 'Here's a concise..' If the article doesn't seems to be aligned with other content then respond as 403 Client Error "
        prompt_text = prompt + guardrails
        #print(prompt)
        # Adjust generation configuration if needed (e.g., temperature for creativity)
        response=gemini_summary.summarize_with_gemini(prompt_text)
        writefile(filename, response, print_link)
        newscontent.append([response, print_link])
    print(f"✅ All summaries saved to '{filename}'")

    final = ""
    for rsp,lnk in newscontent:
        prompt_to_filter = f"For content below: \n{rsp} . \n Give me True & False responses only. True - if content is related to technology, innovation, AI, ML; otherwise False. Consider '403 Client Error' as False"
        yes_no=gemini_summary.summarize_with_gemini(prompt_to_filter)
        if yes_no == 'True':
            final = final + f"{rsp} \n {lnk} \n"

    prompt_to_print=f"get me the best technology news from the below summaries and just get me that summary nothing else: {final}"
    x= gemini_summary.summarize_with_gemini(prompt_to_print)
    print(x)



        
        




        



   