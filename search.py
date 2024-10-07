import arxiv

def search_arxiv_multimodal_papers(year,topic):
    # Broader query to ensure more results
    #search_query = 'multimodal learning OR multimodal AI OR multimodal datasets'
    search_query = topic
    # Search arxiv for up to 200 results
    search = arxiv.Search(
        query=search_query,
        max_results=200,  # Increase results limit
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    
    paper_links = []
    
    # Loop through search results, filtering for papers from 2024
    for result in search.results():
        if result.published.year == year:
            paper_info = {
                'title': result.title,
                'url': result.entry_id
            }
            paper_links.append(paper_info)
    
    return paper_links

print("Enter topic")
topic=input()
print("Enter year")
year=int(input())
# Retrieve and display 2024 multimodal papers
papers = search_arxiv_multimodal_papers(year,topic)

# Print the title and URL of each paper
for paper in papers:
    print(f"Title: {paper['title']}\nLink: {paper['url']}\n")
