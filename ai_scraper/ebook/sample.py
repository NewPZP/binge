from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

graph_config = {
   "llm": {
      "model": "ollama/mistral",
      "temperature": 1,
      "format": "json",  # Ollama needs the format to be specified explicitly
      "model_tokens": 2000, #  depending on the model set context length
      "base_url": "http://localhost:11434",  # set ollama URL of the local host (YOU CAN CHANGE IT, if you have a different endpoint
   },
   "embeddings": {
      "model": "ollama/nomic-embed-text",
      "temperature": 0,
      "base_url": "http://localhost:11434",  # set ollama URL
   }
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
   prompt="get this article, save the title, content, and author",
   # also accepts a string with the already downloaded HTML code
   source="https://www.theatlantic.com/newsletters/archive/2024/06/the-gops-single-message-machine/678591/",
   config=graph_config
)

result = smart_scraper_graph.run()
print(result)