# Post No: 68943
# Solving ROE Realtime
**Topic Slug**: solving-roe-realtime
**Created At**: March 02, 2025 07:30:53

I’ll try to post whatever i solve lol XD

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/solving-roe-realtime/602167)

Q 7 LLM Embeddings (1 mark)
<strong>SecurePay</strong>, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.
Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized v…
ANSWER:<br>
{<br>
“model”: “text-embedding-3-small”,<br>
“input”: [<br>
“Dear user, please verify your transaction code 33692 sent to roe-23f1002382@ds.study.iitm.ac.in”,<br>
“Dear user, please verify your transaction code 66801 sent to roe-23f1002382@ds.study.iitm.ac.in”<br>
]<br>
}

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/solving-roe-realtime/602183)

Q^: 6 Move and rename files (1 mark)
Download q-move-rename-files.zip and extract it. Use <code>mv</code> to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, <code>a1b9c.txt</code> becomes <code>a2b0c.txt</code>.
ANSWER:
<pre><code class="lang-auto">unzip /workspaces/TDS/q-move-rename-files.zip -d extracted_folder123123
    5  mkdir empty_folder 
    6  find extracted_folder -type f -exec mv {} empty_folder/ \; 
    7  ls
    8  find extracted_folder123123 -type f -exec mv {} empty_folder/ \; 
    9  cd empty_folder  
   10  for file in *; do       new_name=$(echo "$file" | tr '0123456789' '1234567890')  ;     mv "$file" "$new_name"  ; done  
   11  grep . * | LC_ALL=C sort | sha256sum  
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/solving-roe-realtime/602184)

Sydney,Brisbane,Perth,Jakarta,Singapore,Dubai,Doha<br>
flights

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/solving-roe-realtime/602196)

150,171,174
for studebts

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/solving-roe-realtime/602197)

