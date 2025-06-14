# Post No: 66647
# I have doubt in Q10
**Topic Slug**: i-have-doubt-in-q10
**Created At**: February 09, 2025 14:51:52

I have doubt in question 10 to convert pdf to markdown<br>
I am not getting correct markdown<br>
<a class="mention" href="/u/pds_staff">@pds_staff</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/592777)

Try using the pymupdf4llm Library<br>
pip install pymupdf4llm
import pymupdf4llm<br>
md_text = pymupdf4llm.to_markdown(“input.pdf”)
import pathlib<br>
pathlib.Path(“output.md”).write_bytes(md_text.encode())
import pymupdf4llm<br>
llama_reader = pymupdf4llm.LlamaMarkdownReader()<br>
llama_docs = llama_reader.load_data(“input.pdf”)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/593235)

