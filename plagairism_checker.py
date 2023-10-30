import difflib
import re
import requests

def check_plagiarism(text1, text2):
  """Checks for plagiarism between two text strings.

  Args:
    text1: The first text string.
    text2: The second text string.

  Returns:
    A float between 0 and 1, where 1 represents identical text and 0
    represents completely different text.
  """

  matcher = difflib.SequenceMatcher(None, text1, text2)
  return matcher.ratio()

def check_plagiarism_online(text):
  """Checks for plagiarism between the given text and online sources.

  Args:
    text: The text to check for plagiarism.

  Returns:
    A list of tuples, where each tuple contains a URL and a similarity score.
  """

  url = "https://www.plagiarismchecker.com/api/v1/check"
  headers = {"Authorization": "Bearer YOUR_API_KEY"}
  data = {"text": text}

  response = requests.post(url, headers=headers, data=data)

  results = []
  for result in response.json()["results"]:
    results.append((result["url"], result["similarity"]))

  return results

def main():
  """The main function."""

  text1 = input("Enter the first text:")
  text2 = input("Enter the second text:")

  similarity_score = check_plagiarism(text1, text2)

  print("Similarity score:", similarity_score)

  if similarity_score > 0.75:
    print("WARNING: The two text strings are highly similar.")

    online_results = check_plagiarism_online(text1)

    for url, similarity_score in online_results:
      print(f"URL: {url}, Similarity score: {similarity_score}")

if __name__ == "__main__":
  main()
