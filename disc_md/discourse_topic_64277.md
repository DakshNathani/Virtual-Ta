# Post No: 64277
# Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]
**Topic Slug**: project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025
**Created At**: January 19, 2025 08:17:46

Please post any questions related to <a href="https://tds.s-anand.net/#/project-1">Project 1 - LLM-based Automation Agent</a>.
Deadline: <span class="discourse-local-date" data-date="2025-02-16" data-email-preview="2025-02-16T18:29:00Z UTC" data-format="LLLL" data-time="23:59:00" data-timezone="Asia/Calcutta">Sunday, February 16, 2025 6:29 PM</span>
<strong>Update on 27 Jan 2025</strong>:
A <em>sample</em> evaluation script for Project 1 tasks A1-A10 is available at <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub</a>
You can use this to validate your code for Project 1.
Please note:
<ol>
<li>This is a sample. It <strong>WILL</strong> change.</li>
<li>Don’t rely on the dataset being the same. It <strong>WILL</strong> change.</li>
<li>LLMs give different results each time they are called. Make sure:
<ul>
<li>Your code gives correct results <em>reliably</em> (i.e. try a few times)</li>
<li>Change the task in the evaluation script slightly to test variations</li>
</ul>
</li>
<li>Your <a href="https://aiproxy.sanand.workers.dev/">AI Proxy usage</a> resets on 1 Feb. You have a limited budget. Utilize what you can this month.</li>
<li>For those who <a href="https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog">submit their code</a> by Friday 31 Jan, I will run a sample evaluation and share the results.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/581882)



[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/581888)

sir show us all the way to do project

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/582037)

Hi Shouvik,
We will have live sessions to guide on how to do project.
Kind regards<br>
Jivraj

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/582038)

Will those session be on youtube too?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/582333)

Hi Sakthivel,
Yes all sessions are being recorded and are available on youtube within a day.<br>
<a href="https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C" rel="noopener nofollow ugc">Jan 25 TDS Playlist</a>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/582334)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276.png" data-download-href="/uploads/short-url/4BkD3LlTOfyv9hWwtxx8jW22F14.png?dl=1" title="Screenshot 2025-01-23 151614" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276_2_690x67.png" alt="Screenshot 2025-01-23 151614" data-base62-sha1="4BkD3LlTOfyv9hWwtxx8jW22F14" width="690" height="67" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276_2_690x67.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276_2_1035x100.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/0/20410aa56e88be04883b6f3feca5010089afe276.png 2x" data-dominant-color="3F484E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-23 151614</span><span class="informations">1281×125 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
sir <a class="mention" href="/u/jivraj">@Jivraj</a> after editing line 127 in datagen.py i got those  required data files. is it allowed ? also i had to run datagen.py MANUALLY(is this process also should be automatic)?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/584016)

Hi Guddu ,
I didn’t make any changes to file and it worked for me. Can you mention what is need of making changes ?
command that I used :<br>
<code>uv run datagen.py 22f3002542@ds.study.iitm.ac.in --root ./data</code>
here --root option defines the folder where you want to store generated data. by default it would try to create a folder in root directory of operating system.
Kind regards<br>
Jivraj

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/584052)

getting this issue :
<pre><code class="lang-auto">openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/584083)

Hi Aishik,
Pls add context to your query, without that we won’t be able to understand, where exactly you are facing problem.
<aside class="quote group-ds-students" data-username="23f2005325" data-post="10" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2005325/48/68296_2.png" class="avatar"> 23f2005325:</div>
<blockquote>
<pre><code class="lang-auto">openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}
</code></pre>
</blockquote>
</aside>
Possible reasons for this issue:
<ol>
<li>Not using anand sir’s proxy url for sending requests.</li>
<li>Token not being correct.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/584107)

yes I was not setting the base url to the proxy. I have fixed it thank you .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/585092)

While implementing task A5, I am confused about what recent actually means in the phrase “recent log file”, mentioned under task A5, in the problem statement. This confusion arises because there are no dates corresponding to the log files. Should I consider log-0 as the most recent one? or the log-&lt;largest_number&gt; file? Please clarify.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/585171)

I am getting the following response when I am trying to extract credit card number from the credit-card.png :
<pre data-code-wrap="json"><code class="lang-json">{'id': 'chatcmpl-&lt;redacted&gt;', 'object': 'chat.completion', 'created': 1737872397, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': "I'm sorry, but I can't assist with that.", 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 946, 'completion_tokens': 11, 'total_tokens': 957, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': '&lt;redacted&gt;', 'monthlyCost': 0.07715699999999998, 'cost': 0.0029040000000000003, 'monthlyRequests': 31, 'costError': 'crypto.createHash is not a function'}
</code></pre>
my code is as below :
<pre data-code-wrap="python"><code class="lang-python">def extract_credit_card_number():
    import requests
    import base64
    import os
    from dotenv import load_dotenv
    load_dotenv()



    BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ["AIPROXY_TOKEN"]}"
    }

    image_path = "../data/credit_card.png"

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",  
                "content": "You are a helpful assistant that provides detailed and accurate descriptions of images. Focus on describing the objects, colors, textures, the overall scene, and most importantly, the text and numbers in the image. Be concise but thorough."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are given an image containing a credit card number. Extract the credit card number from the image"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
    }

    
    response = requests.post(BASE_URL, headers=headers, json=payload)

    
    if response.status_code == 200:
        result = response.json()
        print("RESULT:", result)
        cno = result["choices"][0]["message"]["content"]
        print("CREDIT CARD NUMBER:", cno)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
</code></pre>
please guide <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/585547)

do we have to do these tasks in the linux? As in some of the GA1, the linux answers only accepted. Please tell me that, do we can do it in the desktop or we have to use linux?<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586263)

The bash commands are usually run in a linux machine, but you can easily run those commands in VSCode without installing any virtual machines. Download the WSL extension in VSCode and you will get a WSL terminal to work with.
For more information watch this video <a href="https://youtu.be/q74CP4fB7cY?si=M_zw8WzpmMCyVQat" rel="noopener nofollow ugc">https://youtu.be/q74CP4fB7cY?si=M_zw8WzpmMCyVQat</a> or watch TDS Live Sessions.
Regards,<br>
TDS TA

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586429)

what frameworks can we use? hopefully anything?
or what frameworks can’t we use?<br>
<a class="mention" href="/u/carlton">@carlton</a>   <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586506)

Project 1 deliverables are all that matter. How you accomplish them is not very relevant. The keys to a successful Project 1 are:<br>
Deliverables,<br>
and <em>an example</em> of the Evaluation has been provided.<br>
If your project runs in accordance with the Evaluation methodology then it is considered.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4.png" data-download-href="/uploads/short-url/alQUzS7pakBH4aCVJZXLB7NS2LG.png?dl=1" title="Screenshot 2025-01-27 at 8.35.23 am" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_500x500.png" alt="Screenshot 2025-01-27 at 8.35.23 am" data-base62-sha1="alQUzS7pakBH4aCVJZXLB7NS2LG" width="500" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_500x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_750x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/8/488e23f9ea65d35c5ba806fab09f4b5934ed2ed4_2_1000x1000.png 2x" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-27 at 8.35.23 am</span><span class="informations">1764×1764 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Please read the documentation carefully from top to bottom.
So the main question is how do you test if the script will run according to the evaluation? The whole point is for it to run not just on your system. It should be deployable anywhere on any machine. Your solution should work anywhere we test it. Thats why you package it in a docker container. How you achieve that is up to you. But if we cannot run your docker container according to the specification we have provided then it has failed this crucial test.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586519)

<a class="mention" href="/u/23f1002382">@23f1002382</a>
You can use any library as long as your Project 1 meets the deliverable requirements and does all the (20+) API tasks.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586522)

A <em>sample</em> evaluation script for Project 1 tasks A1-A10 is available at <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" class="inline-onebox">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub</a>
You can use this to validate your code for Project 1.
Please note:
<ol>
<li>This is a sample. It <strong>WILL</strong> change.</li>
<li>Don’t rely on the dataset being the same. It <strong>WILL</strong> change.</li>
<li>LLMs give different results each time they are called. Make sure:
<ul>
<li>Your code gives correct results <em>reliably</em> (i.e. try a few times)</li>
<li>Change the task in the evaluation script slightly to test variations</li>
</ul>
</li>
<li>Your <a href="https://aiproxy.sanand.workers.dev/">AI Proxy usage</a> resets on 1 Feb. You have a limited budget. Utilize what you can this month.</li>
<li>For those who <a href="https://docs.google.com/forms/d/e/1FAIpQLSdOaljgV-INdbKrPotV9OMUKV01QVaFEfcnr5dAxBZqM4x37g/viewform?usp=dialog">submit their code</a> by Friday, I will run a sample evaluation and share the results.</li>
</ol>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> - please socialize this during the live sessions.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586786)

By clicking the project link ,I am getting the notes…but no project is available in my project 1

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586801)

by clicking the link
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9.png" data-download-href="/uploads/short-url/7eRv8qw8NqNdtMS9w7galsdr3Nn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9_2_690x78.png" alt="image" data-base62-sha1="7eRv8qw8NqNdtMS9w7galsdr3Nn" width="690" height="78" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9_2_690x78.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9_2_1035x117.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32bd53681054ab17de6350c49f68b405acd538b9.png 2x" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1198×136 9.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/3/937562cc32dc76a582f6845678b048730622d388.png" data-download-href="/uploads/short-url/l2tGyjPZGc4BeKrx2WotCt6x2fC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/937562cc32dc76a582f6845678b048730622d388_2_690x229.png" alt="image" data-base62-sha1="l2tGyjPZGc4BeKrx2WotCt6x2fC" width="690" height="229" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/937562cc32dc76a582f6845678b048730622d388_2_690x229.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/937562cc32dc76a582f6845678b048730622d388_2_1035x343.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/937562cc32dc76a582f6845678b048730622d388_2_1380x458.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1750×581 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am getting this opened.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586802)

Hi <a class="mention" href="/u/divya1">@Divya1</a> ,
There won’t be any project1 page such as GA1s, there is a google form(which can be found in same page) which needs to be filled after you do project1.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586908)

Hi <a class="mention" href="/u/23f2005325">@23f2005325</a> ,
Extracting details from credit cards is sensitive, try using strong prompts or take code from LLM and execute it in script.
kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/586910)

Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environment using maybe ollama(local llm as now there is deepseek opensource, i doubt we would need to use openai for testing, just for production(test submission)  would be enough) and also some agent(langchain, autogen, crewai) just a quick how-to on setting up and problems while setting up if possible
More resources on docker. Using docker as a virtual environment. Editing and executing code in Dockerfiles (like when you change code in src a web framework automatically reloads page(hot reload)), something along the lines of this .
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587088)

<aside class="quote group-ds-students" data-username="23f1002382" data-post="26" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png" class="avatar"> 23f1002382:</div>
<blockquote>
Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environmen
</blockquote>
</aside>
In Tuesday’s(21 January) session we had discussed docker towards ending of session.<br>
What was discussed in that live session regarding docker:
<ol>
<li>Search for existing containers on repositories such as dockerhub.</li>
<li>Pull an existing docker image.</li>
<li>Run that image inside a container.</li>
<li>Enter to that container and modify something(such as installing python inside a ubuntu container, for customization or create some file)</li>
<li>Once done you can commit it.</li>
<li>And push customized container’s image to docker hub.</li>
</ol>
Regarding local models running for project1, it’s a good idea, we will see if it’s possible to discuss in session.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587185)

In the google forms , I have 2 questions in one form now to submit should it is compulsory that to answer the both the questions?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587326)

Hi <a class="mention" href="/u/divya1">@Divya1</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31.png" data-download-href="/uploads/short-url/7GRWQ9A0Ygc4UgcaxkNn2rTuJyx.png?dl=1" title="Screenshot 2025-01-29 at 8.19.05 am" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31_2_690x389.png" alt="Screenshot 2025-01-29 at 8.19.05 am" data-base62-sha1="7GRWQ9A0Ygc4UgcaxkNn2rTuJyx" width="690" height="389" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31_2_690x389.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31_2_1035x583.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35e7ce763c7605e99ee1fad3906e1cd31d094b31_2_1380x778.png 2x" data-dominant-color="F3F2F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-29 at 8.19.05 am</span><span class="informations">1738×982 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Please do very carefully all things mentioned in the Deliverables as well as look at the Evaluation Section.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09.png" data-download-href="/uploads/short-url/jCKzqFDYJsTz1kwHUd0AifW2DWN.png?dl=1" title="Screenshot 2025-01-29 at 8.26.08 am" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09_2_690x234.png" alt="Screenshot 2025-01-29 at 8.26.08 am" data-base62-sha1="jCKzqFDYJsTz1kwHUd0AifW2DWN" width="690" height="234" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09_2_690x234.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09_2_1035x351.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/898ab28ebe773e40fb3ad9b98c71ce4c5d063c09_2_1380x468.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-29 at 8.26.08 am</span><span class="informations">1460×496 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
We had a session on 28th Jan introducing all the important aspects of Project.
If you do not do everything exactly as mentioned <strong>especially the pre - requisites</strong> mentioned in the Evaluation section you will get 0 in the project and <em>there will be no appeal</em> for failing to meet the pre - requisites of the evaluation criteria.
In order for us to evaluate the project you have to provide the deliverables mentioned above.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587355)

<hr>
<strong>Subject:</strong> Request to Add Instructors to Private GitHub Repo
<strong>Message:</strong><br>
<em>"Dear [Instructors’ Names],</em>
<em>I’ve set up the environment and dependencies for the project and was wondering if it would be appropriate to add you to my private GitHub repository. I’d appreciate any guidance on improving performance, scalability, and design principles. Please let me know if this is feasible or if there’s a more suitable way to seek feedback. Apologies if this request is out of scope.</em>
<em>Thank you for your time!</em>
<em>Best,</em><br>
[Your Name]"*
ChatGPT can make mistakes. Check important info.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587402)

<a class="mention" href="/u/23f1002382">@23f1002382</a> - You’re welcome to use the evaluation script in this post for private repos.
<aside class="quote quote-modified" data-post="21" data-topic="164277">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/21">Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    A sample evaluation script for Project 1 tasks A1-A10 is available at <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" class="inline-onebox">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub</a> 
You can use this to validate your code for Project 1. 
Please note: 

This is a sample. It WILL change.
Don’t rely on the dataset being the same. It WILL change.
LLMs give different results each time they are called. Make sure:

Your code gives correct results reliably (i.e. try a few times)
Change the task in t…
  </blockquote>
</aside>

For public repos submitted in the form, I’ll run this script over the weekend and share preliminary results.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587464)

T  h  a  n  k      y  o  u         sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587475)

For A6, /data/docs/ has subfolders with .md files from which we have to extract the heading level 1’s (#) right? Apparently there are few files with different content but the same name. Can someone confirm the same? If yes how to address these files <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587763)

I had set up the environment and dependencies and everything was working fine. When i tried to recreate it from scratch in a new codespace it broke. I fixed almost everything except this error
<pre><code class="lang-auto">@ANdIeCOOl ➜ /workspaces/TDS-Project-1 (main) $ crewai create crew b2b
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/crewai", line 5, in &lt;module&gt;
    from crewai.cli.cli import crewai
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/__init__.py", line 3, in &lt;module&gt;
    from crewai.agent import Agent
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agent.py", line 7, in &lt;module&gt;
    from crewai.agents import CacheHandler
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/__init__.py", line 2, in &lt;module&gt;
    from .parser import CrewAgentParser
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/parser.py", line 6, in &lt;module&gt;
    from crewai.utilities import I18N
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/__init__.py", line 13, in &lt;module&gt;
    from .embedding_configurator import EmbeddingConfigurator
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/embedding_configurator.py", line 4, in &lt;module&gt;
    from chromadb import Documents, EmbeddingFunction, Embeddings
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/__init__.py", line 6, in &lt;module&gt;
    from chromadb.auth.token_authn import TokenTransportHeader
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py", line 24, in &lt;module&gt;
    from chromadb.telemetry.opentelemetry import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 13, in &lt;module&gt;
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/trace_exporter/__init__.py", line 25, in &lt;module&gt;
    from opentelemetry.exporter.otlp.proto.grpc.exporter import (  # noqa: F401
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py", line 72, in &lt;module&gt;
    from opentelemetry.sdk.metrics.export import MetricsData
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py", line 16, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal import Meter, MeterProvider
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py", line 56, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.measurement_consumer import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py", line 29, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.metric_reader_storage import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py", line 26, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal._view_instrument_match import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py", line 22, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.aggregation import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py", line 48, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.exponent_mapping import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py", line 25, in &lt;module&gt;
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.ieee_754 import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py", line 15, in &lt;module&gt;
    from ctypes import c_double, c_uint64
  File "/usr/local/python/3.12.1/lib/python3.12/ctypes/__init__.py", line 8, in &lt;module&gt;
    from _ctypes import Union, Structure, Array
ImportError: /usr/local/python/3.12.1/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
</code></pre>
i updated the libffi package using sudo but while breaking something else can someone pls help me? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a><br>
<br><br>
<br><br>
<br>
history of commands in new codespace
<pre><code class="lang-auto">    1  crewai --version
    2  pip install crewai crewai-tools
    3  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    4  export PATH=/opt/conda/bin:$PATH
    5  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    6  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    7  crewai create crew &lt;project_name&gt;
    8  crewai create crew b2b
    9  history
</code></pre>
<br>
<br>
UPDATE: IT’s WORKING if you do this in order
<pre><code class="lang-auto">    1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    2  export PATH=/opt/conda/bin:$PATH
    3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    5  pip install --no-cache-dir --force-reinstall typing_extensions pydantic crewai crewai-tools
    6  conda install -c conda-forge typing_extensions
    7  exec bash
    8  crewai create crew "Project 1 - LLM-based Automation Agent"
</code></pre>
Something about different environment conda and python can the instructors please help me understand it(resources ), so i can trouble shoot this later with better accuracy come precision

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587764)

evaluate.py<br>
TDS course repo<aside class="onebox githubfolder" data-onebox-src="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" target="_blank" rel="noopener nofollow ugc">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...</a></h3>


  <span class="label1">Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

line 20
<pre><code class="lang-auto">from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
</code></pre>
but we get datagen.py only in a1 task<br>
line 69
<pre><code class="lang-auto">async def a1(email: str, **kwargs):
    await run(
        f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
    )
    return email in await read("/data/format.md")
</code></pre>
The issue is <strong>importing <code>datagen</code> before ensuring it exists</strong>
just checking
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/587902)

Hi <a class="mention" href="/u/23f1002382">@23f1002382</a>,
Yes datagen.py must be present in same directory from where you  are executing evaluate.py.
Oh, You trying to use crewai locally for Project1<br>
kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588062)

Hi <a class="mention" href="/u/joeljeffrey">@JoelJeffrey</a> ,
Filepath is unique for every file, which needs to be inserted to json file.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588063)

Ok. So just to confirm, since there are files with the same name, the json file should map the filepath and not the filename to the title right?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d3ebea3238860bad920a47ff55ac33cb02ad2d63.png" data-download-href="/uploads/short-url/ueKbRWWjd5grI2e1vqOReD58S1t.png?dl=1" title="Screenshot from 2025-01-31 12-25-29" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d3ebea3238860bad920a47ff55ac33cb02ad2d63.png" alt="Screenshot from 2025-01-31 12-25-29" data-base62-sha1="ueKbRWWjd5grI2e1vqOReD58S1t" width="690" height="102" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-01-31 12-25-29</span><span class="informations">790×117 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588156)

no crewai, it takes really long i put time out for 300 secs(in run(task:str) in evaluate.py) still sometimes its not enough. I’ll try with autogen next and then langchain

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588190)

<pre><code class="lang-auto">INFO:     127.0.0.1:65085 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
data/format.md 81ms
INFO:     127.0.0.1:65149 - "POST /run?task=%0AFormat+the+contents+of+%60%2Fdata%2Fformat.md%60+using+%60prettier%403.4.2%60%2C+updating+the+file+in-place%0A HTTP/1.1" 200 OK
INFO:     127.0.0.1:65251 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
INFO:     127.0.0.1:65263 - "POST /run?task=The+file+%60%2Fdata%2Fdates.txt%60+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+%60%2Fdata%2Fdates-wednesdays.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65298 - "GET /read?path=/data/dates-wednesdays.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65312 - "POST /run?task=Sort+the+array+of+contacts+in+%60%2Fdata%2Fcontacts.json%60+by+%60last_name%60%2C+then+%60first_name%60%2C+and+write+the+result+to+%60%2Fdata%2Fcontacts-sorted.json%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65350 - "GET /read?path=/data/contacts-sorted.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65361 - "POST /run?task=Write+the+first+line+of+the+10+most+recent+%60.log%60+file+in+%60%2Fdata%2Flogs%2F%60+to+%60%2Fdata%2Flogs-recent.txt%60%2C+most+recent+first HTTP/1.1" 200 OK
INFO:     127.0.0.1:65390 - "GET /read?path=/data/logs-recent.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65402 - "POST /run?task=Find+all+Markdown+%28%60.md%60%29+files+in+%60%2Fdata%2Fdocs%2F%60.%0AFor+each+file%2C+extract+the+first+occurrance+of+each+H1+%28i.e.+a+line+starting+with+%60%23+%60%29.%0ACreate+an+index+file+%60%2Fdata%2Fdocs%2Findex.json%60+that+maps+each+filename+%28without+the+%60%2Fdata%2Fdocs%2F%60+prefix%29+to+its+title%0A%28e.g.+%60%7B%22README.md%22%3A+%22Home%22%2C+%22path%2Fto%2Flarge-language-models.md%22%3A+%22Large+Language+Models%22%2C+...%7D%60%29 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65436 - "GET /read?path=/data/docs/index.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65452 - "POST /run?task=%60%2Fdata%2Fcredit_card.png%60+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcredit-card.txt%60 HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65482 - "GET /read?path=/data/credit-card.txt HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65503 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:49154 - "GET /read?path=/data/ticket-sales-gold.txt HTTP/1.1" 200 OK
</code></pre>
result after running evaluate.py:
<img src="https://emoji.discourse-cdn.com/google/dart.png?v=12" title=":dart:" class="emoji" alt=":dart:" loading="lazy" width="20" height="20"> Score: 0 / 10
why sir <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>  what is the problem here??<br>
please do a live session of complete project process with one or two tasks if possible

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588192)

Hi Guddu,
We are planning several project sessions in order to show the workflow of creating a successful project.
Although you are returning a 200 ok, the get request file must match the expectation. In other words after running the first task for example, has the new format.md been formatted correctly and matches the expected output.
In this case you would write out the the <code>expected</code> variable in the <code>evaluate.py</code> and see if <code>result</code> variable matches the <code>expected</code>. Then you can figure out what went wrong.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588200)

Ok sir<br>
But please try to take those sessions sooner<br>
Because it’s taking too much time for me to do any problem(plus two more courses and one oppe you know) .so I just want to build the project before deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588211)

Please give the date, time and agenda also please.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588237)

Yes sir ,<img src="https://emoji.discourse-cdn.com/google/saluting_face.png?v=12" title=":saluting_face:" class="emoji" alt=":saluting_face:" loading="lazy" width="20" height="20">
As soon as we know we will send an announcement.
Kind regards.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588244)

the model keeps wrong answer, it says uvicorn for uv and has no info on how to run uv even after explicitly giving instructions(basically an older model) , basic “ls” command is also wrong, among other things. You can check your logs with respect to my api key.<br>
Do you think we could access a better model?
Maybe Download Deepseek 70b or even 671b and create an api while y’all run the model locally, in the long it would be cheaper for the course?<br>
because the model doesn’t know basic commands after telling how to do it.<br>
So if the model gives us wrong commands 2/3 times then how would we even solve the question.<br>
I spent a week on this just saying<br>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588510)

sent pull request maybe accept it then please <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588521)

<div class="youtube-onebox lazy-video-container" data-video-id="sdg4N-H4BR0" data-video-title="2025-01-31 Week 3 - Session 4 - TDS Jan 25" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=sdg4N-H4BR0" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/5/75628a6b4c923f0a11501b30fafc0317310f82fd.jpeg" title="2025-01-31 Week 3 - Session 4 - TDS Jan 25" data-dominant-color="49413A" width="690" height="388">
  </a>
</div>

can we have the code for this session please?<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/588583)

i need some help can you send me your repo?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/589264)

Hello, I recently started working on the project. I understood how to do all the phase A tasks on a high level but I’m struggling to start the implementation of the first task in phase A. I’m confused mainly about how the /data directory is supposed to be created, I don’t know how to generate the data and a little confused about the output formats. I would appreciate if I could get in contact with anyone who could guide me in the right direction.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590035)

Hello everyone, <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a><br>
I had a few queries regarding the project;
<ol>
<li>I am preloading my docker image with uv and generating the /data files when the container is ran. For task A1, I am automating my server to remove the /data directory that’s already present and run datagen.py again. Is this fine?</li>
<li>For /read endpoint, is there a standard for parameters like “path=/data/format.md” or the parameter could be a plain english sentence like “path=show the data in format.md”?</li>
<li>Are we concerned about what’s shown on the console if I run a /run command as long as it gets the job done?</li>
<li>For tasks A1-10, are the file paths provided in the project doc standard or even they’re flexible? Ex. “Count the number of Wednesdays in file /data/format.md, and write just the number to /data/out.txt”</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590128)

+1<br>
<br><br>
<br><br>
<br><br>
<br>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590164)

Dear Sir,<br>
Can we have a mentorship program for TDS for those who have no experience in programming like me ?<br>
thanks &amp; regards.<br>
ULAGAOOZHIAN

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590213)

For Project-1 to complete, it requires:<br>
"You MUST complete ALL these 3 steps to get a score. Failure to do so will result in getting 0 in the project. If you do not do ALL these 3 steps before the deadline, there will be no appeal available.<br>
• Fill the form that is on the Project Page<br>
But I did not get the form; where is it? While I checked inside the project pages also.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590283)

Hi Dewang,
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306.png" data-download-href="/uploads/short-url/kUeQpf8MMOL4Iezh7zL7bTgwg5M.png?dl=1" title="Screenshot 2025-02-03 at 6.27.39 pm 1" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306_2_642x500.png" alt="Screenshot 2025-02-03 at 6.27.39 pm 1" data-base62-sha1="kUeQpf8MMOL4Iezh7zL7bTgwg5M" width="642" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306_2_642x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306_2_963x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/2/9286f3dcf5984d514cf6a40996bd5040f5d9c306_2_1284x1000.png 2x" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-03 at 6.27.39 pm 1</span><span class="informations">2268×1766 491 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Please <em>read</em> the Project page Deliverables carefully as well as the Evaluation Pre - Requisites.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590282)

<aside class="onebox githubblob" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md">
  <header class="source">

      <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># TDS-Project1-Ollama_FastAPI-
## Info
- Create codespaces on main or evalution script branch
Use history.txt to get sqlite to version 3.45.3 into bash session 
   - 64  export PATH=/opt/conda/bin:$PATH
   - 65  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
   - 66  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"

- cd to latest_ai_development and run cmd [ crewai run] which set up server 
- Then in a separate bash terminal run "python evaluate.py" 
- also make sure to enter openai or sanand api key in crew.py

# Simple history of commands
1. Terminal 1 
    - 1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 2  export PATH=/opt/conda/bin:$PATH
    - 3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    - 4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 5  cd latest_ai_development/
    - 7  pip install crewai crewai-tools
</code></pre>



  This file has been truncated. <a href="https://github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

My take on autonomous agents. Limited by model capabilities to some extent. Will use function calling hence forth but here is a quick look at using crewai for agent tasks.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590523)

Sir   <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> just saying,<br>
If possible Please do 40-50% of project in upcoming live sessions so that we all have atleast something to submit.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590531)

I am using ubuntu. How do I use python 3.13. It says my python version is 3.12 even after installing python 3.13<br>
Someone please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590917)

<a class="mention" href="/u/s.anand">@s.anand</a> sir, I see that the project 1 timeline was changed from February 7 - 17, 2025 to January 17 - February 15 which undoubtedly is a good increase in duration. However, I have my GATE DA exam on Feb 15 and the exam center is unexpectedly far. So, I request you to consider pushing the deadline to at least Feb 16. If not, I’ll still do my best.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/590984)

Hello! <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>
Is the proxy server down right now?<br>
I am getting this error when I am accessing the endpoint:
{‘id’: ‘chatcmpl-Axq55TzulOVjHYuXYIhkRQzCC3PNl’, ‘object’: ‘chat.completion’, ‘created’: 1738824915, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: …, ‘costError’: ‘crypto.createHash is not a function’}
Or, do I have to install crypto module?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591128)

<a class="mention" href="/u/21f3002390">@21f3002390</a> - AI Proxy is working and you <em>did</em> get the result. You can ignore any <code>costError</code>. It won’t happen in the future anyway.
<strong>What’s happening?</strong> I was trying to generate a unique hash for each request, as a precursor to caching requests. But I made a mistake in the code. Specifically, <code>crypto.createHash</code> is not supported in CloudFlare. <a href="https://github.com/sanand0/aiproxy/commit/5943b6d355deffff88ac07d17aa0c6969cacc3d5">I fixed that</a> by removing this. I’ll introduce caching later if required.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591135)

For the question <span class="hashtag-raw">#A8</span> on recognizing the credit card number in the image, Open AI doesn’t seem to be recognizing the number correctly and as a result the evaluation is failing. What should be the solution?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab0a8c362c564a00917bb033bce6ad5ba40d103.png" data-download-href="/uploads/short-url/xuadyQv9NXtkZL0HXLiqBWQ8yaf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab0a8c362c564a00917bb033bce6ad5ba40d103.png" alt="image" data-base62-sha1="xuadyQv9NXtkZL0HXLiqBWQ8yaf" width="690" height="376" data-dominant-color="282827"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×498 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591170)

When will live sessions for demo project start? If started please provide link for that as I am unable to get what the project is about and what are the initial steps to start project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591224)

Getting the following error :
<pre><code class="lang-auto">127.0.0.1 - - [07/Feb/2025 01:44:54] "GET /run?task=generate%20data%20for%20ujanaishik109@gmail.com HTTP/1.1" 200 -
  File "/tmp/datagenyhqKlO.py", line 1
    404: Not Found
    ^^^
SyntaxError: illegal target for annotation

</code></pre>
when executing the following code :
<h2><a name="p-591326-mainpy-1" class="anchor" href="#p-591326-mainpy-1"></a>Main.py</h2>
<pre><code class="lang-auto">@routes.route("/run", methods=["GET", "POST"])
def run():
    task = request.args.get("task")
    try:
        res = get_func_name(task)
        func_name = res["func_name"]
        args = res.get("arguments", [])
        print("ARGUMENTS : ", args)
        if args:
            generated_func = globals()[func_name](*args)
            print("GENERATED FUNC :",generated_func)
            res = f"{func_name} executed successfully"
        else:
            generated_func = globals()[func_name]()
            print(generated_func)
            res = f"{func_name} executed successfully"
    except Exception as e:
        res = None
        print("error : ", e)
    return jsonify(res)

</code></pre>
<h2><a name="p-591326-taskspy-2" class="anchor" href="#p-591326-taskspy-2"></a>Tasks.py</h2>
<pre><code class="lang-auto">def generate_data_files(user_email: str):
    subprocess.Popen(
        [
            "uv",
            "run",
            "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py",
            f"{user_email}",
            "--root",
            "../data",
        ]
    )
    print("data generated successfully")
</code></pre>
Please Guide <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591326)

A query regarding the task description in the query given to LLM for phase A.
For task A3, we have been asked to count wednesdays and the python file corresponding to A3 does count for wednesday alone. However the example says the LLM might be asked to count Sundays or other days. Should we be modifying task A3 code? Or was that just an example and only Wednesdays would need to be counted?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591514)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  Please respond .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591582)

When will the project session be held? If I have missed it, can I get the recording?
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591761)

Tuesday is when we are currently planning a project session.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591780)

Tasks in Phase A are defined but that does not mean it has to do one precise thing. If that was the case then there is no use for an LLM.
Your application should be able to take parse the input and be able to run commands that do similar things in parameterised fashion. It could be Wednesdays or Sundays or it might be in Arabic days or anything. So coding to precisely do something very specific is not the goal.
The program has to be intelligent to do a certain type or class of tasks.
We had a session introducing project. Week 3 session 1. But we will have a more hands on session on Tuesday.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591783)

the last date of project submission is gonne get extended?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591814)

Project 1 was released over a month ago. So there will be no extension for Project 1

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591822)

how to handle this error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb2aa2c67034917f4e124243281661285cbe26a6.png" data-download-href="/uploads/short-url/sZigWPfeWhRLDPlQWlHX2QUBClw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb2aa2c67034917f4e124243281661285cbe26a6.png" alt="image" data-base62-sha1="sZigWPfeWhRLDPlQWlHX2QUBClw" width="690" height="237" data-dominant-color="1B1A1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1425×490 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591824)

<pre data-code-wrap="result"><code class="lang-result">    expected = sum(1 for date in dates if parse(date).weekday() == 2)
    if result.strip() != str(expected):
        return mismatch("/data/dates-wednesdays.txt", expected, result)
    return True```


</code></pre>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> /data/dates-wednesdays.txt<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
129<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“129”
If it is expecting str then why throw error sir  ? <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a><br>
or just tell me how to pass count as an int here
<pre><code class="lang-auto">with open(output_file, "w") as f:
        f.write(str(count)) 
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/591879)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<strong>I am getting below error message from LLM end points <strong><a href="https://api.openai.com/v1/chat/completions" rel="noopener nofollow ugc">https://api.openai.com/v1/chat/completions</a> or <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a></strong> , while running my project .</strong>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png" alt="image" data-base62-sha1="h1TDysFxS8sSBnC3Yk9Z4t6w7u1" width="690" height="25" data-dominant-color="303030"><br>
Kindly help me to resolve this issue. <img src="https://emoji.discourse-cdn.com/google/cry.png?v=12" title=":cry:" class="emoji" alt=":cry:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592061)

<a class="mention" href="/u/carlton">@carlton</a> Will there be evaluation script for tasks in group B also?
Some questions about ‘B’ group tasks:
Q1: For the following tasks (B5, B7, B9, and B10) tasks, how will input files be provided? Will it be URL or will <code>datagen.py</code> also generate files for these?
Q2: For the above tasks as well as for B6 ( Extract data from (i.e. scrape) a website), how should output be returned?
Q3: In task B8, for transcribing audio file, which Python package is recommended or do we need to use OpenAI API?
B5. Run a SQL query on a SQLite or DuckDB database<br>
B7. Compress or resize an image<br>
B8. Transcribe audio from an MP3 file<br>
B9. Convert Markdown to HTML<br>
B10. Write an API endpoint that filters a CSV file and returns JSON data

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592078)

its expecting to  match every single detail in that even " and ’ .<br>
in that case changing evaluate.py will result in zero or less marks.<br>
llm will only handle  -calling function based on query and parameter   . What is it going to do about the logic of functions.
If i still focus on passing evaluate.py will it be any good sir <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>
<pre><code class="lang-auto">🔴 /data/contacts-sorted.json
⚠️ EXPECTED:
[{'first_name': 'Kevin', 'last_name': 'Aguirre', 'email': 'ricardocarlson@example.net'}, {'first_name': 'Andrew', 'last_name': 'Anderson', 'email': 'kimberly08@example.com'}, {'first_name': 'Robert', 'last_name': 'Arnold', 'email': 'hunterpamela@example.com'}, {'first_name': 'Isaac', 'last_name': 'Barker', 'email': 'jessicabriggs@example.net'}, {'first_name': 
</code></pre>
My output was in good looking structured form but I had to make it look like this just to pass the evaluation.
<pre><code class="lang-auto">⚠️ RESULT:
[{"first_name": "Kevin", "last_name": "Aguirre", "email": "ricardocarlson@example.net"}, {"first_name": "Andrew", "last_name": "Anderson", "email": "kimberly08@example.com"}, {"first_name": "Robert", "last_name": "Arnold", "email": "hunterpamela@example.com"}, {"first_name": "Isaac", "last_name": "Barker", "email": "jessicabriggs@example.net"}, {"first_name": "Anthony", "last_name": "Barrett", "email": "kevinknox@example.org"}, {"first_name": "Monique", "last_name": "Bass", "email": "lindsaymcgrath@example.net"}, {"first_name": "Michael", "last_name": "Berry", "email": "an
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592079)

Sorry, sir, not trying to be rude, but there isn’t a single full-fledged project session. It’s a bit difficult to dive into the project without guidance on how to do it. It would be nice to have a full project session where we can start a project from the beginning and follow it to completion.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592372)

Yes. I am very worried about this project. I have been trying to do this. But have gotten nowhere until now.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592385)

<a class="mention" href="/u/carlton">@carlton</a> sir I request you demonstrate atleast few tasks, I spent last 2 days trying to implement but din’t reach anywhere, its really demotivating sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592429)

Can you please demonstrate it by just doing One task or provide sample example code of 1 similar task in the way you explained here. It will be very helpful right now it is very confusing.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592466)

We will be doing project session on <s>Tuesday 9 Feb</s> [correction] Tuesday 11th of Feb (thanks <a class="mention" href="/u/23f1002382">@23f1002382</a> <a class="mention" href="/u/23f2000237">@23f2000237</a>) . Project 1 uses the things you learnt in week 1-3. But mostly week 2 &amp; 3.
We dont do it in the beginning, (but introduced it 2 weeks ago in a live session), to give students chance to practise the new learnings from week 2 &amp; 3.
The plan has always been to demonstrate a few tasks and have you try doing the rest.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592508)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<strong>I am getting below error message from LLM end points <strong><a href="https://api.openai.com/v1/chat/completions" rel="noopener nofollow ugc">https://api.openai.com/v1/chat/completions</a> or <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a></strong> , while running my project .</strong>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png" alt="image" data-base62-sha1="h1TDysFxS8sSBnC3Yk9Z4t6w7u1" width="690" height="25" data-dominant-color="303030"><br>
Kindly help me to resolve this issue. I am unable to proceed with my project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592517)

Today’s 9th Feb and it’s a Sunday.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592531)

<aside class="quote group-faculty" data-username="s.anand" data-post="1" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png" class="avatar"> s.anand:</div>
<blockquote>
<strong>Update: 27 Feb 2025</strong>:
</blockquote>
</aside>
Sir, does this mean 27th is submission deadline?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/592835)

Hi Aindree,
No its a typo (and will be corrected soon). In the context of what was written it clearly means it was <em>updated</em> on 27th January. The update being that the evaluation.py file was provided so that you could test your code against it.
Thanks for bringing it to our attention.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593296)

Hi
This would be only for a selected few questions right because say for the credit card question, where the LLM is involved, to get the card number itself, we have to give a fine-tuned and strong query.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593354)

Try using the eval() function, that seemed to work for me

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593461)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  Sir, could you please share some guidance on the above?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593493)

<a class="mention" href="/u/jivraj">@jivraj</a>,<a class="mention" href="/u/carlton">@carlton</a><br>
I have done the a1 to a10 task and tried querying through localhost and its working fine basically all these ten steps but dont know whether its enough or not. also steps in phase B i am confused that should we create separate endpoints for these tasks or should it be with same /run endpoint and query. then will the input be random by any user. what about the output . where should it be given. phase b needs more explanation.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593507)

At what time will the session be happening tomorrow sir can you please give the details?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593514)

Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Facing some issues in running my project. Taking an example of the Phase A - A3 task.
I am able to read my files through the GET/read/data/dates.txt query.<br>
I am also able to use the count_wednesdays function through the POST/run task/count_wednesdays.
But when I am entering a query such as “count_wednesdays in data/dates.txt” I am unable to get a response.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3409badd267a53d868ee0474c770481d75a98510.png" data-download-href="/uploads/short-url/7qlFPLx7jz367QF7junfCfApvNu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3409badd267a53d868ee0474c770481d75a98510.png" alt="image" data-base62-sha1="7qlFPLx7jz367QF7junfCfApvNu" width="618" height="246"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">618×246 6.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Please advice. Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593593)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0.png" data-download-href="/uploads/short-url/nt1RANtC1bK5k7LPCda2eu3wnHW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0_2_690x63.png" alt="image" data-base62-sha1="nt1RANtC1bK5k7LPCda2eu3wnHW" width="690" height="63" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0_2_690x63.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0_2_1035x94.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a47a14f732c91f801761f2728bdf74f5611c81f0.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1215×112 19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
On task A8, credit-card.png is given, but it is in credit_card.<br>
it makes the errors. I checked that 2 to 3 tasks depend on these, and we create the ouput file with ‘-’ this only. please clarify that output and input files name ‘-’ or ‘_’   <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593646)

On tomorrow live sessions, kindly explain how to use docker, evaluations, github, what generally we have to do submit, please get some tuturials for us to submit those answers. Thankyou Sir  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593647)

(post deleted by author)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593670)

(post deleted by author)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593684)

(post deleted by author)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593685)

<img src="https://emoji.discourse-cdn.com/google/dart.png?v=12" title=":dart:" class="emoji" alt=":dart:" loading="lazy" width="20" height="20"> Score: 9 / 10<br>
Almost done with A tasks. Please use this for local llm to verify output<br>
Also Ollama doesn’t require Schemas<br><br>
CHECK OUT THE REPO AND ANY INPUTS ARE WELCOME<br>
<a href="https://github.com/ANdIeCOOl/TDS-Project-1/blob/checking-with-evaluate.py/README.md" rel="noopener nofollow ugc">Link to ReadMe and also repo</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593686)

Hi Andrew,
You have done a great job with the Phase A tasks. Very methodical, well structured, logical and even incorporates (unnecessarily) two different ways of evaluating its performance via local llm or the project proxy.
I just want to forewarn you (and others who are tempted to just blindly copy and paste) that evaluate.py is not meant to give you an exact expectation of what prompts will be sent to your application.
<strong>In other words getting 10/10 in <code>evaluate.py</code> does NOT guarantee 10/10 or even 5/10  or 1/10 in the real evaluation.</strong>
So do not write your code so rigidly that it will only work in the very strict interpretation of <code>evaluate.py</code>. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general <em>idea</em> of the task.
That said, <code>evaluate.py</code> is a good way to know what to expect. Some of Phase A tasks although given a detailed specification in the project description, will still be given challenging prompts (i.e. hard difficulty, and requires some clever self correcting mechanism). Some of the tasks will be given straight forward prompt (i.e. easy for your application).  Some of the tasks will be given with some level of parameterisation that deviates from the strict interpretation (i.e. medium difficulty).
Hope that helps with how you deal with Phase B tasks (and making your Phase A more robust to a stronger evaluation.)
<strong>A word of caution:</strong> <em>(i.e. this is just some advice, not a set in stone recommendation)</em> Your requirements.txt is massive. If your code does not execute a task (<em>possibly your first task</em>) within 20 seconds (on our server) then it will fail that task. You might want to consider a dynamic, flexible way of installing only required libraries when necessary and keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593709)

Respected <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> and <a class="mention" href="/u/jivraj">@Jivraj</a> ,
Is anyone actively monitoring the Discourse page? I have been raising this issue for the past few days, but there has been no response. Does this mean the TAs are not addressing students’ concerns?
I am encountering the following error while running my project with these LLM endpoints:
<ul>
<li><strong><a href="https://api.openai.com/v1/chat/completions" rel="noopener nofollow ugc">https://api.openai.com/v1/chat/completions</a></strong></li>
<li><strong><a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a></strong><br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/7/775bdd56ec848f8c87546375952710aacc722ba1.png" alt="image" data-base62-sha1="h1TDysFxS8sSBnC3Yk9Z4t6w7u1" width="690" height="25" data-dominant-color="303030"><br>
This issue is blocking my progress, and I urgently need assistance to resolve it. Kindly provide guidance or suggest a solution at the earliest.</li>
</ul>
Looking forward to your response.
Thanks,<br>
Telvin Varghese

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593744)

Hi,<br>
I am not able to understand how to do the Project 1. The date is also very near.
The problem I am facing is, When I did the Modules the page was different, but now in the Project 1 I am not getting any section to submit the project.
Please let me know where are the questions and how tot submit that.<br>
The deadline is near.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593754)

<aside class="quote group-ds-students" data-username="carlton" data-post="103" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
o do not write your code so rigidly that it will only work in the very strict interpretation of <code>evaluate.py</code>. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general <em>idea</em> of the task.
</blockquote>
</aside>
This where I need help, i tried doing with agentic framework but i failed with the model in llm proxy, which was highly suspect because, that model should have known what the uv framework but it seemed to me to be outdated. Hence executing code Interpreter tools failed as the model gave outdated code. I have raised this issue before
Hence i moved to function calling, using local llms as cost-effective solution and it was quite robust.
I just need to understand how the function should be general, maybe 2-3 tasks you could provide the general description along with all the ways one would query the agent llm(ie our project). This general function is what i need help with. Please kindly do the needful.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593756)

<aside class="quote group-ds-students" data-username="carlton" data-post="103" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.
</blockquote>
</aside>
Any tentative size cutoff for the docker image?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593765)

Hi Telvin
You have run out of tokens. Thats what the message is saying. You ran out 3 days ago. It was clearly mentioned that the limit is $1. You have exceeded $2.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05.png" data-download-href="/uploads/short-url/3UT9vulaDP4aGOL6pZaeJ0PSs7z.png?dl=1" title="Screenshot 2025-02-11 at 3.36.50 pm" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05_2_690x423.png" alt="Screenshot 2025-02-11 at 3.36.50 pm" data-base62-sha1="3UT9vulaDP4aGOL6pZaeJ0PSs7z" width="690" height="423" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05_2_690x423.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05_2_1035x634.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b74cf0c060e28cd3459173bce28d123a8d5da05_2_1380x846.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-11 at 3.36.50 pm</span><span class="informations">2078×1276 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
In our current internal build of project 1, we have yet to exceed $0.50
As to whether it can be renewed is something we have still not yet decided, because the question you have raised equally would apply to everyone. Raising it for you means raising it for everyone. $1 for everyone equals raising it by $1600+ <em>(i.e Rs 1.39 Lakhs)</em> for us!
The budget question then involves more than one person. It also involves the BS Team Operations and not just the TDS team and therefore instead of responding with a response that is not useful, we typically try to solve the problem first and then respond.
In short we are working on it. But as we have mentioned repeatedly in our sessions, use APIs efficiently, thats part of the skill. As soon as we have a resolution we will inform everyone via an announcement and an email.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593802)

Thanks for your response, <a class="mention" href="/u/carlton">@Carlton</a>. It seems I won’t be able to proceed with the project until this issue is resolved. Also, I haven’t used LLM so much until February 7th to cost $2.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593807)

Every request you send, gives you a response back with exactly how much that request cost. So you can track your usage.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593809)

I’m aware of that. I’ve mostly noticed a cost of $0.0003 per request, so I haven’t been tracking my total monthly expenses. Moving forward, I’ll keep a record of the cost for each request. Also, do strong prompts impact the overall cost?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593816)

<a class="mention" href="/u/carlton">@carlton</a> Is the project session happening today? I don’t have the link. Can you please send it if it’s happening?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593820)

Hi, where is the link for todays Project 1 demo session? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593821)

<a href="https://meet.google.com/odh-ycbm-ahj?authuser=0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://meet.google.com/odh-ycbm-ahj?authuser=0</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593822)

<h1><a name="p-593823-request-1" class="anchor" href="#p-593823-request-1"></a>request</h1>
<pre><code class="lang-auto">http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt](http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt)
</code></pre>
<h1><a name="p-593823-output-2" class="anchor" href="#p-593823-output-2"></a>output</h1>
<pre><code class="lang-auto">{    "detail": "Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_issuer'}}"}
</code></pre>
<a class="mention" href="/u/carlton">@carlton</a> sir I am getting this issue while running my script. Please help!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593823)

I’m getting an error in task a2, def do_a2():<br>
“”“Format markdown using prettier”“”<br>
format_md_path = DATA_ROOT / “format.md”<br>
subprocess.Popen([“prettier”, str(format_md_path), “–write”, “–parser”, “markdown”])<br>
print(“data formatted successfully”)
any idea how to fix this? Also in A8, a 5 and a 3 is getting interchanged. Can someone help why that is hapening, I changed the prompt to include caution about not switching 3 and 5 as well, that didn’t help either

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593826)

what is  the session time?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593832)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/7/b7b024074300d61b0df1d7ebf727f9cfb8fcceae.png" data-download-href="/uploads/short-url/qcYKVrgkNokn9jbch4vRvh7U3Aq.png?dl=1" title="Screenshot 2025-02-11 181453" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/7/b7b024074300d61b0df1d7ebf727f9cfb8fcceae.png" alt="Screenshot 2025-02-11 181453" data-base62-sha1="qcYKVrgkNokn9jbch4vRvh7U3Aq" width="690" height="97" data-dominant-color="181518"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-11 181453</span><span class="informations">1459×207 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Could you kindly help me with this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593836)

in checking for the task of json my code is outputting json with double quotes (valid json) and evaluate.py has exact same json but with single quotes , what should I do?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593884)

check out my repo and download the datagen and evaluate file for testing

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593885)

it should work, use fastapi text response when /read api

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593886)

Has anyone used a local LLM for testing? If so, could you please share the request URL and the request body format? I attempted to use a local LLM, but I was unable to succeed

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593897)

use ollama it is openai api compatible, supports function calling without json schema for tool usage. Check it out

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593911)

NEED HELP. CAN SOMEONE CONTACT OLLAMA AND ASK THEM TO CHECK THEIR CODE ITS HAS SOME SILLY MISTAKES IN CODE EXAMPLES. I DONT KNOW HOW TO DO IT.
<a href="https://ollama.com/blog/embedding-models" rel="noopener nofollow ugc">LINK TO PAGE WITH CODE EXAMPLE</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png" data-download-href="/uploads/short-url/5F1hzxksDi54nBGls5d6m6F2hyu.png?dl=1" title="Screenshot 2025-02-11 232608" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/7/27adf05313946c445fec614cd1fd17ba6c1f4cde.png" alt="Screenshot 2025-02-11 232608" data-base62-sha1="5F1hzxksDi54nBGls5d6m6F2hyu" width="643" height="499" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-11 232608</span><span class="informations">919×714 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<br><br><br>
correct code in step 2 collection query step
<pre><code class="lang-auto">response = ollama.embed(
  model="nomic-embed-text:latest",
  input=task
)
results = collection.query(
  query_embeddings=response["embeddings"], #here embeddings and also not list of list as response embeddings already gives correct format
  n_results=1
)
data = results['documents'][0][0]
</code></pre>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593930)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
While implementing the Phase B tasks, can I take the data (csv file, git repo, audio, sqlite/duckdb database, website, image and markdown file) of my choice and perform any operation on them as long as they meet the critetia mentioned in the Phase B task list? Please guide.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593963)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
In the Task B5, where we have to run an SQL query on a sqlite or duckdb database, should I create a database on my own and then take the query to be ran on it as an argument? Or should I take the query as an argument and run it on the ticker_sales.db in ./data folder? Please guide

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593966)

same issue on my side as well

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593967)

on using the AIPROXY_TOKEN from here <a href="https://aiproxy.sanand.workers.dev/" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/</a>
getting this error :
Error: Your authentication token is not from a valid issuer.
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  please help!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593968)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> Can the link to the live session (for project) be provided?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593971)

As in the previous session for task a1 we use llm just to get the url and email , so after retriving the both arguments can i use them in a function and got the work given in work done in function.<br>
Also, am i correct that we use llm only to retrive url or location ??
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593972)

Anyone whom have done have done any one task of phase a and one task of phase b, please help…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593974)

Can you do one task from each phase in today’s session. Please <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593976)

thanks for the reply I will check

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593977)

TDS project <img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> Tedious project <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593981)

can anyone share the link of yesterdays live session if there in youtube

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593993)

Its updated in the TDS live sessions playlist
<div class="youtube-onebox lazy-video-container" data-video-id="jXj6bqy4R4c" data-video-title="2025-02-06 Week 5 - Session 1 - TDS Jan 25" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jXj6bqy4R4c" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b990ffaadbfcbad12d865c514f3d6b48e5bc7cf2.jpeg" title="2025-02-06 Week 5 - Session 1 - TDS Jan 25" data-dominant-color="595C5F" width="690" height="388">
  </a>
</div>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/593997)

<em>For task A2</em>:
<ul>
<li><strong>A2</strong>. Format the contents of <code>/data/format.md</code> using <code>prettier@3.4.2</code>, updating the file in-place</li>
</ul>
I am getting the following error:<br>
<code>🔴 A2 failed: Command '['npx', 'prettier@3.4.2', '--stdin-filepath', '/data/format.md']' returned non-zero exit status 1.</code>
However, running a <strong>POST request</strong> to <a href="https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2" rel="noopener nofollow ugc">https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2</a> gives successful output.
<code>{"success":true,"message":"Formatted and verified successfully!"}% </code>
Here is my code snippet:
<pre data-code-wrap="py"><code class="lang-py">def format_file(filepath):
    while True:  # Loop until formatting and verification pass
        try:
            result = subprocess.run(
                ["npx", "prettier@3.4.2", "--write", filepath],
                check=False,  # Don't raise exception automatically
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {"success": False, "message": f"Prettier write failed: {result.stderr}"}

            if verify_prettier_formatting(filepath):
                return {"success": True, "message": "Formatted and verified successfully!"}
            else:
                logging.info("Verification failed. Retrying formatting...") #Log the retry
                # If verification fails, the loop continues and prettier --write is executed again.

        except Exception as e:
            return {"success": False, "message": str(e)}

def verify_prettier_formatting(filepath):
    try:
        subprocess.run(["npx", "prettier@3.4.2", "--check", filepath], check=True, capture_output=True, text=True) #Capture output
        return True  # File is formatted correctly
    except subprocess.CalledProcessError as e:
        logging.error(f"Prettier check failed: {e.stderr}") # Log the error from prettier check
        return False  # File is not formatted correctly
</code></pre>
What am I missing here?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594022)

I am getting the same error. Did you find any solution?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594041)

Has anyone succeeded in the extraction of credit cards details task? The LLM seems to consider it as illegal task and if I use pytessaract the docker image size will become really large. What to do in this case?
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594042)

Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>,
I followed what you taught in Feb 11 session and tried implementing task A1. My understanding is once i run the subprocess, datagen.py file should be run and /data folder should be created in the project folder. But it is not happening to me. I am getting the following error
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/datagen4COEF3.py", line 284, in &lt;module&gt;
    os.makedirs(config["root"], exist_ok=True)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "&lt;frozen os&gt;", line 227, in makedirs
OSError: [Errno 30] Read-only file system: '/data'
</code></pre>
If i can’t automate this process, i don’t see the point writing code for other tasks. Can anyone help me solving this error?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594043)

shell = true in evaluate.py, remove it meaning comment it out, task a2 thats causing the error

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594045)

the admin banned me from using laughing emoji  <a class="mention" href="/u/jkmadathil">@jkmadathil</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594046)

For task A6,
<blockquote>
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/docs/index.json" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/docs/index.json</a> “HTTP/1.1 200 OK”
</blockquote>
<pre><code class="lang-auto">⚠️ EXPECTED:
{'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}
</code></pre>
<pre><code class="lang-auto">⚠️ RESULT:
{'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}
</code></pre>
If I am not wrong, both the expected and actual result contain the same entries. It is just that the ordering is different. The expected result also doesnt follow any particular format (so does the actual result).
Kindly advise on this <a class="mention" href="/u/carlton">@carlton</a>
<strong>EDIT</strong> : Resolved on a later evaluation

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594057)

For the task - * <strong>B10</strong>. Write an API endpoint that filters a CSV file and returns JSON data
Do we have to handle prompts for converting CSV to JSON or for writing an endpoint for doing so?
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594058)

yeah i am also facing the same doubt

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594061)

+1…<br>
<a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594062)

could someone please share their repo for reference. it would be very much helpful

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594068)

Dear Instructors (<a class="mention" href="/u/carlton">@carlton</a>, <a class="mention" href="/u/iamprasna">@iamprasna</a>):
Confirming, just to be needfully pedantic:
It will <strong>solely</strong> be the responsibility of the Project Evaluator (human or machine) to parse the correct <code>AIPROXY_TOKEN</code> generated against my IITM email ID (presumably, per some database which holds all such generated <code>AIPROXY_TOKEN</code>s of the students who have generated one); and the correct <code>$IMAGE_NAME</code> (to-be-submitted by myself in the Project Submission Google Form) in <code>podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000</code>, correct?
Asking this seemingly obvious question, as (apparently) the actual <code>AIPROXY_TOKEN</code> is not to be included anywhere in the code, or the repository, or the dockerfile.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594069)

I am also facing the same issue, just that the ordering is different.<br>
Sorting by keys also didn’t help.<br>
Please help on this <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594074)

sir will the tasks of Phase A and Phase B change? like currently do we need to make llm write the code for all tasks dynamically or can we write a pre defined python code to execute tasks after the llm parses the task and runs python code

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594086)

Check length of result and length of expected, one is 98 and other is 298
<pre><code class="lang-auto">expected = {'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}
result  = {'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}
print(len(set(result)), len(set(expected)))
count = 0
print("length of result", len(result))
print("length of expected", len(expected))
for y in result:
    if y not in expected:
        count += 1
        print(f"{y}:{result[y]} IS EXTRA FILE")
        print(count)
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594087)

<aside class="quote group-faculty" data-username="s.anand" data-post="1" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png" class="avatar"> s.anand:</div>
<blockquote>
A <em>sample</em> evaluation script for Project 1 tasks A1-A10 is available at <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" rel="noopener nofollow ugc">tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub</a>
</blockquote>
</aside>
Sir there is an error in the evaluation script for task A1, url - <a href="https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py" rel="noopener nofollow ugc">https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py</a> doesn’t exist,<br>
instead this should - <a href="https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py" rel="noopener nofollow ugc">https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594091)

<a class="mention" href="/u/23f2001978">@23f2001978</a>
That error is usually if you are using the wrong endpoint (ie. using open ai libraries instead of sending requests to aiproxy).
Without seeing the request its hard to tell you what the cause of the error is.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594109)

<a class="mention" href="/u/21f2000709">@21f2000709</a> <a class="mention" href="/u/23f1002382">@23f1002382</a>
B10 → Create a service that creates a specified endpoint that receives a CSV and returns a JSON data . Where the JSON is expected, whether in the response body of the endpoint , or in a file will be specified by the task master <img src="https://emoji.discourse-cdn.com/google/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594121)

hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
for A2 i am getting this particular error and i don’t know what i am doing wrong in this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90.png" data-download-href="/uploads/short-url/a1qItFSCXcfheeTQHIxQNQK6b84.png?dl=1" title="Screenshot from 2025-02-12 19-31-47" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90_2_690x259.png" alt="Screenshot from 2025-02-12 19-31-47" data-base62-sha1="a1qItFSCXcfheeTQHIxQNQK6b84" width="690" height="259" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90_2_690x259.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90_2_1035x388.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/6/463f25f29e9ac0e51e43914eb00cef2e89341c90_2_1380x518.png 2x" data-dominant-color="1B1B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-12 19-31-47</span><span class="informations">1501×564 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594129)

issue with evaluate.py , post the code snippet in task a2, where it calculates the result and checks with expected.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594131)

you mean screenshot of evaluate.py file?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/18e7419bec3e953904b029c887a657f57b376377.png" data-download-href="/uploads/short-url/3yiVgj5MK4I0OIhWEkiH5rjnAJF.png?dl=1" title="Screenshot from 2025-02-12 20-21-56" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/18e7419bec3e953904b029c887a657f57b376377_2_690x259.png" alt="Screenshot from 2025-02-12 20-21-56" data-base62-sha1="3yiVgj5MK4I0OIhWEkiH5rjnAJF" width="690" height="259" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/18e7419bec3e953904b029c887a657f57b376377_2_690x259.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/18e7419bec3e953904b029c887a657f57b376377_2_1035x388.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/18e7419bec3e953904b029c887a657f57b376377_2_1380x518.png 2x" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-12 20-21-56</span><span class="informations">1501×564 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594133)

running in docker?<br>
////////////////////////////

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594143)

Yes, I commented out check=True to see the error

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594144)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
could you please help me out on how to start with TDS Project-1, as I am stuck at the moment and don’t know where to start from. This project is very much unfamiliar for me and I need some guidance on how to start with it. It would be really great if you could provide some help through resources/materials/videos and help me complete the project. Thanks in advance!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594158)

then im not sure exactly wait lemme check

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594167)

issue with evaluate py, specifically , how it formats the file, maybe shell=True should be uncommented if commented out. then im not sure. Im not in composing docker files yet

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594169)

Could anyone please help me with the project… I am trying to do it but I’m always getting errors even while starting.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594177)

My final docker image size is coming 1.25 gb, I am using the ubuntu base image as I thought it would be appropriate given the tasks. Is it ok with that size?
PS - Also I would be running out of token if I need to test again with some other base image now.<br>
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594189)

Go through the week 1-3 assignments once, you would be good to go with Phase A tasks.
<a class="mention" href="/u/23f2003413">@23f2003413</a> <a class="mention" href="/u/anvithav">@AnvithaV</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594190)

You do not need the whole of ubuntu!
Just python and uv
More like 128mb image.
Please watch Tues week 5 session 1
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594192)

Will there be more live sessions on project ?
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594194)

I could pull it down to 610 mb, using python:3.9-slim now, but there are some essential libraries that is needed which is taking up the space…will it be ok? I mean installing on the go with uv might lead to timeout during evaluation…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594196)

How did you corrected it ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594202)

I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594210)

could you help later, when i need to construct docker image, via gmeet? PLEASE

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594215)

ANY SUGGESTIONS (just one digit away) ::
<pre><code class="lang-auto">import easyocr
from pathlib import Path
import re

def extract_credit_card_number(input_image: str, output_file: str):
    
    input_path = Path(f".{input_image}")
    output_path = Path(f".{output_file}")

    if not input_path.exists():
        raise ValueError(f"Image file {input_path} does not exist.")

    # Step 1: Use OCR to extract text from the image
    reader = easyocr.Reader(['en'])
    try:
        result = reader.readtext(str(input_path))
    except Exception as e:
        raise ValueError(f"OCR processing failed: {str(e)}")

    # Combine all extracted text into a single string
    extracted_text = " ".join([text for (_, text, _) in result])

    # Step 2: Use the LLM to refine the extracted text and extract the credit card number
    prompt = f"""
    The following text was extracted from an image. It may contain a credit card number. 
    Extract the credit card number and return only the number without spaces or dashes. 
    If no credit card number is found, return "None".

    Extracted text: {extracted_text}
    """
    try:
        response = chat_completion(prompt)
        card_number = response.get("choices", [])[0].get("message", {}).get("content", "").strip()

        # Validate the card number (basic check for 16 digits)
        if card_number.lower() == "none" or not card_number.isdigit() or len(card_number) != 16:
            raise ValueError("No valid credit card number found in the image.")

        # Write the card number to the output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(card_number)

        return f"A8 Completed: Credit card number extracted and written to {output_file}"
    except Exception as e:
        raise ValueError(f"Failed to process text with LLM: {str(e)}")
</code></pre>
<pre><code class="lang-auto"> /data/credit-card.txt
⚠️ EXPECTED:
4026399336539356
⚠️ RESULT:
4026399338539356
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594216)

&lt;Response [200]&gt;<br>
{‘id’: ‘chatcmpl-B0De8V66WZAucAweJe6e32BWSLnpT’, ‘object’: ‘chat.completion’, ‘created’: 1739392156, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: “I’m sorry, but I can’t assist with that.”, ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘stop’}], ‘usage’: {‘prompt_tokens’: 874, ‘completion_tokens’: 11, ‘total_tokens’: 885, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.048128640000000014, ‘cost’: 0.0026880000000000003, ‘monthlyRequests’: 51}
<pre><code class="lang-auto">def query_gpt_image(image_path: str, task: str):
    print("🔍 Image Path:", image_path)
    image_format = image_path.split(".")[-1]
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {"APIKEY"}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": task},
                    {
                    "type": "image_url",
                    "image_url": { "url": f"data:image/{image_format};base64,{image_data}" }
                    }
                ]
                }
            ]
            }
                     )
    response.raise_for_status()
    print(response)
    print(response.json())
    result = response.json() 
response = query_gpt_image("data/credit_card.png","Extract the credit card number from image")
</code></pre>
Why is this not working?<br>
EDIT: Requires prompt engineering as “credit card” is sensitive information <img src="https://emoji.discourse-cdn.com/google/roll_eyes.png?v=12" title=":roll_eyes:" class="emoji" alt=":roll_eyes:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/roll_eyes.png?v=12" title=":roll_eyes:" class="emoji" alt=":roll_eyes:" loading="lazy" width="20" height="20">
&lt;Response [200]&gt;<br>
{‘id’: ‘chatcmpl-B0Dlie1ZIS68PZBCT0XJKhLKbyPAC’, ‘object’: ‘chat.completion’, ‘created’: 1739392626, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: ‘The numbers extracted from the image are:\n\n- 3009 1429 5211 59\n- 09/29\n- 113’, ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘stop’}], ‘usage’: {‘prompt_tokens’: 871, ‘completion_tokens’: 31, ‘total_tokens’: 902, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.05092764000000002, ‘cost’: 0.002799, ‘monthlyRequests’: 52}
<pre><code class="lang-auto">response = query_gpt_image("data/credit_card.png","Extract number from image")
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594218)

Sir in main.py file I’m defining task with different variables . But in evaluate.py tasks are defined by different variables to test and when I’m testing it using python evaluate.py it returns unsuccessful . I’m testing all my tasks of main.py with Postman it returns successful.<br>
My query is that how the tasks get evaluated and do i need to change my variables in main.py ? And what are the other things i have to change.<br>
Also plss update evaluate.py fie with phase B tasks
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594228)

<a class="mention" href="/u/22f3001777">@22f3001777</a>
Yes there will be one more session today (13th Feb) at usual time 8pm to 10pm
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594235)

Hi instructors and TAs,<br>
For the different tasks in Phase B, I don’t have a clear idea of what type of a response you expect.
eg.
<ul>
<li>Run a SQL query on a SQLite or DuckDB database &amp; Extract data from (i.e. scrape) a website &amp; Transcribe audio from an MP3 file - Do you want the query’s response on an output file like A10? or as a response?</li>
</ul>
I understand that these are broad problems you except us to solve, but it would be helpful to know what type of response you would require.
Thanks,<br>
Trebhuvan

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594241)

Hi,<br>
Pls tell us how to use evaluate.py script to check our codes

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594247)

Output specifications will be detailed in the “task” sent to the endpoint.
Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve <em>all tasks using the same function</em> !
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594250)

Okay sure!! Ping me when you require to generate…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594252)

Hello sir,<br>
Is yesterday’s session not uploaded to YouTube yet ?<br>
I couldn’t find it in calendar either… It will be very helpful if you (or anyone else) could provide yesterday session’s recording’s link…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594254)

<aside class="quote group-ds-students" data-username="21f2000709" data-post="174" data-topic="164277" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png" class="avatar"> 21f2000709:</div>
<blockquote>
I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb
</blockquote>
</aside>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
will it be ok? Actually I developed it in a way that require some of the essential dependencies and at this point of time it would be dangerous to alter the way of handling it as I am running short of AIProxy Token credits.
Earlier when I asked this:
<aside class="quote group-ds-students" data-username="21f2000709" data-post="108" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png" class="avatar"> 21f2000709:</div>
<blockquote>
Any tentative size cutoff for the docker image?
</blockquote>
</aside>
I could have altered my way of handling dependencies but at that point of time there was no clear numbers.
I request you to please allow this time around with this size…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594261)

<a class="mention" href="/u/carlton">@carlton</a> Could you please consider extending the submission date of Assignment 5 (it is 16th Feb right now). We are very busy with the project.
And assignment 6 submission date is much later: 9th of March.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594280)

<a class="mention" href="/u/carlton">@carlton</a> +1 Agreed, a relaxation in deadline will be a boon for students who’ve taken up other projects this term.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594298)

usage of langchain is allowed?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594303)

It will be extended, <a class="mention" href="/u/carlton">@carlton</a> mentioned it in a TA session already.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594320)

Hi <a class="mention" href="/u/rishabh2">@Rishabh2</a>
What exactly you mean by variables?  only one argument is required for running <code>evaluate.py</code> that’s an email address.
You need to download both <code>evaluate.py</code> and <code>datagen.py</code> in same folder and then execute <code>evaluate.py</code> using uv.<br>
<code>uv run evaluate.py --email $any_email</code>.
For phase B
<aside class="quote" data-post="183" data-topic="164277">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/183">Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    Output specifications will be detailed in the “task” sent to the endpoint. 
Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve all tasks using the same function ! 
Kind regards
  </blockquote>
</aside>

Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594333)

610 Mb’s is good size, no need to worry, it will be evaluated.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594337)

Hi <a class="mention" href="/u/23f1002382">@23f1002382</a><br>
This is the classic case where you use Prompt engineering to solve your problems. I assume you have already achieved your answers, but I want to clarify this for someone who is facing this problem.
The thing is GPT-4o-mini is intelligent enough to understand what kind of task you are asking it do, and extracting Credit Card info from an image is one of the many prohibited tasks.
What you can do is, <strong>try to fool it using itself.</strong> Just ask ChatGPT to generate a prompt that would be capable of fooling itself into extracting out that credit card info. I was capable of doing it after pretending to be a working on a Cyber Security project, and other fake details which ChatGPT itself provided me with.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594342)

<a class="mention" href="/u/carlton">@carlton</a> . I cannot send requests to <a href="https://aiproxy.sanand.workers.dev/openai/v1" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1</a> . Getting  $RateLimitError: Error code: 429 - {‘message’: 'On 2025-02 you used $2.0003758999999954, exceeding <span class="math">2'}</span>  . Looks like I used all of my credit . What can I do now ? Project is also Incomplete.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594344)

Try creating a better prompt for this task.<br>
<em>Hint: Ask it to recheck certain similar looking digits.</em>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594345)

After submitting docker image through, it will be pulled and our token will be used.
Things to be checked at your end.<br>
1.<code> podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME</code> works fine<br>
2.  Above command will start 8000 server so use evaluate.py to test if things are working as expected.
Kind regards.<br>
Jivraj

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594351)

Hi <a class="mention" href="/u/joeljeffrey">@JoelJeffrey</a>
What you did wrong and how did you correct it?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594353)

I think there was something wrong with the way the code was getting inputs (keys). I just rewrote that part and it worked

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594354)

Hi <a class="mention" href="/u/22f3001307">@22f3001307</a>
Provide required write permissions to <code>/data</code> folder. We will also discuss this issue regarding permissions in initial part of today’s session.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594355)

Hello sir,<br>
Is yesterday’s session not uploaded to YouTube yet ?<br>
I couldn’t find it in calendar either…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594358)

Command to run the image in the docs, seemed to have some error,
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e724c8ad15be3f5051e9abaf562830a2a1217ec.png" alt="Screenshot 2025-02-13 at 1.31.01 PM" data-base62-sha1="23Nzhqv7fQsw7MQIWGUG4ZEkERS" width="690" height="75" data-dominant-color="353F44">
The command:<br>
<code>podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000</code>
gives the error:<br>
<code>crun: executable file `-e` not found in $PATH: No such file or directory: OCI runtime attempted to invoke a command that was not found</code>
However the correct command seems to be:<br>
<code>podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME</code>
This works totally fine.
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf9060b0880a8d94e57a14ce300b4dcc714ed117.png" alt="Screenshot 2025-02-13 at 1.33.21 PM" data-base62-sha1="tCcab37inD3OmPbAYgJPLdNROyb" width="690" height="45" data-dominant-color="252525">
<a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594359)

nvm i can laugh nw xD

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594361)

One final question <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> , will our projects be evaluated with our <code>AIPROXY_TOKEN</code> or a different one.
Because my project is done but for evaluation if my <code>AIPROXY_TOKEN</code> is used, it might be out of credits.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594372)

Thanks. Do you know the new date?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594378)

That wasn’t said, but it was not this weekend for sure.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594385)

my automation is happening and prompt distribution too but it just isnt able to pass any test after 1st in evaluation.py did someone else face same problem if yes then how to solve it please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594394)

actually that easyocr is directly sending the clear text(no confusion) to llm and llm is just extracting the  exact numbers from it .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594398)

[quote=“23f2001975, post:211, topic:164277, full:true”]<br>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a><br>
While running the evaluation.py i am facing several issues because my output isnt strictly adhering sometimes to it will the checking be on such a basis only
for example in A3<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
129<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“129”<br>
this is the error i get while it is the function in eval.py checking problem as it gets response as text and doesnt strip (“”)
Please guide what should i do

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594409)

<aside class="quote group-ds-students quote-modified" data-username="21f2000709" data-post="202" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png" class="avatar"> 21f2000709:</div>
<blockquote>
podman run -e AIPROXY_TOKEN=“$AIPROXY_TOKEN” -p 8000:8000 $IMAGE_NAME
</blockquote>
</aside>
Yes this is correct command, we will update in project page.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594416)

<aside class="quote" data-post="196" data-topic="164277">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/164277/196">Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025]</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    After submitting docker image through, it will be pulled and our token will be used. 
Things to be checked at your end. 
1. podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME works fine 
2.  Above command will start 8000 server so use evaluate.py to test if things are working as expected. 
Kind regards. 
Jivraj
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594420)

<a class="mention" href="/u/jivraj">@Jivraj</a> sir I get this error<br>
but my app.py is able to get the server running on localhost and not on 0.0.0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/d/ed519f25f712a007f48e1e2f3cf5cf7f946271cb.png" data-download-href="/uploads/short-url/xRq27aO3iKC8e2tH9JXnzpGWF0T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/d/ed519f25f712a007f48e1e2f3cf5cf7f946271cb.png" alt="image" data-base62-sha1="xRq27aO3iKC8e2tH9JXnzpGWF0T" width="690" height="129" data-dominant-color="222425"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1014×190 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
could you please help ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594421)

When i am trying evaluate the code, I am getting the following error
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/evaluateyea70I.py", line 20, in &lt;module&gt;
    from datagen import (
    ...&lt;9 lines&gt;...
    )
ModuleNotFoundError: No module named 'datagen'
</code></pre>
can someone tell me what i should do?<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594422)

<a class="mention" href="/u/22f3001307">@22f3001307</a><br>
Install datagen.py in the same folder from where you are executing evaluate.py.
<a class="mention" href="/u/vikramjncasr">@vikramjncasr</a> Check how you are executing, use uv or else install required modules globally<br>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594424)

Sir,<br>
the folder already exists in that folder<br>
besides, I am using <code>OPENAI_API_KEY=$AIPROXY_TOKEN uv run https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py</code> from Anand sir’s page to run the code in my system

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594426)

Sir would the belowformat be ok when you evaluate ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/58c6872accc838dcec5fda23f4290f5e284dde1e.png" data-download-href="/uploads/short-url/cFlmqgkVc1erxEuGI9rlgBaGA9M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/58c6872accc838dcec5fda23f4290f5e284dde1e.png" alt="image" data-base62-sha1="cFlmqgkVc1erxEuGI9rlgBaGA9M" width="690" height="147" data-dominant-color="292726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">985×211 24.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594427)

But when I use podman i keep getting errror.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594428)

Hello,
Can anyone please reset my AIProxy limit. I am getting this error, {“detail”:“Agent error: 429 Client Error: Too Many Requests for url: <a href="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/chat/completions</a>”}<br>
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594438)

i am getting unauthorized error in A9 again and again, i have pasted my code if someone can help please look into this.
<pre><code class="lang-auto"># /// script
# requires-python = "&gt;=3.11"
# dependencies = [
#   "numpy",
#   "httpx",
#   "fastapi",
# ]
# ///


import httpx
import numpy as np
import datetime
import os

from fastapi import HTTPException


now = datetime.datetime.now()

OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"


# async def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -&gt; float:
def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -&gt; float:
    # """Calculate cosine similarity between two texts."""
    # emb1 = await embed(text1)
    # emb2 = await embed(text2)
    return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))


# async def embed_list(text_list: list[str]) -&gt; list[float]:
async def embed_list(text_list: list[str]) -&gt; list[float]:
    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    """Get embedding vector for text using OpenAI's API."""
    try:
        async with httpx.AsyncClient() as client:
            # with httpx.AsyncClient() as client:
            response = await client.post(
                # response = httpx.post(
                OPENAI_API_URL,
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                
                json={"model": "text-embedding-3-small", "input": text_list},
            )
        # print(f'{response.json()["data"][0]["embedding"]}')
        emb_list = [emb["embedding"] for emb in response.json()["data"]]
        print(f"Number of embeddings returned = {len(emb_list)}")
        return emb_list

    except KeyError as e:
        print(f"INSIDE EMBED_LIST IN A9. KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(f"INSIDE EMBED_LIST IN A9. General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def most_similar(embeddings):
    # Extract the phrases and their corresponding embeddings
    phrases = list(embeddings.keys())
    emb_values = list(embeddings.values())

    # Initialize variables to track the maximum similarity
    max_similarity = -1  # Start with the smallest possible similarity value
    most_similar_pair = None

    # Compute cosine similarity between each pair of embeddings
    for i in range(len(emb_values)):
        for j in range(i + 1, len(emb_values)):  # Avoid repeating pairs
            similarity = get_similarity_from_embeddings(emb_values[i], emb_values[j])
            if similarity &gt; max_similarity:
                max_similarity = similarity
                most_similar_pair = (phrases[i], phrases[j])

    return most_similar_pair


# async def get_similar_comments(input_file_path: str, output_file_path: str):
async def get_similar_comments(input_file_path: str, output_file_path: str):
    print(f"Reading the input file: {input_file_path}")
    with open(input_file_path, "r") as file:
        comments = file.readlines()

    print(f"Embedding the comments")
    # embeddings = await embed_list(comments)
    embeddings = await embed_list(comments)
    embed_dict = dict(zip(comments, embeddings))
    most_similar_pair = most_similar(embed_dict)
    print(f"Most similar comments: {most_similar_pair}")

    with open(output_file_path, "w") as file:
        for comment in most_similar_pair:
            file.write(f"{comment.strip()}\n")
        # file.write(f"Most similar comments: {most_similar_pair}")


if __name__ == "__main__":
    # import asyncio

    input_file_path = "/data/comments.txt"
    output_file_path = "/data/similar_comments.txt"
    # asyncio.run(get_similar_comments(input_file_path, output_file_path))
    get_similar_comments(input_file_path, output_file_path)
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594439)

<a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a> sir can you take my doubt in today’s session please , i have successfully run docker server but endpoints are not working…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea.png" data-download-href="/uploads/short-url/yO2xtMBVAwea8Bpo3rTBKumTB5U.png?dl=1" title="Screenshot 2025-02-13 165912" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea_2_690x368.png" alt="Screenshot 2025-02-13 165912" data-base62-sha1="yO2xtMBVAwea8Bpo3rTBKumTB5U" width="690" height="368" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea_2_690x368.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea_2_1035x552.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f3f203d53c41f1d3c7c214f4904ca32579085bea_2_1380x736.png 2x" data-dominant-color="1E1E1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-13 165912</span><span class="informations">1917×1024 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If anyone have knowledge about this , please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594447)

How did u resolve the issue?  <a class="mention" href="/u/joeljeffrey">@JoelJeffrey</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594449)

I am also facing the same issue.<br>
Evaluation Output:
<pre><code class="lang-auto">HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

❌ A9 FAILED
</code></pre>
I sense ‘Authentication Problem’ happens only with the evaluation script, as the curl requests seems to work fine.
<pre><code class="lang-auto">INFO:httpx:HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60849 - "POST /run?task=%60%2Fdata%2Fcomments.txt%20contains%20a%20list%20of%20comments,%20one%20per%20line.%20Using%20embeddings,%20find%20the%20most%20similar%20pair%20of%20comments%20and%20write%20them%20to%20%2Fdata%2Fcomments-similar.txt,%20one%20per%20line HTTP/1.1" 200 OK
</code></pre>
Any views? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594451)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> Sir i keep getting this error<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/acf1856ac9b092f16e614440286674227fb05f45.png" data-download-href="/uploads/short-url/oFVA3JKtDSmA2FNzMT1OoeZWyHj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/acf1856ac9b092f16e614440286674227fb05f45.png" alt="image" data-base62-sha1="oFVA3JKtDSmA2FNzMT1OoeZWyHj" width="671" height="109"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">671×109 8.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
even though i have downloaded the packages globally and tried installing them by making a venv but nothing seems to work please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594512)

what is the base url?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594531)

use your api key guys

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594556)

we are using that only bro, only for A9 it says unauthorized

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594557)

network mapping or something, even im working that out

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594558)

Even i am facing the same problem. I am unable to resolve it ,i tried many ways.<br>
could anyone please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594559)

2 ways, try command line package installing, or inside venv, try which python,etc and make paths reconcile, or inside venv, uv pip install , if that doesn’t work, inside venv pip install 

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594561)

thanks , already it work out

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594564)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> sir please help
When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?<br>
needs sudo permission all the time…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c.png" data-download-href="/uploads/short-url/bMJwuO7QKs4EnTOSYl6G6XWdNyk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c_2_690x62.png" alt="image" data-base62-sha1="bMJwuO7QKs4EnTOSYl6G6XWdNyk" width="690" height="62" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c_2_690x62.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c_2_1035x93.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/2/529a3326ad0a3a4a60a7c95b080336814e487f6c.png 2x" data-dominant-color="1F262C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1368×124 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594621)

Hello Sir <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
What are implications on missing the project 1.<br>
Due to some personal reasons I wasn’t able to start any work on my project 1. It seems difficult for me to complete it.<br>
Could you please tell what will be the implications of missing it. Will I in anyway be able to cover up and pass in the subject doing future assignments and projects?
Thank you
PS: This isn’t any request to extend dates. I accept my fault and respect the dates provided by the team.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594626)

Sir I haven’t initaiated the podman earlier.<br>
Now when i try to use podman using the wsl via the code “sudo apt install -y podman” it is asking for the password…<br>
The problem is:
<ol>
<li>I haven’t set any password for podman earlier.</li>
<li>Though it is asking for password but it is not taking any input.(ie I am unable type anything there).<br>
what should I am supposed to do…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20.png" data-download-href="/uploads/short-url/uanLPgzih2sckRlTm7brBjpnJxS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20_2_690x153.png" alt="image" data-base62-sha1="uanLPgzih2sckRlTm7brBjpnJxS" width="690" height="153" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20_2_690x153.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20_2_1035x229.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/3/d36db27ac5478d6c2d5fee2e15c56e2068836c20_2_1380x306.png 2x" data-dominant-color="1C1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1612×359 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594642)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a> I think the evaluation.py test case is broken for A8 because I can manually see more folders and markdown files than the expected case output of A8 evaluation. And also is there any evaluation file for Part B

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594654)

password are not visible in wsl when typed, just type and enter if it matches, the process will continue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594657)

Sir If possible please extend the Project deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594660)

same error the execution is correct but format.md file is not modified with correct markdown format

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594677)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
can u please upload the video that was recorded on 12th Feb, as I am able to view only the video that was last recorded on 11th Feb (3 hrs 57 mins video). As I am doing the project completely from the recorded videos, please post those videos in youtube at the earliest.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594685)

Hi <a class="mention" href="/u/23f2003413">@23f2003413</a><br>
Because of some technical issues we could not record 12 Feb session. That was doubt clearing session regrading project1.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594689)

Can we submit project number of times before deadline…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594692)

thanks for you feedbacak I have figured it out! Thanks it means a lot…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594696)

A silly Doubt though but still a doubt!<br>
Could we create an image first of our project in initial stage(ie the my “app.py” is not completely ready) but I have build an docker image including the app.py and other dependencies.<br>
Should I give the same url now and then carry on updating the app.py<br>
Or, Should first complete and then upload in the form!
plz reply!!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594701)

Can you send the link for the video on 11th Feb?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594785)

How did you resolve the file cannot be found error?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594794)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c040c4323f2d2dfbeb3c76334f44adc7a59343f.png" data-download-href="/uploads/short-url/d80BbSQTNrgbeBjhu9MCwM8WE7Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c040c4323f2d2dfbeb3c76334f44adc7a59343f.png" alt="image" data-base62-sha1="d80BbSQTNrgbeBjhu9MCwM8WE7Z" width="690" height="435" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">872×550 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
pls help with this error

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594823)

Sir, could you please mention the title of youtube videos in which the project session are covered?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594831)

Hi,
When yesterday’s recorded video will be uploaded in youtube?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594837)

Thanks for the prompt reply <a class="mention" href="/u/jivraj">@Jivraj</a> . I have done the project setup till whatever was covered on the 11th Feb session. I am not able to proceed further as I have no clue on how to work on this. Can you please help me out as it would mean a lot.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594842)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/23f1002382">@23f1002382</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594844)

<div class="youtube-onebox lazy-video-container" data-video-id="jXj6bqy4R4c" data-video-title="2025-02-11 Week 5 - Session 1 - TDS Jan 25" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jXj6bqy4R4c" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b990ffaadbfcbad12d865c514f3d6b48e5bc7cf2.jpeg" title="2025-02-11 Week 5 - Session 1 - TDS Jan 25" data-dominant-color="595C5F" width="690" height="388">
  </a>
</div>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594845)

Are you subscribed to the TDS channel? If you were it would notify you immediately when it was uploaded. (10am this morning).
Please subscribe to the channel. It was also on the main page for TDS.<br>
<a href="https://tds.s-anand.net/#/README" class="onebox" target="_blank" rel="noopener nofollow ugc">https://tds.s-anand.net/#/README</a><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.youtube.com/@se-lr5ff">
  <header class="source">
      <img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/5/85553e6b4edcc2dda60afe0f9f82c7f3dbf31e04.png" class="site-icon" data-dominant-color="FF103A" width="16" height="16">

      <a href="https://www.youtube.com/@se-lr5ff" target="_blank" rel="noopener nofollow ugc">YouTube</a>
  </header>

  <article class="onebox-body">
    <img width="500" height="500" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05fae46322d62fdfa90a7c47a2011056f549cd9b_2_500x500.jpeg" class="thumbnail onebox-avatar" data-dominant-color="655F59">

<h3><a href="https://www.youtube.com/@se-lr5ff" target="_blank" rel="noopener nofollow ugc">Tools in Data Science</a></h3>

  Share your videos with friends, family, and the world


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594846)

Thanks sir, Now I subscribed to the channel.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594849)

Hi <a class="mention" href="/u/carlton">@carlton</a> sir! Is this video (Week-5 Session-3) the continuation video from the previous session (Week-5 Session-1), since the Session-2 video has not been recorded and uploaded. I am totally relying on these videos to complete the project sir. Please help me out!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594852)

offical answer is you dont, you let run it in docker and it would apparently work , im not there yet, bus as of of now , create your docker image and start testing there

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594859)

The deadline is at 11:59 pm right Saturday? Feb 15th? Google Standard Time?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594862)

Yes feb 15 11:59 PM indian standard time.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594863)

Hi <a class="mention" href="/u/23f2003413">@23f2003413</a>
Session 3 was continuation of session1.<br>
Session 2 was DCS(doubts clearing session)
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594865)

Got it. Thank you sir!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594868)

Hi <a class="mention" href="/u/jivraj">@Jivraj</a>, <a class="mention" href="/u/carlton">@carlton</a>, <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> sir,
I’m getting the following error while post mapping, I couldn’t able to fix it.<br>
I’m getting status code as 400 from the llm api response. How to fix it sir?
<pre><code class="lang-auto">   "json": {
        "message": "Invalid JSON body: SyntaxError: Unexpected token 'm', \"model=gpt-\"... is not valid JSON"
    }
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594870)

There is some problem with the json that you are using.
Try to debug it with GPT.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594873)

week5 session 1 and session3

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594874)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bf2517eb87feb20f7270ef8730daf3f1c5599473.png" data-download-href="/uploads/short-url/rgWFukcvzbPAVGQTtNCeVY8TbMv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bf2517eb87feb20f7270ef8730daf3f1c5599473.png" alt="image" data-base62-sha1="rgWFukcvzbPAVGQTtNCeVY8TbMv" width="690" height="317" data-dominant-color="4A4B4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">929×427 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is someone else are also getting this kind of error messages…<br>
I have a low end system, then shifted to high one then again this popped up…<br>
Does anyone know how to come over this…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594875)

Hello <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> sir, I have implemented the code for B3 &amp; B6 but unfortunately as per the instructions given in project for B3 &amp; B6 —
<ul>
<li>
<strong>B6</strong>. Extract data from (i.e. scrape) a website
</li>
<li>
<strong>B3</strong>. Fetch data from an API and save it
</li>
</ul>
They are almost similar and it’s getting confusing in both cases, it’s given output based on B3 and not reading the input for B6, so could you please help me out with this?
Is anyone else facing this or a similar issue?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594887)

Two solutions
<ol>
<li>give proper permissions.</li>
<li>use docker containers this is what we will test on.</li>
</ol>
I would prefer 2nd approach

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594890)

For B tasks use LLM to write code on the fly and execute it, use better prompts. In evaluation script detailed task will be provided with what data needs to be scraped, endpoints, parameters, etc.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594892)

{‘error’: {‘message’: “Invalid ‘tools[6].function.description’: string too long. Expected a string with maximum length 1024, but got a string with length 4384 instead.”, ‘type’: ‘invalid_request_error’, ‘param’: ‘tools[6].function.description’, ‘code’: ‘string_above_max_length’}, ‘monthlyCost’: 0.08569882000000002, ‘cost’: 0, ‘monthlyRequests’: 82}
i cant send long prompts then what is the point?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594895)

local llm also we cant use you because you have some limit on file size, we send long prompt also it doesn’t work xD . What do we do?<br>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  <span class="mention">@anybodywhowouldatleastreplyONCE</span>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594896)

Hi,<br>
If you read these questions carefully then they are not similar, one is asking you to extract data from a webpage, meaning you have to do something related to the HTML code. And the other is simply sending a request to a given endpoint.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594899)

Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/jivraj">@Jivraj</a> ,<br>
In task A6<br>
<strong>Find all Markdown (<code>.md</code> ) files in <code>/data/docs/</code> . For each file, extract the first occurrance of each H1 (i.e. a line starting with <code># </code> ). Create an index file <code>/data/docs/index.json</code> that maps each filename (without the <code>/data/docs/</code> prefix) to its title (e.g. <code>{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}</code> ).</strong>
Here expected output JSON “key” is file name or file path without prefix /data/docs/ as prompt is bit confusing . when “path/to/large-language-models.md” is given in example is actually referring to file path or filename itself is “path/to/large-language-models.md”.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594912)

This can easily be checked by runing the evaluate.py file.<br>
Anyways, a file present in data/docs/folder_a/folder_b/md_file should be folder_a/folder_b/md_file as key.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594917)

hey <a class="mention" href="/u/23f2001975">@23f2001975</a> did you find the solution to this problem ?<br>
i am facing the exact same issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594919)

<a class="mention" href="/u/carlton">@carlton</a><br>
Sir, my token limit has crossed the $1 limit. Will I receive new limit or a fresh token ? I still need to complete my project.<br>
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594944)

<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> /data/credit-card.txt<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
30091429521159<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
3009142952159
{‘role’: ‘assistant’, ‘content’: ‘3009142952159’, ‘refusal’: None} if LLM is giving wrong output. I hope y’all look into edge cases. Some people tried really hard. to prompt it xD <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=12" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">.<br>
<br>You can check the logs
<br>
(venv) @ANDIECOOLER2 ➜ /workspaces/TDS-Project-1/app (checking-with-open-ai) $ uv run evaluate.py 
🟡 Running task: Install `uv` (if required) and run the script `https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py`
with `23f1002382@ds.study.iitm.ac.in` as the only argument
HTTP Request: POST <a href="http://localhost:8000/run?task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fraw.githubusercontent.com%2FANdIeCOOl%2FTDS-Project1-Ollama_FastAPI-%2Frefs%2Fheads%2Fmain%2Fdatagen.py%60%0Awith+%6023f1002382%40ds.study.iitm.ac.in%60+as+the+only+argument%0A" rel="noopener nofollow ugc">http://localhost:8000/run?task=
Install+`uv`+(if+required)+and+run+the+script+`https%3A%2F%2Fraw.githubusercontent.com%2FANdIeCOOl%2FTDS-Project1-Ollama_FastAPI-%2Frefs%2Fheads%2Fmain%2Fdatagen.py`
with+`23f1002382%40ds.study.iitm.ac.in`+as+the+only+argument
</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/format.md" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/format.md</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A1 PASSED
10.8.2<br>
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Format the contents of <code>/data/format.md</code> using <code>prettier@3.4.2</code>, updating the file in-place
HTTP Request: POST <a href="http://localhost:8000/run?task=%0AFormat+the+contents+of+%60%2Fdata%2Fformat.md%60+using+%60prettier%403.4.2%60%2C+updating+the+file+in-place%0A" rel="noopener nofollow ugc">http://localhost:8000/run?task=
Format+the+contents+of+`%2Fdata%2Fformat.md`+using+`prettier%403.4.2`%2C+updating+the+file+in-place
</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/format.md" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/format.md</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A2 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: The file <code>/data/dates.txt</code> contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to <code>/data/dates-wednesdays.txt</code>
HTTP Request: POST <a href="http://localhost:8000/run?task=The+file+%60%2Fdata%2Fdates.txt%60+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+%60%2Fdata%2Fdates-wednesdays.txt%60" rel="noopener nofollow ugc">http://localhost:8000/run?task=The+file+`%2Fdata%2Fdates.txt`+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+`%2Fdata%2Fdates-wednesdays.txt`</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/dates-wednesdays.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/dates-wednesdays.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A3 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Sort the array of contacts in <code>/data/contacts.json</code> by <code>last_name</code>, then <code>first_name</code>, and write the result to <code>/data/contacts-sorted.json</code>
HTTP Request: POST <a href="http://localhost:8000/run?task=Sort+the+array+of+contacts+in+%60%2Fdata%2Fcontacts.json%60+by+%60last_name%60%2C+then+%60first_name%60%2C+and+write+the+result+to+%60%2Fdata%2Fcontacts-sorted.json%60" rel="noopener nofollow ugc">http://localhost:8000/run?task=Sort+the+array+of+contacts+in+`%2Fdata%2Fcontacts.json`+by+`last_name`%2C+then+`first_name`%2C+and+write+the+result+to+`%2Fdata%2Fcontacts-sorted.json`</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/contacts-sorted.json" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/contacts-sorted.json</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A4 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Write the first line of the 10 most recent <code>.log</code> file in <code>/data/logs/</code> to <code>/data/logs-recent.txt</code>, most recent first
HTTP Request: POST <a href="http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+%60.log%60+file+in+%60%2Fdata%2Flogs%2F%60+to+%60%2Fdata%2Flogs-recent.txt%60%2C+most+recent+first" rel="noopener nofollow ugc">http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+`.log`+file+in+`%2Fdata%2Flogs%2F`+to+`%2Fdata%2Flogs-recent.txt`%2C+most+recent+first</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/logs-recent.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/logs-recent.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A5 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Find all Markdown (<code>.md</code>) files in <code>/data/docs/</code>.<br>
For each file, extract the first occurrance of each H1 (i.e. a line starting with <code># </code>).<br>
Create an index file <code>/data/docs/index.json</code> that maps each filename (without the <code>/data/docs/</code> prefix) to its title<br>
(e.g. <code>{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}</code>)
HTTP Request: POST <a href="http://localhost:8000/run?task=Find+all+Markdown+%28%60.md%60%29+files+in+%60%2Fdata%2Fdocs%2F%60.%0AFor+each+file%2C+extract+the+first+occurrance+of+each+H1+%28i.e.+a+line+starting+with+%60%23+%60%29.%0ACreate+an+index+file+%60%2Fdata%2Fdocs%2Findex.json%60+that+maps+each+filename+%28without+the+%60%2Fdata%2Fdocs%2F%60+prefix%29+to+its+title%0A%28e.g.+%60%7B%22README.md%22%3A+%22Home%22%2C+%22path%2Fto%2Flarge-language-models.md%22%3A+%22Large+Language+Models%22%2C+...%7D%60%29" rel="noopener nofollow ugc">http://localhost:8000/run?task=Find+all+Markdown+(`.md`)+files+in+`%2Fdata%2Fdocs%2F`.
For+each+file%2C+extract+the+first+occurrance+of+each+H1+(i.e.+a+line+starting+with+`%23+`).
Create+an+index+file+`%2Fdata%2Fdocs%2Findex.json`+that+maps+each+filename+(without+the+`%2Fdata%2Fdocs%2F`+prefix)+to+its+title
(e.g.+`{“README.md”%3A+“Home”%2C+“path%2Fto%2Flarge-language-models.md”%3A+“Large+Language+Models”%2C+...}`)</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/docs/index.json" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/docs/index.json</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A6 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: <code>/data/email.txt</code> contains an email message. Pass the content to an LLM with instructions to extract the sender’s email address, and write just the email address to <code>/data/email-sender.txt</code>
HTTP Request: POST <a href="http://localhost:8000/run?task=%60%2Fdata%2Femail.txt%60+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender%27s+email+address%2C+and+write+just+the+email+address+to+%60%2Fdata%2Femail-sender.txt%60" rel="noopener nofollow ugc">http://localhost:8000/run?task=`%2Fdata%2Femail.txt`+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender’s+email+address%2C+and+write+just+the+email+address+to+`%2Fdata%2Femail-sender.txt`</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/email-sender.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/email-sender.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A7 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: <code>/data/credit_card.png</code> contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to <code>/data/credit-card.txt</code>
HTTP Request: POST <a href="http://localhost:8000/run?task=%60%2Fdata%2Fcredit_card.png%60+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcredit-card.txt%60" rel="noopener nofollow ugc">http://localhost:8000/run?task=`%2Fdata%2Fcredit_card.png`+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+`%2Fdata%2Fcredit-card.txt`</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/credit-card.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/credit-card.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> /data/credit-card.txt<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
30091429521159<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
3009142952159
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A8 FAILED
HTTP Request: POST <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: <code>/data/comments.txt</code> contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to <code>/data/comments-similar.txt</code>, one per line
HTTP Request: POST <a href="http://localhost:8000/run?task=%60%2Fdata%2Fcomments.txt%60+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+%60%2Fdata%2Fcomments-similar.txt%60%2C+one+per+line" rel="noopener nofollow ugc">http://localhost:8000/run?task=`%2Fdata%2Fcomments.txt`+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+`%2Fdata%2Fcomments-similar.txt`%2C+one+per+line</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/comments-similar.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/comments-similar.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A9 PASSED
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: The SQLite database file <code>/data/ticket-sales.db</code> has a <code>tickets</code> with columns <code>type</code>, <code>units</code>, and <code>price</code>. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the “Gold” ticket type? Write the number in <code>/data/ticket-sales-gold.txt</code>
HTTP Request: POST <a href="http://localhost:8000/run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60" rel="noopener nofollow ugc">http://localhost:8000/run?task=The+SQLite+database+file+`%2Fdata%2Fticket-sales.db`+has+a+`tickets`+with+columns+`type`%2C+`units`%2C+and+`price`.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+“Gold”+ticket+type%3F+Write+the+number+in+`%2Fdata%2Fticket-sales-gold.txt`</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/green_circle.png?v=12" title=":green_circle:" class="emoji" alt=":green_circle:" loading="lazy" width="20" height="20"> HTTP 200 {<br>
“status”: “success”,<br>
“message”: “Task executed successfully”<br>
}
HTTP Request: GET <a href="http://localhost:8000/read?path=/data/ticket-sales-gold.txt" rel="noopener nofollow ugc">http://localhost:8000/read?path=/data/ticket-sales-gold.txt</a> “HTTP/1.1 200 OK”
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> A10 PASSED
<img src="https://emoji.discourse-cdn.com/google/dart.png?v=12" title=":dart:" class="emoji" alt=":dart:" loading="lazy" width="20" height="20"> Score: 9 / 10 proof<br>
EDIT CREDIT CARD NUMBERS are 16 digits, so even there is discrepancy

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594945)

usage’: {‘prompt_tokens’: 1384,<br>
‘completion_tokens’: 67,<br>
‘total_tokens’: 1451,<br>
‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0},<br>
‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}},<br>
‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_13eed4fce1’,<br>
‘monthlyCost’: 0.5243745800000005,<br>
‘cost’: 0.004554000000000001
GPT-4o mini<br>
Fine-tuning price<br>
Input:--------------------------&gt; CALCUATION: (1384/10^6)*$0.30 = 0.0004152<br>
$0.30 / 1M tokens<br>
Cached input:<br>
$0.15 / 1M tokens<br>
Output:-------------------------&gt;  CALCUATION: (67/10^6)$1.20 = 0.0000804<br>
$1.20 / 1M tokens<br>
Training:<br>
$3.00 / 1M tokens<br>
TOTAL = 0.0004152 + 0.0000804 = 0.0004956<br>
‘cost’: 0.004554000000000001 MAKE IT MAKE SENSE?<br>
‘total_tokens’: 1451, so only input and completion tokens used?<br>
<br><br>
<br><br>
<br><br>
<br><br>
INFO:     Uvicorn running on <a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a> (Press CTRL+C to quit)<br>
INFO:root:10<br>
INFO:root:Inside run_task with task:<br>
Install <code>uv</code> (if required) and run the script <code>https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py</code><br>
with <code>23f1002382@ds.study.iitm.ac.in</code> as the only argument
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::<br>
{‘id’: ‘chatcmpl-B0pChhrBiCN8x8ueL2u57rwQiucl7’, ‘object’: ‘chat.completion’, ‘created’: 1739536527, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: None, ‘tool_calls’: [{‘id’: ‘call_ULCgfFzpEcnGNditwVwGwRIS’, ‘type’: ‘function’, ‘function’: {‘name’: ‘install_and_run_script’, ‘arguments’: ‘{“package”:“uv”,“args”:[“23f1002382@ds.study.iitm.ac.in”],“script_url”:“<a href="https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py" rel="noopener nofollow ugc">https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py</a>”}’}}], ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘tool_calls’}], ‘usage’: {‘prompt_tokens’: 1384, ‘completion_tokens’: 67, ‘total_tokens’: 1451, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_13eed4fce1’, ‘monthlyCost’: 0.5243745800000005, ‘cost’: 0.004554000000000001, ‘monthlyRequests’: 217}
<a class="mention" href="/u/s.anand">@s.anand</a>  How is the usage calculated? Just asking not implying<br>
UPDATE:  ITS EVEN MORE CHEAPER, I gave benefir of doubt better its much cheaper? ???<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40.png" data-download-href="/uploads/short-url/hpybf5VWgkRP2wPZWvJVRMWMGIg.png?dl=1" title="Screenshot 2025-02-14 183844" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40_2_690x357.png" alt="Screenshot 2025-02-14 183844" data-base62-sha1="hpybf5VWgkRP2wPZWvJVRMWMGIg" width="690" height="357" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40_2_690x357.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40_2_1035x535.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a085e66044ea9d25d6ad8e95640d6b635c9cd40_2_1380x714.png 2x" data-dominant-color="080707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-14 183844</span><span class="informations">1695×879 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594946)

You can continue to $2. Then you would need to ask for a new token.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594952)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> please upload recording of TDS Week 5 - Session 2. Only recordings of session 1 &amp; 3 have been uploaded.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594953)

<aside class="onebox githubrepo" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project-1">
  <header class="source">

      <a href="https://github.com/ANdIeCOOl/TDS-Project-1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/b/3bfc6f97a124e61d5c97c25e6dd6c901e0262fde_2_690x344.png" class="thumbnail" data-dominant-color="EFF2F3">

  <h3><a href="https://github.com/ANdIeCOOl/TDS-Project-1" target="_blank" rel="noopener nofollow ugc">GitHub - ANdIeCOOl/TDS-Project-1</a></h3>

    <span class="github-repo-description">Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

DONE WITH A TASK , you have to create DOCKER IMAGE THOUGH &lt; HAVE ENV file with keys , check the key value pair names, an cheers guy , we all get 9 marks hopefully

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594958)

For as task description like this
<ul>
<li>Write the # of Thursdays in <code>/data/extracts.txt</code> into <code>/data/extracts-count.txt</code></li>
</ul>
I have given the prompt in such detail to the LLM but it is still not able to understand the task because of the “#” symbol. The task is getting truncated even before it reaches to the LLM.<br>
Can anyone help me on this because I have tried so many things to fix this but nothing seems to help.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594960)

Hi <a class="mention" href="/u/jivraj">@Jivraj</a>, <a class="mention" href="/u/carlton">@carlton</a> sir,
I have created a docker file and run the application but it’s throwing error for<br>
A2 task<br>
No such file or directory: ‘npx’<br>
Do i need give the node install in docker file?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594963)

Hash is just another way of writing “number”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594964)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
sir i have tried to solve the A1. when I want to check the solution we are asked for the datagen module as the evaluate.py have<br>
’
<pre><code class="lang-auto">''from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
'''
</code></pre>
so do we need to download the datagen.py in the local system first…
Or it should be the part of the automation only…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594967)

I am getting internal server error for task A1, I have been trying for a long time. It may be possible that i have issues with my ai_proxy token thus tell how to properly set the taken.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594968)

Yes I know that but LLM does not know that # indicates number. And no prompt is fixing this issue because the task has to be passed as query parameter and by the time LLM reads the task, it is already half gone due to #.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594973)

Where to find AIProxy token from?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594978)

what if we are out of token sir how do we complete our project then?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594979)

could u share your code once i think you should explicitly try to install npx in your code

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594981)

<aside class="quote group-ds-students" data-username="23f1002382" data-post="279" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png" class="avatar"> 23f1002382:</div>
<blockquote>
ANDIECOOLER2
</blockquote>
</aside>
could you help me out with q2?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594982)

Can you tell me where to get the AIPROXY Token from and also are u able to execute docker image push command it keeps showing as an error to me

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594983)

<pre><code class="lang-auto">def format_with_prettier(file_path:str, prettier_version:str):
    if file_path and os.path.exists(file_path):
        print('Path exisit - will perform prettier')
        subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])
    else:
        raise FileNotFoundError()
</code></pre>
This is my code

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594984)

this isnt also working are you sure its right?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594986)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/dbd85efd1bbce9710794cb0434a90d37a8c20a25.png" data-download-href="/uploads/short-url/vmQ8BNdYH7yAYCyh6zn06I9QfB3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/dbd85efd1bbce9710794cb0434a90d37a8c20a25.png" alt="image" data-base62-sha1="vmQ8BNdYH7yAYCyh6zn06I9QfB3" width="559" height="500" data-dominant-color="1D1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1027×917 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594987)

okay but in my docker image when i tried to run that in local, its asking for npx and it doesnt work

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594989)

<a class="mention" href="/u/carlton">@carlton</a> could you please give a hint as to why this isnt working

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594990)

im running locally first and then will use docker when i get a 10/10 score

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594991)

Okay, actually when i tried with local, i’m facing path error
<pre><code class="lang-auto">./data/format.md
[WinError 2] The system cannot find the file specified
</code></pre>
So that’s why i moved to docker but there also i’m getting error for A2.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594992)

you should manually check if the file really exists or not because i think the code and the folder where datagen.py is downloading files(data folder) are different

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594993)

yes yes i moved the folder to current working directory

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/594997)

If you are using the function calling approach, you could just parse the ‘#’ and change it to ‘number’ and then send the prompt to the llm for that particular task.
Or another approach is tell the llm,
If you ever see the phrase ‘count the # of’ in a task, please interpret it as ‘count the number of’. For example<br>
Count the # of Fridays means<br>
Count the number of Fridays

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595006)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55.png" data-download-href="/uploads/short-url/8NBFgsDIDQ14khxWKQTblBAyfUV.png?dl=1" title="Screenshot 2025-02-14 201854" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55_2_690x364.png" alt="Screenshot 2025-02-14 201854" data-base62-sha1="8NBFgsDIDQ14khxWKQTblBAyfUV" width="690" height="364" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55_2_690x364.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55_2_1035x546.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dacf2bf3fd48309342a483aeb249f46faf1dc55_2_1380x728.png 2x" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-14 201854</span><span class="informations">1919×1015 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> this is showing while docker image is running

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595010)

in project page, ctrl+F and search ai proxy, one link s.anandProxy or something, there it will validate you email and get you your token.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595016)

can you share your code for dynamic code generation, i dont have the base to start with , can you send me the code?<br>
whatever this image is , llm_code,oy and etc

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595019)

What file should we have while pushing it to git and making image<br>
should datagen file and data be there or not?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595024)

Please read the deliverables and evalute section.
datagen.py and evaluate.py were for only for your testing purposes so that you have an idea of the workflow and how the evaluation works. They are NOT part of your project submission.
Only DO what the project page tells you in the deliverables and evalute sections.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595026)

sir i am getting this error by running the docker image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d16a8ef3054bbd7db0999d3efcf5aaadae798d5.png" data-download-href="/uploads/short-url/hQAeppzCT6UMjxo679DbUO4hU8d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d16a8ef3054bbd7db0999d3efcf5aaadae798d5.png" alt="image" data-base62-sha1="hQAeppzCT6UMjxo679DbUO4hU8d" width="656" height="116"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">656×116 3.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
i tried troubleshooting this for hours but no luck could you please tell me what i did wrong here

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595050)

i can help you up, if you need my help you can email me

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595051)

<a class="mention" href="/u/s.anand">@s.anand</a> Sir please tell me this I am not using podman i am using docker for building and hosting is it fine sir ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595068)

Hey <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> , I actually submitted the project already in the morning,<br>
I included all the deliverables and things mentioned in the evaluation section.
But since I was actively testing with the - <code>datagen.py</code> and <code>evaluate.py</code>, I forgot to remove them before submission.
However these files do not play a role in my project execution in any way, they just sit idle. Will there be any issue?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595073)

when trying to use function call way of open api
<pre><code class="lang-auto">tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_email_sender",
            "description": "Extract sender email from a specific file in directory",
            "parameters": {},
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_day_of_week",
            "description": "To count the occurances of a specific day of a week in a file with various dates",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "day of week"
                    }
                },
                "required": ["day_of_week"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]
</code></pre>
<pre><code class="lang-auto">    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_input},
                
        ],      
	"tools": tools,
    "tool_choice": "auto",
    "max_tokens": 500,
    "temperature": 0.7
    }
</code></pre>
facing the below issue<br>
ror’: {‘message’: “Invalid type for ‘tools[0]’: expected an object, but got an array instead.”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595074)

when i run POST request t is showing output “HTTP/1.1 200 OK” but when i give GET request it is showing HTTP/1.1" 404 Not Found. Can you please say how can it be solved

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595078)

These files are inside a separate folder - <code>evaluation</code> in my project root directory. Since I already submitted please do consider.
Thanks &amp; Regards<br>
Pradeep

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595082)

This indicates your task execution returns  “HTTP/1.1 200 OK” but the execution doesn’t creates the required file in the given location that the evaluation script is requesting.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595086)

If have doubts in building DOCKER stuff can you help me debug
PLEASE SENPAI
<img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/fish_cake.png?v=12" title=":fish_cake:" class="emoji" alt=":fish_cake:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/dolls.png?v=12" title=":dolls:" class="emoji" alt=":dolls:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595087)

sure!! how can I help?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595088)

+1<br>
SENPAI is right <img src="https://emoji.discourse-cdn.com/google/innocent.png?v=12" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595089)

not yet maybe in an hour, im building, but after that running in docker is different ball game, thats why , i need quick debugs in a meeting, other people also can join, maybe tomorrow, i have an exam tomorrow, so preferably , collectively before project submission . IF YOU HAVE TIME

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595090)

<aside class="quote group-ds-students quote-modified" data-username="23f1002382" data-post="321" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png" class="avatar"> 23f1002382:</div>
<blockquote></blockquote>
</aside>
Sure tell me I would try, if I am online then otherwise tomorrow if it’s late

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595091)

I am getting this error while pulling docker image
ansh@Lenovo:~/llm_project$ podman pull <a href="http://docker.io/ansh205/llm_project:final" rel="noopener nofollow ugc">docker.io/ansh205/llm_project:final</a><br>
Trying to pull <a href="http://docker.io/ansh205/llm_project:final" rel="noopener nofollow ugc">docker.io/ansh205/llm_project:final</a>…<br>
Error: parsing image configuration: Get “<a href="https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/07/079f65bc553514a8f38a08fd959e932ca984894a64eed71fca406f3353b71d3b/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250214%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250214T172706Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=073575bf08338fcdda378b997ebe749b15a6b676ed7b80fbf4c3f8080a791152" rel="noopener nofollow ugc">https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/07/079f65bc553514a8f38a08fd959e932ca984894a64eed71fca406f3353b71d3b/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250214%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250214T172706Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=073575bf08338fcdda378b997ebe749b15a6b676ed7b80fbf4c3f8080a791152</a>”: dial tcp: lookup <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com</a> on 10.255.255.254:53: server misbehavingPreformatted text

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595097)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
sir please provide me other api key. My current request cost is full.
Full LLM Response: {‘message’: ‘On 2025-02 you used $2.000143640000001, exceeding $2’}

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595108)

<pre><code class="lang-auto"> curl -X POST http://localhost:8001/run?task=Extract%20sender%20email
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    36  100    36    0     0      9      0  0:00:04  0:00:03  0:00:01     9{"results":"wrighttara@example.net"}
</code></pre>
is this expectation of having %20 for blanks in query string fine ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595109)

docker run -e OPEN_AI_PROXY_TOKEN=your_token_value <br>
-e OPEN_AI_PROXY_URL=your_proxy_url <br>
-e OPEN_AI_EMBEDDING_URL=your_embedding_url <br>
-p 8000:8000
how do we get out urls inside, hardcode?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595111)

Can you help with docker size image?<br>
is it 2 GB?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595126)

I want to reset my aiproxys i have used them all if i could even buy some would work i need it to test my app or could iitm help in resetting it please tell

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595131)

could u help me in q9 thats the one left

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595132)

<a class="mention" href="/u/carlton">@carlton</a> my aiproxy is also exhausted please help me out

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595133)

sir my api tokens limit reached to one dollar , hiw to reset it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595134)

bro can you help me with q2

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595135)

How to handle task a8 ? I tried pytesseract but gave wrong results.EasyOCR is giving the exact answer so tried in docker but some Model download is interrupting the flow of evaluate.py resulting in error .<br>
I appreciate any help/procedure or code to handle taska8.<br>
Thanks in advance.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595139)

Did you get any solution to this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595140)

u can use groq api groq api is compatible with openai

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595142)

whats up?<br>
/////////////////////

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595143)

bro can please check my repo i am only able to do 7 tasks.
repo url: <a href="https://github.com/23f2005593/tds-project-1" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 23f2005593/tds-project-1: TDS Project 1</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595145)

got the docker working?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595148)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jeeveash.k">@Jeeveash.k</a><br>
sir i submitted the wrong docker image file while submitted the form. Can you please let me change it, or make it such that we can reupload it<br>
thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595149)

22f3001011 I’ve enabled “Allow response editing” on the form. I <em>think</em> that means you can edit your response… but since you had submitted it before it was enabled, I’m not sure what the procedure is. Worst case, please submit again.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595151)

<strong>Please make this change in evaluation.py</strong>
In evaluation script url of datagen.py is different than actual one please change it
evaluation.py line 72
Install <code>uv</code> (if required) and run the script <code>https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py</code>
<strong>change this to</strong>
Install <code>uv</code> (if required) and run the script <code>https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py</code>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595152)

very true there is too much confusion Id like to ask if you know that evaluate.py is mean to run only for <a href="mailto:user@example.com">user@example.com</a> or our own mail too  because there was written <strong>You MUST use your Student Id</strong> (eg. 22f3xxxxxx@ds.study.iitm.ac.in) <strong>to do the Project, otherwise your score will not be considered for evaluation.</strong>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595153)

Hi any one have any idea on the below,
<pre><code class="lang-auto">SyntaxError: illegal target for annotation
</code></pre>
I’m getting this error only when i run the evaluate.py but in with postman it works as expected.
Anyone please help on this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595154)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8.png" data-download-href="/uploads/short-url/oQJF4dWyOs4fDfQrPxf5Xm8i3q0.png?dl=1" title="Screenshot 2025-02-15 071910" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8_2_690x367.png" alt="Screenshot 2025-02-15 071910" data-base62-sha1="oQJF4dWyOs4fDfQrPxf5Xm8i3q0" width="690" height="367" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8_2_690x367.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8_2_1035x550.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae2a4772672aef536d8e69b87e59e4f94853ebc8_2_1380x734.png 2x" data-dominant-color="1F1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-15 071910</span><span class="informations">1919×1021 71.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
sir why the datagen.py in not created in the tree and the data folder please help me <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595160)

created in toot, cd /data in docker will take you there.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595163)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213.png" data-download-href="/uploads/short-url/u4LCPuNaRYEWsimvnsykic5CAmf.png?dl=1" title="Screenshot 2025-02-15 075843" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213_2_690x365.png" alt="Screenshot 2025-02-15 075843" data-base62-sha1="u4LCPuNaRYEWsimvnsykic5CAmf" width="690" height="365" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213_2_690x365.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213_2_1035x547.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/2/d2cb339eab8983304f220c258a57f4db8cd76213_2_1380x730.png 2x" data-dominant-color="202020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-15 075843</span><span class="informations">1919×1017 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
is changes is required in Dockerfile

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595170)

i too got the same error you can change the the tools part in your payload to
<pre><code class="lang-auto">"tools": [{"type": "function", "function": schema} for schema in function_schema]
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595180)

i think you have to run the following command
<pre data-code-wrap="python"><code class="lang-python">uv run datagen.py &lt;your_email&gt; --root ./data
</code></pre>
try to include --root ./data in your code

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595182)

sorry i forgot the change the name of function_schema to tools please you do that

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595185)

<a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Hello,<br>
just a silly question, if my code runs well in docker environment with <code>/data</code> in root directory, will it be fine ?<br>
or should i keep the relative <code>./data</code> directory like in the lecture ?<br>
Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595187)

The reason in the lecture they were using ./data was because they were debugging in their local machine not in the docker.
For the docker image (the official submission) you must use /data.<br>
It is a clear requirement mentioned in the project page.
Thats why it works fine when you use it in the docker image.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595189)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69011e1ad4ea3c00a9294163be28e49ebc671faa.png" data-download-href="/uploads/short-url/eYUwMQMGVSkTHB8Q1rchZjfsJmO.png?dl=1" title="Screenshot 2025-02-15 101818" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69011e1ad4ea3c00a9294163be28e49ebc671faa.png" alt="Screenshot 2025-02-15 101818" data-base62-sha1="eYUwMQMGVSkTHB8Q1rchZjfsJmO" width="690" height="418" data-dominant-color="F6F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-15 101818</span><span class="informations">858×521 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a><br>
hello sir i need help here. I have pushed my image into a docker repo and trying to submit it on ht google form. but it is not accepting it and asking to remove the tag .<br>
What do i do ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595204)

Alright sir.  Thank you very much for your help.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595208)

Are multiple submissions allowed for project?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595225)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83.jpeg" data-download-href="/uploads/short-url/eSjyAinyD3Rk4efDQena0iYIpRF.jpeg?dl=1" title="A8" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83_2_281x500.jpeg" alt="A8" data-base62-sha1="eSjyAinyD3Rk4efDQena0iYIpRF" width="281" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83_2_281x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83_2_421x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/8/68423b54f8da150ecf68a17a19215d51def3ae83_2_562x1000.jpeg 2x" data-dominant-color="446487"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">A8</span><span class="informations">720×1280 85.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
please check this one…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595228)

Hi <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a>  sir,
For A2 do i need to install node in the docker? I’m getting error with npx.<br>
please suggest some way sir?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595230)

if i have two repo on docker , is there any problem in that

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595231)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b63973070de46f577b8184dd1cdeae4449e60a64.png" data-download-href="/uploads/short-url/q01Z1oXJ91KyKi8L0O0z9n1dYAQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b63973070de46f577b8184dd1cdeae4449e60a64.png" alt="image" data-base62-sha1="q01Z1oXJ91KyKi8L0O0z9n1dYAQ" width="684" height="316"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">684×316 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
why do i get this error? can someone please help me out <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>…Anyone pls help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595251)

can u please share the base proxy url

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595252)

I’m also getting the same error. I have used a proxy URL and token. Before, it was working, but now it’s not.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595257)

sir or anyone can you please provide what should be the content inside the docker file … i am getting confuse like /data or python-slim etc<br>
… i am done with locally testing and only this thing left.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595262)

yes please explain somebody. What should be inside the dockerfile

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595263)

Hi ,
Anyone completed Task B, I don’t know how to combine task A (function calling) and task B (self creating python code)
can anyone suggest how to do that? It will be really helpful

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595266)

“<a href="http://aiproxy.sanand.workers.dev/openai/v1" rel="noopener nofollow ugc">http://aiproxy.sanand.workers.dev/openai/v1</a>” use this as proxy URL. its working for me now!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595268)

How to resolve this?<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ uv run app.py<br>
Traceback (most recent call last):<br>
File “/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro/app.py”, line 10, in <br>
from fastapi import FastAPI<br>
ModuleNotFoundError: No module named ‘fastapi’<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip show fastapi<br>
WARNING: Package(s) not found: fastapi<br>
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip install fastapi<br>
error: externally-managed-environment
× This environment is externally managed<br>
╰─&gt; To install Python packages system-wide, try apt install<br>
python3-xyz, where xyz is the package you are trying to<br>
install.
<pre><code>If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
sure you have python3-full installed.

If you wish to install a non-Debian packaged Python application,
it may be easiest to use pipx install xyz, which will manage a
virtual environment for you. Make sure you have pipx installed.

See /usr/share/doc/python3.12/README.venv for more information.
</code></pre>
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.<br>
hint: See PEP 668 for the detailed specification.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595273)

sir,<br>
It is a humble requests from my side, to plz extend the deadline.<br>
Because student like who come from non technical background, are unable to come up with this project…<br>
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.<br>
Moreover I am Dual Degree student. It is very hectic for me.<br>
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…<br>
Plz sir understand the situation and extend the deadline…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595280)

<aside class="quote group-ds-students" data-username="23f2003413" data-post="368" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003413/48/66883_2.png" class="avatar"> 23f2003413:</div>
<blockquote>
<a href="http://aiproxy.sanand.workers.dev/openai/v1" rel="noopener nofollow ugc">http://aiproxy.sanand.workers.dev/openai/v1</a>
</blockquote>
</aside>
For me it says invalid path

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595281)

<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/4/545dc513707cfdd63db2d8d88d8c355d88316c55.png" alt="Screenshot 2025-02-15 140726" data-base62-sha1="c2l0wtftVs48bzpr1MlcrBfEhOB" width="690" height="71" data-dominant-color="F6F6F6">
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595282)

same issue happening with me even though working for last whole week only got 4 correct . please extend some time so we can complete the project as weekends are the time when we get a day off from our primary college and can work with full attention on this project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595285)

it usually happens in some GNU/Linux OS. since you are using some distribution based on Debian namely Ubuntu or whatever try doing sudo apt install python-packagename (replace package name with fastapi for fastapi)<br>
then it works. It usually happens due to manual intervention with pip3 the user might break some system dependencies which require some python3 package. No need to worry about it.<br>
Another Fix: try using a virtual environment which is highly suggested since there is no chance for you to interfere with the system packages.<br>
create a venv using python3 -m venv name_of_venv<br>
add this line to your .bashrc in ~ folder as source /path/to/your/venv/location<br>
and run source .bashrc. This time no error occurs as you do everything in your virtual environment you can install anything python3 package using pip3 install package name.<br>
It even happened for me
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac.png" data-download-href="/uploads/short-url/37CTgqCCMcH8aqhG6ZxcO9HICyE.png?dl=1" title="Screenshot_20250215_143357" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_690x181.png" alt="Screenshot_20250215_143357" data-base62-sha1="37CTgqCCMcH8aqhG6ZxcO9HICyE" width="690" height="181" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_690x181.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_1035x271.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/15e33e0ab5319a089a3cf734a66b3318dc7d08ac_2_1380x362.png 2x" data-dominant-color="282B2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20250215_143357</span><span class="informations">3841×1009 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595295)

Most of your questions and doubts will be solved in todays sessions. First 20 mins will be a clear overview of the logic and workflow and how evaluation actually works.<br>
Rest of the session will be bug fixing and doubts.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595296)

<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.<br>
New customer green strategy.<br>
Feeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.<br>
During professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.<br>
Wind develop world next. Impact appear capital cold stock we. Quality get run case huge that.<br>
Use century general above more region. Radio him quality stage. Truth least military dinner growth.<br>
Study maybe source. For expect imagine.<br>
Analysis remain voice dog sit part. Safe them store spring life girl.<br>
House bring challenge. Tell but rock able great.<br>
Mouth president worker common Mr billion.
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.\nNew customer green strategy.\nFeeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.\nDuring professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.\nWind develop world next. Impact appear capital cold stock we. Quality get run case huge that.\nUse century general above more region. Radio him quality stage. Truth least military dinner growth.\nStudy maybe source. For expect imagine.\nAnalysis remain voice dog sit part. Safe them store spring life girl.\nHouse bring challenge. Tell but rock able great.\nMouth president worker common Mr billion.”<br>
it is the error i am facing but when i am opening manually, i am not getting any error, what should I do?<br>
this same issue is with 3-4 questions

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595298)

when will the session be conducted and how can we join it sir?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595316)

Hi Thanks.<br>
Yes. it works when venv is created. But I see that it was working find in Week 5-Session 1 video without creating virtual environment.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595317)

I will not submit project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595321)

Get authentication token from this <a href="https://aiproxy.sanand.workers.dev/" rel="noopener nofollow ugc">AI Proxy</a> and usage and follow documentation for sending requests.<br>
<a href="https://github.com/sanand0/aiproxy" rel="noopener nofollow ugc">sanand0/aiproxy: Authorizing proxy for LLMs</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595326)

No Problems, just fill form with correct image name in google forms.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595327)

yes npx will require node to be installed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595328)

<a class="mention" href="/u/jivraj">@Jivraj</a> when would today’s live session be conducted and how can we attend it sir

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595329)

evaluate.py is not working sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595333)

What if you run out of credits during or just before final evaluation?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595335)

This is only for testing on local machine.
In docker image keep /data.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595338)

One session is going live right now (from 3 to 5 pm).<br>
It will be visible from calendra.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595339)

sir,<br>
It is a humble requests from my side, to plz extend the deadline.<br>
Because student like who come from non technical background, are unable to come up with this project…<br>
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.<br>
Moreover I am Dual Degree student. It is very hectic for me.<br>
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…<br>
Plz sir understand the situation and extend the deadline…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595342)

Sir, I have put my AIPROXY_TOKEN in .env file should I need to push the .env file also in the github

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595343)

yes sir do we have to put env file also <a class="mention" href="/u/carlton">@carlton</a> sir <a class="mention" href="/u/jivraj">@Jivraj</a> sir

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595348)

In the evaluation.py there is an import require named from datagen import some stuff.<br>
which means inorder to run the evaluation.py we need to manually bring the datagen.py in the working directory…
Because in order to run the evaluation.py we need the datagen. plz help…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595357)

can someone send the meet link for the live session happening now

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595359)

Everytime I run datagen.py for the A1 task, the data file gets downloaded in the C drive instead of the current project folder. I even tried to set the current project folder as the root directory but it still downloads the files in C drive and I cant seem to find a workaround this. Can someone please help with this issue. Thanks!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595362)

Can you please make the changes in the datagen.py file
config = {“root”: “/data”}
This is where I have been facing the issue.
The only solution I can think of is moving the /data folder from the root to the project directory. which I am not sure is a good way to solve this issue.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595366)

<div class="youtube-onebox lazy-video-container" data-video-id="NkUmOagUORE" data-video-title="TDS Jan 2025 Live Stream" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=NkUmOagUORE" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef51e62fc93908c084aebcfe587121a226bb1397.jpeg" title="TDS Jan 2025 Live Stream" data-dominant-color="100801" width="690" height="388">
  </a>
</div>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595369)

<a class="mention" href="/u/carlton">@carlton</a>
please tell do we have to put this url in a variable for A1 task ?
<a href="https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py" class="onebox" target="_blank" rel="noopener nofollow ugc">https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595371)

Task A9 fails.
<blockquote>
HTTP Request: POST <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a> “HTTP/1.1 401 Unauthorized”<br>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A9 failed: ‘data’<br>
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A9 FAILED
</blockquote>
If I run
<pre><code class="lang-auto">curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'
</code></pre>
I get
<pre><code class="lang-auto">{
  "message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"
}
</code></pre>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595372)

<a class="mention" href="/u/carlton">@carlton</a> sir <a class="mention" href="/u/jivraj">@Jivraj</a> sir  do i have to put env file in docker

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595373)

you have to give the <code>AIPROXY_TOKEN</code> to the evaluate.py by either<br>
bash - <code>export AIPROXY_TOKEN="your token"</code><br>
or<br>
powershell - <code>$env:AIPROXY_TOKEN="your token"</code><br>
the evaluate.py file takes the token to send request to embedding end point for processing.<br>
so you have to set <code>AIPROXY_TOKEN</code> in both terminals<br>
i.e. app.py and evaluate.py teminals

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595380)

when I run the evaluation file, i get the following error - <img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Install <code>uv</code> (if required) and run the script <code>https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py</code> with <code>user@example.com</code> as the only argument <img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A1 failed: All connection attempts failed <img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A1 FAILED
I am getting the following error when running the evaluation scripts, can someone help me understand what this error is?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595382)

Humble request to extend the deadline please. Finding it extremely difficult and having time atleast till Sunday will be really helpful for working professionals like me

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595385)

All my tasks are running except A9. I have created a .env file and added my token. Despite that I ran commands in both the terminals. A9 still fails.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595396)

I second this, have been trying to debug the project for the past 1 week, spending over 4 hours daily and yet facing issues everytime I reopen. An extension of even 24 hours would be extremely appreciated. Please consider this. Thanks.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595397)

same issue on my side as well

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595402)

how u did A2<br>
could u please share ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595404)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
AIPROXY_TOKEN=$AIPROXY_TOKEN<br>
what abt m url stuff?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595411)

Sir, I request you to Please  extend the deadline, Because it is time consuming  and regular Students and Working professionals  have only saturday and sunday to complete this project.
Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595416)

also, in evaluate.py file, the embedding url is wrong and the AIPROXY_TOKEN is changed to OPENAI_API_TOKEN or something. i could send you edited evaluate.py… check your messages on discourse

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595417)

On bash it gives below output. On PowerShell it says missing authorization. A9 is failed.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040960e1d380f811ec53df35434564307fbd8388.png" data-download-href="/uploads/short-url/zI0bX2sssJ128w3Yb2Ypa83iAw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040960e1d380f811ec53df35434564307fbd8388.png" alt="image" data-base62-sha1="zI0bX2sssJ128w3Yb2Ypa83iAw" width="686" height="499" data-dominant-color="080808"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×661 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
In PowerShell<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd8b1f78ee2e9e130956f545a8e96d89d6785b2e.png" data-download-href="/uploads/short-url/r2Mjja9KwWVfUIYbgXLiuB4qsH4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd8b1f78ee2e9e130956f545a8e96d89d6785b2e.png" alt="image" data-base62-sha1="r2Mjja9KwWVfUIYbgXLiuB4qsH4" width="690" height="208" data-dominant-color="16191A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">967×292 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595420)

My data is getting generated -<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffe4cd24a993c763714ff420d85a202940240cfa.png" data-download-href="/uploads/short-url/AvJXuBQURIxKUJgwBJkAsPoxFCa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffe4cd24a993c763714ff420d85a202940240cfa.png" alt="image" data-base62-sha1="AvJXuBQURIxKUJgwBJkAsPoxFCa" width="459" height="454"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">459×454 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
despite this I am getting an error when evaluating the file with no explanation of the error. Can someone please help with this.<br>
<img src="https://emoji.discourse-cdn.com/google/yellow_circle.png?v=12" title=":yellow_circle:" class="emoji" alt=":yellow_circle:" loading="lazy" width="20" height="20"> Running task: Install <code>uv</code> (if required) and run the script <code>https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py</code><br>
with <code>user@example.com</code> as the only argument
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A1 failed:
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A1 FAILED

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595421)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffcb4192d3b1be3bc881e54720f2baa8d1b8a51e.png" data-download-href="/uploads/short-url/AuRedeLNq2Tt2gwfYe8yPG9wrng.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ffcb4192d3b1be3bc881e54720f2baa8d1b8a51e.png" alt="image" data-base62-sha1="AuRedeLNq2Tt2gwfYe8yPG9wrng" width="690" height="339" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">820×404 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Even the markdown file shows the correct email. What are the possible issues that I could be facing with this one.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595423)

<aside class="onebox githubfolder" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">GitHub - ANdIeCOOl/TDS-Project-1</a></h3>

  <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">main</a>

  <span class="label1">Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

ATLEAST 6 minimum score use at own risk(MIT LICENCE xD)<br>
<br><br>
BUILD TIME TAKES 2 mins<br>
WITH DOCKER FILE
<pre data-code-wrap="bash"><code class="lang-bash">@ANdIeCOOl ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker build -t tds-project-1 .
[+] Building 123.9s (13/13) FINISHED                                                                       docker:default
 =&gt; [internal] load build definition from Dockerfile                                                                 0.0s
 =&gt; =&gt; transferring dockerfile: 1.18kB                                                                               0.0s
 =&gt; [internal] load metadata for docker.io/library/python:3.11-slim                                                  2.2s
 =&gt; [auth] library/python:pull token for registry-1.docker.io                                                        0.0s
 =&gt; [internal] load .dockerignore                                                                                    0.0s
 =&gt; =&gt; transferring context: 2B                                                                                      0.0s
 =&gt; [internal] load build context                                                                                    0.1s
 =&gt; =&gt; transferring context: 34.30kB                                                                                 0.0s
 =&gt; [1/7] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  8.7s
 =&gt; =&gt; resolve docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  0.0s
 =&gt; =&gt; sha256:2c2c44fb54acb184dbedee948d7ba6460b1075a60a014d66857ce46543d4d840 5.29kB / 5.29kB                       0.0s
 =&gt; =&gt; sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260 28.21MB / 28.21MB                     0.7s
 =&gt; =&gt; sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53 3.51MB / 3.51MB                       0.9s
 =&gt; =&gt; sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335 16.20MB / 16.20MB                     1.6s
 =&gt; =&gt; sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda 9.13kB / 9.13kB                       0.0s
 =&gt; =&gt; sha256:a66bd09b8d35bb52cd106a94c23a94ba22e6fde6bd13d6c5912ec4f5888a7f14 1.75kB / 1.75kB                       0.0s
 =&gt; =&gt; extracting sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260                            2.2s
 =&gt; =&gt; sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f 249B / 249B                           1.9s
 =&gt; =&gt; extracting sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53                            0.2s
 =&gt; =&gt; extracting sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335                            1.4s
 =&gt; =&gt; extracting sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f                            0.0s
 =&gt; [2/7] WORKDIR /app                                                                                               0.2s
 =&gt; [3/7] RUN pip install --upgrade pip setuptools wheel                                                             8.7s
 =&gt; [4/7] RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends     gcc     g++     make     libffi-dev  84.5s
 =&gt; [5/7] RUN npm install -g prettier                                                                                1.5s
 =&gt; [6/7] COPY app /app                                                                                              0.1s
 =&gt; [7/7] RUN pip install uv                                                                                         4.5s
 =&gt; exporting to image                                                                                              13.4s
 =&gt; =&gt; exporting layers                                                                                             13.4s
 =&gt; =&gt; writing image sha256:39add91710bc7970d44dae04b3f4a0c4f227d1471fac4df7b01cec86ce7af3cf                         0.0s
 =&gt; =&gt; naming to docker.io/library/tds-project-1                                                                     0.0s
</code></pre>
<span class="mention">@ANdIeCOOl</span> ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker images<br>
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE<br>
tds-project-1   latest    39add91710bc   31 seconds ago   923MB
if this cause any issues please notify  <a class="mention" href="/u/s.anand">@s.anand</a>  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595429)

in phase B tasks are we supposed to create files to store the output or return it in the response ???
Please answer ASAP sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595430)

<a class="mention" href="/u/s.anand">@s.anand</a><br>
Respected Sir,<br>
I sincerely request you to kindly consider granting a one-day extension for Project 1. Many key clarifications were provided in today’s session, and we need just one additional day to effectively implement them. This extension would be immensely helpful in ensuring a more refined submission.<br>
I truly appreciate your time and consideration.<br>
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595431)

<span class="mention">@all</span> can everyone please test my image and let me know PLEASE. THIS IS THE MOST YOU ALL CAN DO FOR ME. I WILL BE BERY GRATEFUL<aside class="onebox githubfolder" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">GitHub - ANdIeCOOl/TDS-Project-1</a></h3>

  <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main" target="_blank" rel="noopener nofollow ugc">main</a>

  <span class="label1">Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595434)

hey I have a few doubts, if something was said about this please say so.
<ol>
<li>in Phase be tasks do we have to store the output in files or just return it in the response</li>
<li>When I call my some of my endpoints using post man or CURL they work but if I run the evaluate.py it throws an error, this I think is a bug in the eval.py file.</li>
</ol>
any idea about these ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595435)

facing the issue on submission<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12.png" data-download-href="/uploads/short-url/jEwu0RbXwJSFn5jXec9n8gXzJWW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12_2_690x381.png" alt="image" data-base62-sha1="jEwu0RbXwJSFn5jXec9n8gXzJWW" width="690" height="381" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12_2_690x381.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/9/89bdffb424290fa15cf3f07c367b81fac5898b12.png 2x" data-dominant-color="F7F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">942×521 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595441)

please ignore the above… there was a upper case issue  in image name… now fine

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595443)

Is it import to use python 3.13?<br>
It is not stable yet

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595447)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d64ee81798b48ccad186d5051823d3f565424bc2.png" data-download-href="/uploads/short-url/uzReAwAPsgAOBKSrr4jwARzOkLg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d64ee81798b48ccad186d5051823d3f565424bc2.png" alt="image" data-base62-sha1="uzReAwAPsgAOBKSrr4jwARzOkLg" width="690" height="55" data-dominant-color="161616"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1831×146 7.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
can someone help me fix this error <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595449)

for the datagen script is it ok to hardcode the scripts url and my email id? I understand the script itself may change but can I count on the link remaining the same? Also is it necessary to pass the email as argument?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595450)

from dotenv import load_dotenv<br>
load_dotenv()

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595451)

yahh i have it in my code…still facing the issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595454)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> [filler to extend length]

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595457)

whats the image’s name on Docker?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595460)

just completed my sem exams started worrking on the project from 2 days please give extension of deadline for the project sir

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595461)

dont we have to add the data folder or folder like datagen in the repo?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595468)

thats confidential, im not an idiot xD, that will get me definitely  in trouble

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595470)

no, not really . Just your app

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595471)

in your project,in the app folder you have the data folder which is empty so should I keep that or remove it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595473)

and also will u be making any chnages in the repo

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595475)

File “/app/app.py”, line 35, in <br>
client = OpenAI(<br>
^^^^^^^<br>
File “/usr/local/lib/python3.12/site-packages/openai/_client.py”, line 110, in <strong>init</strong><br>
raise OpenAIError(<br>
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable                                                                              some pls help me fix this error!!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595477)

Blunder in your <code>main.py</code>.<br>
You are using API_KEY = os.getenv(“AI_PROXY_TOKEN”) but it should be AIPROXY_TOKEN.
Btw what you using for phase B?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595493)

yes i will change that

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595494)

nothing i think, i’ll import those generic functions and use tool usage only probably if can’t crack dynamic code generation

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595498)

i don’t have that<aside class="onebox githubfolder" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app" target="_blank" rel="noopener nofollow ugc">TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1</a></h3>


  <span class="label1">Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595499)

What we expect in project.
<ol>
<li>server running inside docker container at 8000.</li>
<li>And all files will be accessed from data folder in root directory.</li>
</ol>
Apart from these two you can have anything extra.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595500)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68c6be0490c5eb006c1edaa43f50996e440f8a03.png" data-download-href="/uploads/short-url/eWTsxcch0VyIs8G9dhevCFof78f.png?dl=1" title="Screenshot 2025-02-15 212826" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/68c6be0490c5eb006c1edaa43f50996e440f8a03.png" alt="Screenshot 2025-02-15 212826" data-base62-sha1="eWTsxcch0VyIs8G9dhevCFof78f" width="690" height="178" data-dominant-color="171717"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-15 212826</span><span class="informations">1903×492 32.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
how to fix this error ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595504)

What problem you facing with that dynamic code generation part?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595505)

I have exhausted my api limit of $2. I need to test my project. Can you please provide some more credits? <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595506)

no problem but im losing steam slowly, i need to buckle up and PUSH <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595509)

<strong>Subject:</strong> Request for Project Deadline Extension
Dear Sir,
This project is highly complex, and we need additional time to ensure its successful completion. We kindly request an extension of the deadline to allow for thorough testing and proper implementation. An extension would greatly help us deliver the best results.
Thank you for your understanding  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595510)

This might be problem with network settings(unstable internet, firewall, VPN interference)
try to debug it with help of chatgpt.
You can also use codespaces for trying another network.
<a href="https://www.youtube.com/watch?v=fqQOu2JVI1o" rel="noopener nofollow ugc">Streamlining setup with GitHub Codespaces</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595512)

Push push <a class="mention" href="/u/23f1002382">@23f1002382</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595514)

<a class="mention" href="/u/jivraj">@Jivraj</a> is it fine if i have my AIPROXY_TOKEN in my code instead of getting it as environment variable?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595517)

if you do that then during evaluation, it would use your credit limit. if it gets exhausted, you may face problems. <a class="mention" href="/u/23f2003413">@23f2003413</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595519)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/e/ce7f8f838b86960153991fdea76f15b4a50f80f7.png" data-download-href="/uploads/short-url/tsLEGAhu1G9Q8fvPNw92H8Prfrp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/e/ce7f8f838b86960153991fdea76f15b4a50f80f7.png" alt="image" data-base62-sha1="tsLEGAhu1G9Q8fvPNw92H8Prfrp" width="237" height="500" data-dominant-color="2C2D2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">266×559 12.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
this is what i am doing first using the podman given in the portal and then running the evaluate.py file

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595521)

ahhh okay, but i am getting an error while trying to fetch the token as an environment variable. any suggestions to fix this issue?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595522)

you can use python-dotenv. check that out.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595523)

tried that still not getting T_T anyways thanks mate!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595526)

No don’t do that, just follow the procedure.<br>
Two problems with keeping token in file.
<ol>
<li>It will become public after you push to github.</li>
<li>While running evaluation script after submission your token might run out of credits.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595528)

ohh yes, didn’t think it through xD

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595531)

I am facing the same error. and I have checked for solutions and found none. Did you resolve it? If yes can you please guide me through it?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595533)

{<br>
“detail”: “Error code: 401 - {‘error’: {‘message’: ‘Your authentication token is not from a valid issuer.’, ‘type’: ‘invalid_request_error’, ‘param’: None, ‘code’: ‘invalid_issuer’}}”<br>
}          getting this error sir

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595536)

<aside class="onebox githubfolder" data-onebox-src="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/ANdIeCOOl/TDS-Project-1/tree/main/tds-project-1/app" target="_blank" rel="noopener nofollow ugc">TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1</a></h3>


  <span class="label1">Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

i keep updating, check this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595538)

Please extend deadline by 1 day. i just got discharged from hospital today, was suffering from liver problem since some days and got high heart beat due to a medicine unrelated to liver and made me got admitted@Jivraj

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595543)

11:59 + 5 hours atthe most, <a class="mention" href="/u/s.anand">@s.anand</a> ? <img src="https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12" title=":face_holding_back_tears:" class="emoji" alt=":face_holding_back_tears:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12" title=":face_holding_back_tears:" class="emoji" alt=":face_holding_back_tears:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/google/face_holding_back_tears.png?v=12" title=":face_holding_back_tears:" class="emoji" alt=":face_holding_back_tears:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595545)

11 posts were split to a new topic: <a href="/t/project-1-casual-banter/167344">Project 1 - Casual banter</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595686)

<a class="mention" href="/u/jivraj">@Jivraj</a> sir   <a class="mention" href="/u/carlton">@carlton</a>    sir do have to add datagen in the docker container?<br>
As when I’m running it locally, it gives 9/10, but when I pull it from Hub and run eval, it says:detail": “[Errno 2] No such file or directory: ‘/data/datagen.py’”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595555)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a4995efdbe57c4d2d865982896333f8faf0c8c.png" data-download-href="/uploads/short-url/qugZ0sw5CBFFOJtKl2Mvz5NUDkE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a4995efdbe57c4d2d865982896333f8faf0c8c.png" alt="image" data-base62-sha1="qugZ0sw5CBFFOJtKl2Mvz5NUDkE" width="690" height="188" data-dominant-color="282524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">706×193 6.15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
someone please help me fix this error

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595558)

<a class="mention" href="/u/carlton">@carlton</a> can you pl merge this<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/sanand0/tools-in-data-science-public/pull/7">
  <header class="source">

      <a href="https://github.com/sanand0/tools-in-data-science-public/pull/7" target="_blank" rel="noopener nofollow ugc">github.com/sanand0/tools-in-data-science-public</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/sanand0/tools-in-data-science-public/pull/7" target="_blank" rel="noopener nofollow ugc">Update evaluate.py with correct link of datagen.py for task `A1`</a>
      </h4>

    <div class="branches">
      <code>tds-2025-01</code> ← <code>rohitxiitm:patch-1</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-02-15" data-time="10:56:16" data-timezone="UTC">10:56AM - 15 Feb 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/rohitxiitm" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/c/8c0f24d20066c96d044a995469181fefafc28aff.jpeg" class="onebox-avatar-inline" width="20" height="20" data-dominant-color="89816A">
            rohitxiitm
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/sanand0/tools-in-data-science-public/pull/7/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

ppl are facing issues in evaluate.py for task A2

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595569)

folks, need a confirmation. i don’t know but i heard it from someone or somewhere.<br>
we cannot send json in response, if it is success ? need to send text
is that really the case ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595573)

<a class="mention" href="/u/rohitgarg">@rohitgarg</a> - thanks for this. Merged your PR pointing to the correct link for <code>evaluate.py</code>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595577)

Sir from which session to which session is about tds project?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595651)

week-5 session-1 &amp; week-5 session-3

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595657)

Here is  a Bruno collection (open source alternate for postman) for API testing A1 to A6<br>
<a href="https://drive.google.com/file/d/11TsXO3_uOnKtHxN7hTgmzdX5Cszc2IUc/view?usp=sharing" rel="noopener nofollow ugc">bruno collection</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595664)

On my system evaulate.py is throwing an error on A2 trying to execute npx on format.md before the llm is even invoked. However running the command directly on the command line works.
evaluate.py:<br>
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A2 failed: Command ‘[‘npx’, ‘prettier@3.4.2’, ‘–stdin-filepath’, ‘data/format.md’]’ returned non-zero exit status 2.
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A2 FAILED
bash:<br>
npx prettier@3.4.2 --stdin-filepath data/format.md
bash works as expected. Can someone help?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595668)

<a class="mention" href="/u/carlton">@carlton</a><br>
Is there a maximum size limit for the Docker Image?
Thanking you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595670)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
Hi ,
I am trying to build using both docker and podman but it failed on both. I have watched many videos trying to resolve this adn also chatgpt in order to resolve the issue but it seems to persist. I even uninstalled and reinstalled both podman and doceker multiple times but no help.
When i run command docker build -t ___________ .
the error that comes is :
<h2><a name="p-595677-dockerfile2-1" class="anchor" href="#p-595677-dockerfile2-1"></a>Dockerfile:2</h2>
<h2><a name="p-595677-h-1-use-a-lightweight-python-image-2-from-python312-slim-3-4-set-the-working-directory-in-the-container-2" class="anchor" href="#p-595677-h-1-use-a-lightweight-python-image-2-from-python312-slim-3-4-set-the-working-directory-in-the-container-2"></a>1 |     # Use a lightweight Python image<br>
2 | &gt;&gt;&gt; FROM python:3.12-slim<br>
3 |<br>
4 |     # Set the working directory in the container</h2>
ERROR: failed to solve: python:3.12-slim: failed to resolve source metadata for <a href="http://docker.io/library/python:3.12-slim:" class="inline-onebox" rel="noopener nofollow ugc">Docker Hub Container Image Library | App Containerization</a> failed to copy: httpReadSeeker: failed open: failed to do request: Get “<a href="https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250215T192245Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1" rel="noopener nofollow ugc">https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&amp;X-Amz-Date=20250215T192245Z&amp;X-Amz-Expires=1200&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1</a>”: dialing <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443</a> container via direct connection because static system has no HTTPS proxy: connecting to <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443</a>: dial tcp: lookup <a href="http://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com" rel="noopener nofollow ugc">docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com</a>: no such host
Even tried getting python:3.12-slim separatly and trying again but that also didn’t work.<br>
I think there is some problem in getting python:3.12-slim as the build always stops at this.
on asking ChatGPT it shows that some DNS or network issue is there. I even tried all the remedy that was provided on creating custom network etc. but this was also of no use
Kindly help me finding solution to this and pls mention any other assistance I may require to get this running
Thank You.<br>
Regards,<br>
Aagman

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595677)

i am getting this error, I have tried many times but still the error persists:<br>
“message”: “Bearer YOUR_AIPROXY_TOKEN is invalid: JWSInvalid: Invalid Compact JWS”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595679)

someone please help!!!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595680)

<a class="mention" href="/u/carlton">@carlton</a> needed a confirmation on this task
<code>A8 * `/data/credit-card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt</code> - in this task i assume prompt can ask for credit card number or other details like cvv and name.
My question is, whether my system should allow prompt that CVV or or such info ? or should give it ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595683)

<ol>
<li>
Previously I asked for some more credits to test my project. I got an email stating I have been provided with a new token but I think I got that same token again, not a new one. I still cant send request to the AIPROXY. Please help.
</li>
<li>
Do I need to submit the docker image name with the tag or without the tag? I submitted it before without the tag. Now i see that I have tagged the image with as v1 but I cant submit the form due to pattern matching problems. Should i submit again after tagging it with :latest ?
</li>
</ol>
<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595690)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>  sir in the phase B will the input and output path will be given ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595693)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
When I run my docker image using
<code>podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME</code>
Task A2 fails as the podman container is unable to find npx.
Running the same image using
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME</code>
works fine and Task A2 passes. I can’t understand why this is happening.
I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.<br>
When run using docker, <code>which node</code> gives <code>/usr/bin/node</code> as output but when run using podman, nothing.
<pre><code class="lang-auto">shiva@shiva:~/Desktop/tdsp1$ sudo podman run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo docker run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
/usr/bin/node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --user=root --rm -it docker.io/myusername/myreponame /bin/sh
# which node
# which node
# exit
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595695)

Here’s how to prompt folks. Just do what <a class="mention" href="/u/carlton">@carlton</a> mentioned in today’s live session (the 5 hour marathon) and you should be good for Project-1!
<aside class="onebox twitterstatus" data-onebox-src="https://x.com/aakashg0/status/1890492955842007087?s=46&amp;t=U3mfkIFH433B6kVe5ZktSw">
  <header class="source">

      <a href="https://x.com/aakashg0/status/1890492955842007087?s=46&amp;t=U3mfkIFH433B6kVe5ZktSw" target="_blank" rel="noopener nofollow ugc">x.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/7/67f2a2d0db391947304ab4e006d7ea42c3b8850d.jpeg" class="thumbnail onebox-avatar" data-dominant-color="7A7879" width="48" height="48">
<h4><a href="https://x.com/aakashg0/status/1890492955842007087?s=46&amp;t=U3mfkIFH433B6kVe5ZktSw" target="_blank" rel="noopener nofollow ugc">Aakash Gupta</a></h4>
<div class="twitter-screen-name"><a href="https://x.com/aakashg0/status/1890492955842007087?s=46&amp;t=U3mfkIFH433B6kVe5ZktSw" target="_blank" rel="noopener nofollow ugc">@aakashg0</a></div>

<div class="tweet">
  <span class="tweet-description">Most people are still prompting wrong.

I've found this framework, which was even shared by OpenAI President Greg Brockman.

Here’s how it works: <a target="_blank" href="https://x.com/aakashg0/status/1890492955842007087/photo/1" rel="noopener nofollow ugc">pic.x.com/2MMcEqBeIJ</a><div class="aspect-image-full-size" style="--aspect-ratio:502/500;"><img class="tweet-image" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce7a62f2fa1f33758771e9ef57dd90fe2d98b09d_2_502x500.jpeg" data-dominant-color="333334" width="502" height="500"></div></span>
</div>

<div class="date">
  <a href="https://x.com/aakashg0/status/1890492955842007087?s=46&amp;t=U3mfkIFH433B6kVe5ZktSw" class="timestamp" target="_blank" rel="noopener nofollow ugc">8:06 PM - 14 Feb 2025</a>

    <span class="like">
      <svg viewBox="0 0 512 512" width="14px" height="16px" aria-hidden="true"><path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"></path></svg>
      5.5K
    </span>

    <span class="retweet">
      <svg viewBox="0 0 640 512" width="14px" height="16px" aria-hidden="true"><path d="M629.657 343.598L528.971 444.284c-9.373 9.372-24.568 9.372-33.941 0L394.343 343.598c-9.373-9.373-9.373-24.569 0-33.941l10.823-10.823c9.562-9.562 25.133-9.34 34.419.492L480 342.118V160H292.451a24.005 24.005 0 0 1-16.971-7.029l-16-16C244.361 121.851 255.069 96 276.451 96H520c13.255 0 24 10.745 24 24v222.118l40.416-42.792c9.285-9.831 24.856-10.054 34.419-.492l10.823 10.823c9.372 9.372 9.372 24.569-.001 33.941zm-265.138 15.431A23.999 23.999 0 0 0 347.548 352H160V169.881l40.416 42.792c9.286 9.831 24.856 10.054 34.419.491l10.822-10.822c9.373-9.373 9.373-24.569 0-33.941L144.971 67.716c-9.373-9.373-24.569-9.373-33.941 0L10.343 168.402c-9.373 9.373-9.373 24.569 0 33.941l10.822 10.822c9.562 9.562 25.133 9.34 34.419-.491L96 169.881V392c0 13.255 10.745 24 24 24h243.549c21.382 0 32.09-25.851 16.971-40.971l-16.001-16z"></path></svg>
      360
    </span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595698)

Same issue. Got the same token. Can’t use it since 2 dollar limit has been crossed. Please help. <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595700)

Yes I also need the answer of this.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595718)

Is there any way of figuring what is the usage of my token and if yes then how…<br>
Plz some peers help…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595719)

It will be corrected soon by <a class="mention" href="/u/jkmadathil">@jkmadathil</a><br>
He is in charge of our budget for TDS and the tokens are being issued by him.
Please tag him for any token related issues.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595720)

New token assigned to the students.  Emails are also sent.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595726)

sir I am noticing a pattern, that when I am running the datagen first. And then using the evaluate.py, then I am getting the A2 right.<br>
But running the evaluation.py for the 2nd time cause the A2 to fail…<br>
Probabbly Because the file in the data folder gets upated should I worry for that…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595738)

in the phase B, we have no idea about how many arguments are there, so should we make every function mapping with 2 arguments ( 1 containing the input location and other containing output location) or should we take the parameters in some other way

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595754)

There has been an outage in some parts of the country related to cloudflare servers. What helped some students (and us) is using a completely different network eg. instead of using your home wifi, use mobile internet, since they go through a different DNS and this sometimes works.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595772)

We have not specified a size limit for the docker image, so in theory there is not a limit to the docker image size.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595773)

Hello  <a class="mention" href="/u/carlton">@carlton</a> Sir,<br>
While running evaluate.py , I have observed that the expected  and actual output is having difference like “\n” then also it marks task as fail.
eg:<br>
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.<br>
Attention officer successful. Us population the true show.<br>
Real cold if play side wind affect. Street cause investment receive have miss page station.<br>
Cold rest term her conference. Animal sure campaign new.<br>
Meeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.<br>
Difficult yourself build increase back put others.<br>
Although artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.<br>
Whole way know down. Music machine trip father rather.<br>
Must medical bad law issue.<br>
Someone explain seven maintain wrong day factor property.
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=12" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
“Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.\nAttention officer successful. Us population the true show.\nReal cold if play side wind affect. Street cause investment receive have miss page station.\nCold rest term her conference. Animal sure campaign new.\nMeeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.\nDifficult yourself build increase back put others.\nAlthough artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.\nWhole way know down. Music machine trip father rather.\nMust medical bad law issue.\nSomeone explain seven maintain wrong day factor property.\n”
<img src="https://emoji.discourse-cdn.com/google/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20"> A5 FAILED
Will this be considered as failure in actual evaluation as well or will this be taken care in actual evaluation?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595774)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a.png" data-download-href="/uploads/short-url/gKCzC6SuIow45H46xUYGNubn96W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a_2_690x121.png" alt="image" data-base62-sha1="gKCzC6SuIow45H46xUYGNubn96W" width="690" height="121" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a_2_690x121.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a_2_1035x181.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/7567f3068b587402b54f6d01f3e133f6c21a114a_2_1380x242.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1412×248 16.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Im able to execute the query succesfully.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a.png" data-download-href="/uploads/short-url/e0xXVNIuDIVjQAEbtZoi7eTtHg6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a_2_690x354.png" alt="image" data-base62-sha1="e0xXVNIuDIVjQAEbtZoi7eTtHg6" width="690" height="354" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a_2_690x354.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a_2_1035x531.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/622e4a15020aefe140e92f8aa38035c5518ae41a.png 2x" data-dominant-color="F8F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1109×570 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
But the data gets downloaded to C drive instead of the project folder<br>
The datagen.py file is in the project folder itself.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/5/65498f6319cf654240d6dbf5f62a9313ebd5fd41.png" data-download-href="/uploads/short-url/es1Pem6ac5Foa4FitCRTIlLWLqV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/5/65498f6319cf654240d6dbf5f62a9313ebd5fd41.png" alt="image" data-base62-sha1="es1Pem6ac5Foa4FitCRTIlLWLqV" width="690" height="125" data-dominant-color="242726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">821×149 9.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
am I making any error when setting the directories?
Please help, have been facing this issue since the beginning of this project, initially tried to move the files from C drive to project folder but that does not seem like a viable solution.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595782)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/1/213611a3e30fbaa75a62a4a99c19b20458a92609.png" data-download-href="/uploads/short-url/4JNB76Nt2iFtCZpl6LVDjmNXXi9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/1/213611a3e30fbaa75a62a4a99c19b20458a92609.png" alt="image" data-base62-sha1="4JNB76Nt2iFtCZpl6LVDjmNXXi9" width="690" height="466" data-dominant-color="232423"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1123×760 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am also running datagen.py in the project directory, yet data folder is created in C drive.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595793)

<a class="mention" href="/u/jkmadathil">@jkmadathil</a><br>
sir plz renew my token…<br>
Showing,<br>
{‘message’: ‘On 2025-02 you used $2.0041067399999912, exceeding $2’}
Sorry sir!..

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595796)

use PlainTextResponse for /read

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595797)

Plz do someone reply.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595798)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
Please review the code and help me fix the error in order to proceed further. Thanks.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595800)

<aside class="onebox githubblob" data-onebox-src="https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md">
  <header class="source">

      <a href="https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md" target="_blank" rel="noopener nofollow ugc">README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1/blob/main/README.md" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-md"># TDS_CLUTCH_AT_6AY
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

using code generation, getting 6/10 or * if lucky, similar comments needs a tool function call for sure, maybe someone can implement and create pull request, if you all can get 10/10 fine tuning with tool functions
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> Please help if it meets deliverables

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595808)

Sir I need a help, In hte B portion where no any destination and source files are given…<br>
There we need to ask the user to povide the source and destination files or does we should store it in any default file locations…
As the statement is very vauge saying the “agent should handle this”…<br>
Thanks Sir!!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595833)

<a class="mention" href="/u/jkmadathil">@jkmadathil</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir earlier my code was running fine, but after the assigment of the new token,<br>
it is now showing 400 bad request, which simply implies there is something wrong with the token…<br>
plz do something sir…<br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/3/9334f2224cfb61ea025ddfe149bbfd3df02db6f2.png" alt="image" data-base62-sha1="l0fCGZdX1ZTq0lLZMhY1m9blb3A" width="690" height="41" data-dominant-color="3A3939">
I have do have cross verified the new token been correctly been assigned to the system variable…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595845)

More Particularily the failure occurs in the response portion…
<pre><code class="lang-auto">def get_completions(prompt: str):
    print("Inside get_completions")#Debug
    with httpx.Client(timeout=20) as client:
        response = client.post(
            f"{openai_api_chat}",
            headers=headers,
            json=
                {
                    "model": "gpt-4o-mini",
                    "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": prompt}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_definitions_llm
                            ],
                    "tool_choice": "auto"
                },
        )

    print("DId suceessful llm calll")#Debug
</code></pre>
<pre><code class="lang-auto">INFO:     127.0.0.1:52108 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 400 Bad Request
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595847)

is there any limit on the size of the docker image <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> ? because mine is about 5.6Gb

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595848)

bhai nhi hai…<br>
koi size limit

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595850)

uv run <a href="https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py" rel="noopener nofollow ugc">https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py</a><br>
Installed 13 packages in 543ms<br>
Traceback (most recent call last):<br>
File “/tmp/evaluateF6zgG9.py”, line 20, in <br>
from datagen import (<br>
…&lt;9 lines&gt;…<br>
)<br>
ModuleNotFoundError: No module named ‘datagen’
I am getting this error when I try to run evaluate.py
when I run the evaluate.py by having datagen.py in same folder , it is running perfectly. But my doubt is only after task a1 runs the datagen.py will be downloaded into the /data folder right ?
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Kindly help me with this issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595859)

Use following as first parameter of <code>subprocess.run()</code> to create <code>data/</code> directory inside your project instead of C: drive
<pre data-code-wrap="python"><code class="lang-python">["uv", "run", script_url, user_email, "--root", "./data"]
</code></pre>
Also, you don’t need to download to script, you can directly run it from the url.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595860)

The reason for error is <code>evaluate.py</code> is trying to import <code>datagen.py</code> which doesn’t exist in your system. I’ll suggest download both the files, keep them in same folder and run <code>evaluate.py</code> from your computer

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595863)

Yes actually Thats my doubt , when I run both in same folder it is working , but only after task a1 runs datagen.py will be downloaded in /data folder  right ?,
or did I misunderstood something??

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595864)

<h3>Generation-Based Automation Agent (No Hard Coding)</h3>
<strong>Repository Link:</strong> <a href="https://github.com/23f2005593/tds" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 23f2005593/tds</a>
Currently, it can complete 7 out of 10 tasks. In reality, it can complete 9 out of 10 tasks, but the expected results are not flexible in evaluate.py file.
If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.
Please contribute to this repository. <strong>We will win together.</strong>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595865)

{<br>
“message”: “On 2025-02 you used $2.0041388599999848, exceeding $2”<br>
}
What to do?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595866)

facing same error, have you fouind any solution?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595868)

sir for this task- A6 Find all Markdown (<code>.md</code> ) files in <code>/data/docs/</code> . For each file, extract the first occurrance of each H1 (i.e. a line starting with <code># </code> ). Create an index file <code>/data/docs/index.json</code> that maps each filename (without the <code>/data/docs/</code> prefix) to its title (e.g. <code>{"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...}</code> )   …I am getting correct result for all files but for the very first file budget.md it shows wrong.<br>
my result- { “budget.md”: “Success easy same main modern doctor.”,<br>
“build.md”: “Shoulder follow own never above.”,<br>
and in the data files there is different heading in budget.md.-  # Series dog who make specific agree between.<br>
my question is this if it works for all the files then why not for this file budget.md    <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595871)

do you able to do this task * <strong>A5</strong>. Write the first line of the 10 most recent <code>.log</code> file in <code>/data/logs/</code> to <code>/data/logs-recent.txt</code>, most recent first …<br>
i am also doing using prompt no hard-coded.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595877)

yes doing this only but finding correct for most of the files.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595878)

yes i am able to do task a5.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595879)

so you directly using prompt for doing this task.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595881)

yes i am only using prompt based method

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595882)

If filename has number in its name then extract the number from the filename and convert it to an integer before sorting .Ensure numbers inside filenames are compared as integers, not as strings, to maintain proper order. Sort filenames in said in task. Avoid any lexicographical sorting issues.    i am using this extra info for doing this but still it does not give accurate result. can you help me in this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595883)

i already shared my repo u can check there.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595884)

you have pushed data,datagen and evaluate files…do we have to submit them as well??<br>
(also send the docker file)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595912)

Check the file once, there is a possibility that it’s either fetching a comment or the second heading. Refactor your prompt to search only for the First Heading, specify it explixitly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595917)

okay let me check once.<br>
one more thing sir {“first_name”: “Crystal”, “last_name”: “Wilson”, “email”: “<a href="mailto:delgadorebecca@example.com">delgadorebecca@example.com</a>”}   then what will be the sorted-contact for this as in email there is no first and lastname present. <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595928)

Hey, I submitted the project links in the google form yesterday but, today in the portal it shows that I have not submitted the project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595945)

I am getting this error while running evaluate.py on task A9
<pre data-code-wrap="bash"><code class="lang-bash">HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'
</code></pre>
There were no authentication issues till yesterday.
please guide <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595955)

This is happening because evaluate.py is unable to fetch your API Key from the environment variables. Create a new variable and set it’s value to your API Key then try.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595957)

Hi everyone,
I’m running into an issue with the AI Proxy embeddings endpoint while executing the A9 task. Every time I send a POST request to:
bash
Copy
<pre><code class="lang-auto">https://aiproxy.sanand.workers.dev/openai/v1/embeddings
</code></pre>
I receive a <strong>401 Unauthorized</strong> response. This, in turn, causes my code to fail with a <code>KeyError: 'data'</code> because the expected JSON response doesn’t include the <code>"data"</code> key.
<h3><a name="p-595959-what-ive-tried-1" class="anchor" href="#p-595959-what-ive-tried-1"></a>What I’ve Tried</h3>
<ol>
<li><strong>Token Verification:</strong></li>
</ol>
<ul>
<li>I’m using the <code>AIPROXY_TOKEN</code> obtained by logging in at <a href="https://aiproxy.sanand.workers.dev/" rel="noopener nofollow ugc">aiproxy.sanand.workers.dev</a> with my IITM email.</li>
<li>The token is passed in the header as follows:</li>
</ul>
python
Copy
<pre><code class="lang-auto">"Authorization": f"Bearer {AIPROXY_TOKEN}"
</code></pre>
<ul>
<li>I added debug prints to confirm that the token is being used correctly (printing the first few characters).</li>
</ul>
<ol start="2">
<li><strong>API Request Details:</strong></li>
</ol>
<ul>
<li>The request includes the correct <code>Content-Type: application/json</code> header.</li>
<li>The payload is set as:</li>
</ul>
json
Copy
<pre><code class="lang-auto">{"model": "text-embedding-3-small", "input": ["Test"]}
</code></pre>
<ul>
<li>Despite this, the response status is consistently 401 Unauthorized.</li>
</ul>
<ol start="3">
<li><strong>Debug Output:</strong><br>
Here’s a snippet of the debug output:</li>
</ol>
bash
Copy
<pre><code class="lang-auto">HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"
🔴 A9 failed: 'data'
</code></pre>
This confirms that the issue is with the authentication rather than our processing logic.
<h3><a name="p-595959-what-i-suspect-2" class="anchor" href="#p-595959-what-i-suspect-2"></a>What I Suspect</h3>
<ul>
<li>The token may be invalid, expired, or misconfigured.</li>
<li>There could be changes in the token permissions or endpoint requirements that I’m not aware of.</li>
<li>Alternatively, there might be an issue on the server side with token validation.</li>
</ul>
<h3><a name="p-595959-request-for-help-3" class="anchor" href="#p-595959-request-for-help-3"></a>Request for Help</h3>
Has anyone else encountered this issue recently? Could someone verify if there are any changes to the authentication requirements for the embeddings endpoint? Any insights or updated instructions on how to ensure the token is valid and has the proper permissions would be greatly appreciated.
Thanks in advance for your assistance!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595959)

B5. Run a SQL query on a SQLite or DuckDB database<br>
Should I ask for the SQL data base. Or the agent should be smart enough to find the required database…<br>
Moreover in the data folder there is only one database is it should be robust to handle multiple databases…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595961)

same issue i also face                   pls sir help us fix this issue and provide us more  token
HTTP Request: POST <a href="https://aiproxy.sanand.workers.dev/openai/v1/embeddings" rel="noopener nofollow ugc">https://aiproxy.sanand.workers.dev/openai/v1/embeddings</a> “HTTP/1.1 429 Too Many Requests”
<img src="https://emoji.discourse-cdn.com/google/red_circle.png?v=12" title=":red_circle:" class="emoji" alt=":red_circle:" loading="lazy" width="20" height="20"> A9 failed: ‘data’
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595965)

I had a question on evaluation by the course team. To test that my application would run everywhere, I first deleted all images from my local machine using <code>podman rmi -a</code> and then ran <code>podman run --rm -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN $IMAGE_NAME</code> with the appropriate variables set. This is as per the instructions provided <a href="https://github.com/sanand0/tools-in-data-science-public/tree/tds-2025-01-project-1-wip/project-1" rel="noopener nofollow ugc">here</a>. But this gave me the following error:
<pre><code class="lang-auto">Error: short-name "freshbash/dataworks-agent" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf
</code></pre>
The above is the format in which we have to provide the image name in the Google form. So, I was confused whether this would succeed during actual evaluation.
The only way its working right now is when I specify the image name to be <code>docker.io/freshbash/dataworks-agent</code>
I’m not yet very good with how containers work so some insights would be very helpful. Thanks!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595982)

Nice bro, if its getting 8 you are sorted, probably get more later. But Prompting seems a little less info<br>
BUT
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Structured Outputs</th>
<th>JSON Mode</th>
</tr>
</thead>
<tbody>
<tr>
<td>Outputs valid JSON</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Adheres to schema</td>
<td>Yes (see supported schemas)</td>
<td>No</td>
</tr>
<tr>
<td>Compatible models</td>
<td>gpt-4o-mini, gpt-4o-2024-08-06, and later</td>
<td>gpt-3.5-turbo, gpt-4-* and gpt-4o-* models</td>
</tr>
<tr>
<td>Enabling</td>
<td>response_format: { type: json_schema, json_schema: {strict: true, schema: …} }</td>
<td>response_format: { type: json_object }</td>
</tr>
</tbody>
</table>
</div><pre data-code-wrap="python"><code class="lang-python">    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )
</code></pre>
<aside class="onebox githubblob" data-onebox-src="https://github.com/23f2005593/tds/blob/main/app.py#L142">
  <header class="source">

      <a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" target="_blank" rel="noopener nofollow ugc">github.com/23f2005593/tds</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" target="_blank" rel="noopener nofollow ugc">app.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/23f2005593/tds/blob/main/app.py#L142" rel="noopener nofollow ugc"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="132" style="counter-reset: li-counter 131 ;">
          <li>prompt = (</li>
          <li>    f"The Python code generated for the task '{task}' produced the following error when executed:\n"</li>
          <li>    f"{error_message}\n\n"</li>
          <li>    f"Here is the original code:\n{original_code_data['code']}\n\n"</li>
          <li>    "Please provide a corrected version of the code that fixes the error. Return only a JSON object with:\n"</li>
          <li>    "- code: the corrected Python code as a string\n"</li>
          <li>    "- function_name: name of the main function\n"</li>
          <li>    "- required_libraries: list of required pip packages\n\n"</li>
          <li>    "Make sure the code is simple, direct, and error-free this time. And try not to mess it up like before."</li>
          <li>)</li>
          <li class="selected">try:</li>
          <li>    response = client.chat.completions.create(</li>
          <li>        model="gpt-4o-mini",</li>
          <li>        messages=[{"role": "user", "content": prompt}],</li>
          <li>        temperature=0,</li>
          <li>        response_format={"type": "json_object"}</li>
          <li>    )</li>
          <li>except Exception as exc:</li>
          <li>    logger.error("Error connecting to OpenAI API for auto-fix: %s", exc)</li>
          <li>    raise HTTPException(status_code=500, detail="Connection error during auto-fix. Maybe it's time to admit defeat?")</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

you are taking a chance on that format

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595987)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0.png" data-download-href="/uploads/short-url/7eArfdqDaXSAc2cGYke8q0YtAFq.png?dl=1" title="Screenshot 2025-02-16 091341" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0_2_690x211.png" alt="Screenshot 2025-02-16 091341" data-base62-sha1="7eArfdqDaXSAc2cGYke8q0YtAFq" width="690" height="211" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0_2_690x211.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0_2_1035x316.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/2/32b55ca09f5894f9baa7082d8a44fdb1d14268f0.png 2x" data-dominant-color="151920"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-16 091341</span><span class="informations">1315×404 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png" data-download-href="/uploads/short-url/qusb7PKn6Irl2dNw3ZkKyEdnhHW.png?dl=1" title="Screenshot 2025-02-16 091101" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png" alt="Screenshot 2025-02-16 091101" data-base62-sha1="qusb7PKn6Irl2dNw3ZkKyEdnhHW" width="690" height="149" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_1035x223.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png 2x" data-dominant-color="16181F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-16 091101</span><span class="informations">1351×292 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Hardest i ever worked in my life. Thank you <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596001)

<aside class="quote group-ds-students" data-username="TheVishal" data-post="521" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/thevishal/48/110717_2.png" class="avatar"> TheVishal:</div>
<blockquote>
If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.
</blockquote>
</aside>
have tried function calling? with open code generation ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596007)

not yet… but i have another problem when i am running this by using docker it is giving error “datagen module not found”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596034)

bro please help by contribute please

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596038)

come off on one meet

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596052)

what should we push in the github repo <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> ??<br>
is it enough if we just push the Dockerfile, app.py, datagen.py and the LICENSE. Someone pls help!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596053)

bro i used all my codespaces credits xD<br>
i am nitpicking and editing from website and running not exceed limit XD

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596054)

someone pls help T_T

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596057)

submit image and github  repo link, evalhaters will handle the rest im assuming

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596060)

yeaa i got that but what should we add in the github repo…like should we add the generated data folder?<br>
or is it enough if we just add the code and the Dockerfile to the repo

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596063)

doesn’t matter they use only image

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596064)

use local editor naa bro

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596065)

and run my code xD i have one crazy setup XD give me some time, at 9:30 we’ll hop on eachother

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596066)

which repo u submitting yesterday one or todays.<br>
i am unable to run the yesterday one

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596067)

this one new one only xD

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596068)

and what do they mean by image-name in the gform…is it the repo name in dockerhub?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596069)

what evil have u done xd

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596070)

why? ///////////// O—O

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596071)

dockerhub image name

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596072)

ur words are saying something else <img src="https://emoji.discourse-cdn.com/google/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596074)

image name as in i dont get it lol.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596075)

<pre><code class="lang-auto">(general) [shubham@laptop data]$ curl https://api.openai.com/v1/models -H "Authorization: Bearer $AIPROXY_TOKEN"
{
  "error": {
    "message": "Your authentication token is not from a valid issuer.",
    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_issuer"
  }
</code></pre>
pls help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596076)

push ur image to docker hub that it will be available for them to use<br>
(use chatgpt on how to push to docker hub 2 3 steps to flw)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596077)

yeah i hv pushed the image to dockerhub but i exactly dont get what image name is
like is it the name of my repo

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596078)

ur docker-username/image-name

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596080)

check if u have exported the AIPROXY_TOKEN properly in your environment

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596081)

anyone check my repo<aside class="onebox githubrepo" data-onebox-src="https://github.com/Tusharisme/TDS_Project_1">
  <header class="source">

      <a href="https://github.com/Tusharisme/TDS_Project_1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/f/0f711604313d08011bd1d17317c9e8190f364b1d_2_690x344.png" class="thumbnail" data-dominant-color="EDF0F4">

  <h3><a href="https://github.com/Tusharisme/TDS_Project_1" target="_blank" rel="noopener nofollow ugc">GitHub - Tusharisme/TDS_Project_1</a></h3>

    <span class="github-repo-description">Contribute to Tusharisme/TDS_Project_1 development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596083)

yes i have the same key which is provided on ai proxy website for my login<br>
and yes i have that key properly exported

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596084)

check if u have used the correct ai proxy url then

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596086)

An email I just received says my license doesn’t have “MIT” in it. Although it does have it. I don’t know what I am missing. Someone help (if you didn’t get this mail). <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596088)

<a class="mention" href="/u/carlton">@carlton</a>  <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
Hi,<br>
I received a mail saying that my submission has no Dockerfile. But git repo has a dockerfile.
even if i am to submit again, i have submit the same repo.<br>
what should i do?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596090)

Hey I just got a mail saying that my github repo has no Dockerfile present. and im confused .
It doesnt mention anywhere that the dockerfile must be present in the root directory as a requirement/prerequisite of the project.
In my case its present inside the app directory. Could the team help clarify on this issue.
<a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596091)

What is expected repo structure ?<br>
I have a folder in my repo and dockerfile and license are present in that folder but I still received a mail regarding missing License and Dockerfile.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596092)

do we need to have data folder in repo no right?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596095)

No, it is not needed

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596096)

We see that your submission <a href="https://github.com/22f3001011/project-1/tree/main" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 22f3001011/project-1</a>  has a result of FAIL due to the below reasons:<br>
No “MIT” in LICENSE
Hello sir, i got this mail despite having added the mit license as stated in the project problem statement. I cant figure out what the issue is, and help me out here.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jeeveash.k">@Jeeveash.k</a><aside class="onebox githubfolder" data-onebox-src="https://github.com/22f3001011/project-1/tree/main">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/22f3001011/project-1/tree/main" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/22f3001011/project-1/tree/main" target="_blank" rel="noopener nofollow ugc">GitHub - 22f3001011/project-1</a></h3>

  <a href="https://github.com/22f3001011/project-1/tree/main" target="_blank" rel="noopener nofollow ugc">main</a>

  <span class="label1">Contribute to 22f3001011/project-1 development by creating an account on GitHub.</span>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

Thank you<br>
Regards<br>
Shashank J Shetth<br>
22f3001011

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596097)

Yeah. Same issue. Someone who didn’t get this error, please share the MIT license.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596101)

<a href="https://github.com/saniyanz/tds-p1new" rel="noopener nofollow ugc">https://github.com/saniyanz/tds-p1new</a>
check my repo. what<code>s wrong. I</code>ve also got the mail but I`ve included the MIT License and the Dockerfile

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596104)

Rename <code>LICENSE.txt</code> to <code>LICENSE</code>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596105)

I got a mail saying my Dockerfile is missing. However I have a dockerfile already in my github repository. Is it an issue with the spelling of dockerfile since I have submitted it in all small case as ‘dockerfile’. It was showing the score when I checked with the evaluate.py that was provided by iitm.
Shall I just change the name of the file from ‘dockerfile’ to ‘Dockerfile’ in github repository of mine or is there anything else that is needed to detect the Dockerfile?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596108)

Hey team, I just moved my Dockerfile to the root level on my Github repo. Hope this solves the issue.
Small doubt: Do i need to submit the google form again?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596109)

I ran out of tokens. Please help me. Please its urgent.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596114)

<a class="mention" href="/u/carlton">@carlton</a> sir <a class="mention" href="/u/s.anand">@s.anand</a> sir please provide me more tokens, I am out of tokens i don’t knwo what happened i hade 151 requests use and 0.09 usd and suddenly i check it was 300 requests and 2 usd i don’t knwo what happened can you provide me more tokens.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596117)

Dear <a class="mention" href="/u/s.anand">@s.anand</a> , <a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> , and <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
Thank you all for this wonderful project. Coming from a non-coding background, I have learned a lot new things throughout this project building process.
<a class="mention" href="/u/carlton">@carlton</a> Sir, yesterday’s session provided valuable insights into Method 1 (prompt engineering) for dynamically handling tasks. I was able to develop an application using this approach; however, due to submission time constraints, I could not verify all tasks (my bad). While I tested some tasks and found the results to be highly accurate, I was unable to validate everything thoroughly.<br>
Therefore, I submitted the function-calling approach (Method 2) instead.
I sincerely appreciate everyone’s guidance and support.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596118)

Did you ran out of tokens suddenly like me ?<br>
How many requests have you sent in total ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596120)

can u share ur repo<br>
i really need it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596121)

Thanks <a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a> for this feedback. Glad to know you learned from our efforts, it means a lot. This proves that even a person from non-tech background with determination can achieve it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596129)

sir pls provide more token   <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>  <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/s.anand">@s.anand</a>                              sir pls , give any reply we have only 2 hr left

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596131)

Change the name of your dockerfile to “Dockerfile”

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596132)

yes sir please provide more tokens to me also <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596133)

i hope i get 1 mark xD
im getting tasks only maybe 3 / 10

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596135)

i have done many attempt but it is not working please show  my environment saying fastapi is not installed but i have installed and it is showing on checking but no running file it is saying no module i have installed in both virtual and system<br>
please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596138)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef.png" data-download-href="/uploads/short-url/tKDB9OvCsBntiPn9UaFPfgI5hQX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef_2_690x365.png" alt="image" data-base62-sha1="tKDB9OvCsBntiPn9UaFPfgI5hQX" width="690" height="365" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef_2_690x365.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef_2_1035x547.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/0/d084b074bcf4af69fe3e57753664fd39b016c2ef_2_1380x730.png 2x" data-dominant-color="202121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1016 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
this problem occuring sir since two days

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596140)

How long does it take to make a docker image, I’ve been doing it for the past 25 minutes and it’s still not completed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596141)

<ol>
<li>
Your LLM app should be designed like it can give desire result based on task desc at run endpoint, and that result should be accessible at read endpoint.
</li>
<li>
Evaluation file just for reference to check how things works and it works for phase A tasks only. Also ensure datagen.py file and evaluation.py file are latest. There is one issue in evaluation.py file for task A1,  link of datagen.py file not correct, rectify that link. Even it corrected in GitHub repo file but when I download that raw file in local system it takes back previous link.
</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596144)

I WONDER HOW MANY API REQUESTS THE SERVER IS PROCESSING . It’s too slow

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596146)

too much in the last few hours it feel

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596151)

I guess what is done is done. I should have maintained my version history properly. I am getting 4 correct but with minor formatting issues so only 1 correct I guess.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596161)

It was tough… I will probably not score much but I enjoyed it a lot. Thank you for pushing us so hard. At least I am not scared of docker now and function calling feels easier than before.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596163)

Well done, everyone! This is not an easy project. This is the kind of work our clients are asking us for.
I will keep you posted on the evaluation on this thread, it progresses.
<ul>
<li><span class="discourse-local-date" data-date="2025-02-17" data-email-preview="2025-02-16T18:31:00Z UTC" data-time="00:01:00" data-timezone="Asia/Calcutta">2025-02-16T18:31:00Z</span> Google Form closed</li>
<li><span class="discourse-local-date" data-date="2025-02-17" data-email-preview="2025-02-16T18:35:00Z UTC" data-time="00:05:00" data-timezone="Asia/Calcutta">2025-02-16T18:35:00Z</span> Validating submissions. Will post results shortly</li>
</ul>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596166)

Sir i have missed the submission deadline  by 5  minutes, can you give permission for the google form to accept the response for half an hour more.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596168)

Sir, due to time panic, I mistakenly named the Docker image incorrectly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596169)

Sir can you please allow submission for 5 more minutes?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596170)

A post was merged into an existing topic: <a href="/t/project-1-casual-banter/167344/13">Project 1 - Casual banter</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596988)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Dear Sir,
I am writing to you in a state of distress and humility. An unfortunate mistake on my part has led to the upload of an incorrect Docker image link. When I checked the authenticity of the link, it showed an error, even though the GitHub repository link is functioning perfectly.
I have poured my heart and soul into this project, dedicating countless hours and sleepless nights to ensure its success. The project has successfully passed both Test A and Test B, and I was thrilled to see my hard work paying off. However, this single error has left me devastated.
I am pleading with you, with all my heart, to allow me to correct this mistake by updating the Docker image link. Alternatively, I humbly request that my application be reviewed directly through GitHub. Please consider this an exception, as I have worked tirelessly over the past two weeks to create an application that is 890 lines long.
I beg for your understanding and leniency in this matter. This project means the world to me, and I am genuinely sobbing over this setback.
Thank you for considering my heartfelt request.
Sincerely,
Rishit Jain<br>
(24F2004595)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596172)

Although couldn’t complete handling every task, but really enjoyed working on this project and learned a lot throughout the process. I appreciate the opportunity to work on such an engaging project. For Project 2, I’ll make sure to allocate sufficient time and approach it with even greater commitment.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596174)

Sorry <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
<h3>Sir, due to time panic, I mistakenly named the Docker image incorrectly.</h3>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596175)

Just push the latest image to docker asap. Hopefully the team considers it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596179)

True. Same here. Just giving 2 days for this project was definitely a big mistake on my part… but I couldn’t really give more time due to work commitments.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596180)

<a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
Sir, due to time panic, I mistakenly named the Docker image incorrectly.
I am not 100% sure but i guess i used “ii” instead of “i” in “thevixhal/tdsvishal”… is there any way to check this ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596182)

Can the submissions open just for some time? In minutes?<br>
Many students did silly mistakes due toh nervousness, we can just correct it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596183)

I don’t think the project is too difficult to implement—it’s essentially a simple HTTP API for an AI agent that reads a task, converts it into parameters, and passes those parameters to specific functions to complete the task. However, the instructions in the project question aren’t very clear. Before the session, I am unable to fully understand the question. It took me almost an entire day just to understand what we need to do.<br>
Sir Could you provide test cases or a sample answer for Phase B?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596203)

<a class="mention" href="/u/s.anand">@s.anand</a><br>
<a class="mention" href="/u/carlton">@carlton</a> sorry to disturb you, project1 deadline is over.<br>
I made a mistake in my project. In my call llm function i set some payload instead of default for open ai api call like max token, temp. , n, stop etc.<br>
Due to this, some tasks may fail especially credit card image task will fail 100%, if possible can i just remove that payload from git hub repository . or you can check this call llm function present in my task_handler.py file of my repository.<br>
I found this issue after deadline. If possible consider this request. I never engaged in a project or course like for this one. I love this project genuinely.
my github repo : <a href="https://github.com/21f3001076/TDS_Project_1" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 21f3001076/TDS_Project_1: This is IITM Data Science TDS Course Project 1 Repository</a><br>
Thankyou<br>
Lakshay<br>
student id: 21f3001076@ds.study.iitm.ac.in

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596221)

Dear <a class="mention" href="/u/s.anand">@s.anand</a>  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> ,<br>
Thank you so much for this wonderful project! We have learned so many things from this experience, especially the power of prompts. The team has put in tremendous effort, extending a few sessions and patiently clearing all our doubts. We truly appreciate the dedication and support
Regards,<br>
Arjun

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596231)

I would like to sincerely thank the course faculty <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> for their support on the project throughout the week. They were so patient in listening to our issues and helping us resolve them, even if the issues were repeated.
I was not able to complete some or maybe many of the tasks but overall, it was a very good learning for me, and I thoroughly enjoyed it.
Thanks very much again for your guidance and support.
Regards,<br>
Swati

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596233)

Thanks for your compliments Swati. It’s always nice to know our efforts paid off.<br>
<em>Happy Learning <img src="https://emoji.discourse-cdn.com/google/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></em>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596296)

I have received a mail that my project has ""No “MIT” in LICENSE;No Dockerfile " which I saw today. My project has MIT licence and Dockerfile was also there… but to reconfirm I pulled my dockerfile from dockerhub to github only . NOw am not sure will that be considered now in my project submission or not. Requesting to kindly consider current state of my project in submission for my project.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596310)

WOMP WOMP should i call a wambulance?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596317)

(post deleted by author)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596319)

<span class="mention">@all</span> those who didn’t submit, its ok EVEN I did NOT submit. Even though i get zero, i am happy with the learning i did. Once again thank you sir <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a> . This a been awesome experience , i haven’t been this alive in forever. Cheers.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596321)

I noticed something quite funny. The project never specified the required tech stack, so one could have done this entirely with JavaScript as well, assuming the necessary libraries are installed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596326)

<a class="mention" href="/u/thevishal">@TheVishal</a><br>
EDIT: Create a new docker image with the mistaken image name , so when they pull image from repo, that image with the wrong name also gets pulled.<br>
what to do
<ul>
<li>push a new image with the mistaken name, so in your repo there will be two images<br><br>
how will this help?</li>
<li>since you are unsure, which image link you posted, you can be sure that even you had a mistake in link, a new image will exist with the wrong name after you push another image</li>
</ul>
<span class="mention">@all</span><br>
use this to update your image even after submission, as now they only validate the images, they do not pull it so you can edit your project and add more functionality if they release the code solutiion
CHEERS<br>
Andrew OUT.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596329)

I didn’t submit the google form, I have made the github repo and docker image for TDS project 1. I, mistakenly, thought that I had submitted the google form but actually it was saved as a draft and closed my laptop. As soon as I realized my mistake, I hit the submit button but this was shown then,<br>
“The form TDS Jan 2025 - Project 1 Submission is no longer accepting responses.”
I apologize for this. I have been working on this project for weeks.<br>
This was my first TDS project. I would highly appreciated, if you could help me.<br>
Thankyou
GitHub repo:<a href="https://github.com/Sagankaur/TDS_project1" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Sagankaur/TDS_project1: LLM-based automation agent</a><br>
Docker : sagandeep/tds_project1

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596332)

Sir, can we get the evaluation script now
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596348)

If I am not wrong you were getting 9/10 in task A when many of us were stuck  and you didn’t submit… unbelievable <img src="https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596368)

Thank you, sir, for giving us this amazing opportunity! Honestly, I learned more in the last week than I did throughout the three modules.
The project was a rollercoaster ride—especially with all the errors that kept popping up—but overall, the experience was incredibly enriching. The amount of knowledge I gained was truly valuable.
A huge thanks to <a class="mention" href="/u/carlton">@Carlton</a>, <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>, and <a class="mention" href="/u/jivraj">@Jivraj</a> sir for their guidance and support. Without the last week’s lectures, the project couldn’t have been completed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596370)

i couldn’t my code space ran out of compute and then it was just lagging before i found out what happened , i just submitted old code repo and the image the we created in week 2 or week1 when had to create docker image for graded assignments<br>
EDIT:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png" data-download-href="/uploads/short-url/qusb7PKn6Irl2dNw3ZkKyEdnhHW.png?dl=1" title="Screenshot 2025-02-16 091101" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png" alt="Screenshot 2025-02-16 091101" data-base62-sha1="qusb7PKn6Irl2dNw3ZkKyEdnhHW" width="690" height="149" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_690x149.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980_2_1035x223.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9a9d315d58f80e3b851da3a0e981365d48de980.png 2x" data-dominant-color="16181F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-16 091101</span><span class="informations">1351×292 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82.png" data-download-href="/uploads/short-url/v7KT6Bv6VbMQ4cwdgqIslIbAfsK.png?dl=1" title="Screenshot 2025-02-17 200414" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82_2_690x103.png" alt="Screenshot 2025-02-17 200414" data-base62-sha1="v7KT6Bv6VbMQ4cwdgqIslIbAfsK" width="690" height="103" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82_2_690x103.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82_2_1035x154.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da23d8a478ff6a79db4af56fef947fd376297d82.png 2x" data-dominant-color="221F24"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-17 200414</span><span class="informations">1338×200 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f.png" data-download-href="/uploads/short-url/rlmwKGVLoqyj7lVVSeCMUJGzMiX.png?dl=1" title="Screenshot 2025-02-17 200525" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f_2_690x168.png" alt="Screenshot 2025-02-17 200525" data-base62-sha1="rlmwKGVLoqyj7lVVSeCMUJGzMiX" width="690" height="168" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f_2_690x168.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f_2_1035x252.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/f/bfa4ea8edf0da66b0bb609f953c06ce7f6bd8e3f.png 2x" data-dominant-color="171A21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-17 200525</span><span class="informations">1312×321 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596381)

Wait we had limits in codespace…I didn’t thought much of it but now that I see… …even mine is not so far from the limit…thanks for reminding…gotta be careful in next project

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596406)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> Is there something like peer-review in the project, I found this in the grading document.
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/2/52e6c1b35b7e4c898f1c0cc4abb3cbbcc66760c0.png" alt="Screenshot 2025-02-18 at 12.58.15 PM" data-base62-sha1="bPnxSnsOAejM5OjTiWG7d4VAveM" width="677" height="28">
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/8/08a834722986d3dccd4bf9fb24640bd842d76d08.png" data-download-href="/uploads/short-url/1eAcdnxqu6vSiSV4a7CHDC9brss.png?dl=1" title="Screenshot 2025-02-18 at 1.00.50 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/8/08a834722986d3dccd4bf9fb24640bd842d76d08.png" alt="Screenshot 2025-02-18 at 1.00.50 PM" data-base62-sha1="1eAcdnxqu6vSiSV4a7CHDC9brss" width="126" height="226"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-18 at 1.00.50 PM</span><span class="informations">126×226 2.02 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596606)

This project is one of the best experiences I had in the entire degree program. I could say this without any hesitation that what I learnt in the past 10 days &gt;&gt; last 3 months.
I really appreciate the idea of open internet type of evaluations, wherein, you implement things without any constraints, learning for the sake of implementing.
Doing this project, I also found many new ideas wherein function calling can be used to solve new problems. I also learned many new things from enthusiastic peers like <a class="mention" href="/u/23f1002382">@23f1002382</a> and also got the chance to help a few.
I thank the entire TDS team - <a class="mention" href="/u/s.anand">@s.anand</a> sir, <a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> for their support throughout this amazing experience.
Regards,<br>
Pradeep Mondal

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596614)

sir using prompt method also i am having the error please provide a step wise solution so then i can make functions accordingly.
<pre><code class="lang-auto">#/// Scirpt
# requires-python = "&gt;=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#     "requests",
# ]
#///

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import requests
import os
import json
from subprocess import run

app = FastAPI()

response_format = {
    "type": "json",
    "json_schema": {
        "name": "taks_runner",
        "schema": {
            "type": "object",
            "required": ["python_dependencies","python_code"],
            "properties": {
                "python_code": {
                    "type": "string",
                    "description": "Python code to perform the task"
                },
                "python_dependencies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "module": {
                                "type": "string",
                                "description": "Name of the python module"
                            }
                        },
                        "required": ["module"],
                        "additionalProperties": False
                    }
            }
        }
    }
}
}

primary_prompt = """
                You are an automated agent, so generate python code that does the specified task.
                Assume that uv and python are pre-installed.
                Assume that code you generate will be executed inside a docker container.
                Inorder to perform any task if some python package is required to install, provide name of those modules. 
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AIPROXY_TOKEN}"
}

@app.get("/")
def home():
    return {"welcome to the task runner"}
@app.post("/run")
def task_runnner(task: str):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    data = {
        "model": "gpt-4o-mini", 
         "messages": [
             {
              "role": "user", 
              "content": task
              },
              {
                "role": "system",
                "content": f"""{primary_prompt}"""
            }
         ],
         "response_format": response_format
    }

    response = requests.post(url=url, headers=headers, json=data)
    r = response.json()

    return r

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c.png" data-download-href="/uploads/short-url/nGMHoGQOqao8rFmV5aSYe2okJXK.png?dl=1" title="Screenshot 2025-02-14 185820" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c_2_655x500.png" alt="Screenshot 2025-02-14 185820" data-base62-sha1="nGMHoGQOqao8rFmV5aSYe2okJXK" width="655" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c_2_655x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c_2_982x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a60823d7458d88b699955503f1e0665b9f4e4a4c_2_1310x1000.png 2x" data-dominant-color="272828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-14 185820</span><span class="informations">1945×1484 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> , <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596662)

<aside class="quote group-ds-students" data-username="Sakshi6479" data-post="638" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png" class="avatar"> Sakshi6479:</div>
<blockquote>
<pre><code class="lang-auto">{
    "type": "json",
    "json_schema": {
        "name": "taks_runner",
        "schema": {
            "type": "object",
            "required": ["python_dependencies","python_code"],
            "properties": {
                "python_code": {
                    "type": "string",
                    "description": "Python code to perform the task"
                },
                "python_dependencies": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "module": {
                                "type": "string",
                                "description": "Name of the python module"
                            }
                        },
                        "required": ["module"],
                        "additionalProperties": False
                    }
            }
        }
    }
}
}
</code></pre>
</blockquote>
</aside>
It clearly says in your error message:
Invalid value: ‘json’
if you look at the “type” key in your response_format variable at the top,
the value cannot be “json”
The error is telling you what the supported values are
‘json_object’, ‘json_schema’, and ‘text’
Since you are defining a schema the correct value should be ‘json_schema’
So therefore you should change
<pre><code class="lang-auto">"type": "json"
</code></pre>
to
<pre><code class="lang-auto">"type": "json_schema"
</code></pre>
If you have trouble constructing Json schemas,<br>
either feed it to gpt and have it correct it (along with your error) or please go over Module 3, in particular
<a href="https://tds.s-anand.net/#/llm-text-extraction" class="onebox" target="_blank" rel="noopener">https://tds.s-anand.net/#/llm-text-extraction</a>
There is a clear example you can use as a template. We use the same one as a template when we do it in the sessions. That way you will make less errors.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/595022)

Thanks <a class="mention" href="/u/21f2000709">@21f2000709</a> for kind words
Tagging Saransh for his efforts to project <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>.
<a class="mention" href="/u/23f1002382">@23f1002382</a> most active student on this post thanks to you too.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596763)

<aside class="quote group-ds-students" data-username="21f2000709" data-post="636" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png" class="avatar"> 21f2000709:</div>
<blockquote>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> Is there something like peer-review in the project, I found this in the grading document.
</blockquote>
</aside>
Anyone having any idea on this?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/596771)

No human peer reviews. The peer will be an LLM that has been given the rubrics and fine tuned.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/598912)

<aside class="quote group-ds-students" data-username="carlton" data-post="643" data-topic="164277">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
The peer will be an LLM that has been given the rubrics and fine tuned.
</blockquote>
</aside>
May the peer give me good marks <img src="https://emoji.discourse-cdn.com/google/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/598921)

<a class="mention" href="/u/carlton">@carlton</a> Would the scores of project 1 be released tomorrow?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/599398)

<a class="mention" href="/u/yogesh1">@Yogesh1</a>
<s>We do not have an ETA on Project 1 scores yet. Might have more clarity soon.</s>
Project 1 scores will be available roughly second week of March.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/599832)

<a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a>
I know this is a late reply, but its not possible for us to consider changes to your project after the deadline for academic integrity purposes.
If we were to allow it, we would have to allow everyone to make changes to their project as well for it to be fair.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/599836)

We will soon provide a complete solution for Project 1 because of its valuable learning.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/599837)

Alright, <a class="mention" href="/u/carlton">@Carlton</a>. No problem at all, and thank you for your response.
I just wanted to bring a small limitation in my project’s LLM function to your attention, which I discovered after submission. It may impact one or two tasks. However, no concerns—this has been a great learning experience.
And if possible, just add one line in your Evaluation LLM prompt: <em>“Give loose marking for effort!”</em>—because, you know, creativity deserves some extra credit! <img src="https://emoji.discourse-cdn.com/google/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/599929)

I am not able to see my project marks please look into the problem

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/606016)

Its not been evaluated yet.
We are still processing them.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/606505)

So will the solution be based on New MCP style or will they use the same function calling?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/607262)

Definitely MCP style. Its the most elegant solution and it works beautifully. As soon as evals are done we will showcase it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/607744)

<a class="mention" href="/u/carlton">@carlton</a> Any ETA on project 1 scores?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/609776)

I would like to request some bonus like 0.5 bonus mark for each day of delay from the original expected date of receiving score for Project 1 (will be life-saving for us and will be an incentive for team to release scores quickly; or request to TAs if you had better ideas for helping us score more in Project 1)! <img src="https://emoji.discourse-cdn.com/google/smiley.png?v=14" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/609976)

Any Updates? Can we expect it to be out before P2 deadline?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/611582)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png" data-download-href="/uploads/short-url/3HoFXyYqbYD2IGHEd2R2HnPbOkR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png" alt="image" data-base62-sha1="3HoFXyYqbYD2IGHEd2R2HnPbOkR" width="412" height="167"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">412×167 4.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png" data-download-href="/uploads/short-url/xKjkSm5LcRMcqZCkcM5M1idqlp1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png" alt="image" data-base62-sha1="xKjkSm5LcRMcqZCkcM5M1idqlp1" width="439" height="204"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">439×204 7.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<em><strong>This docker image has outlived many students’ hopes, dreams and ambitions of passing this course.</strong></em>
<strong>Why is it still not being detected properly on the docker hub?</strong><br>
What in the April Fools is this <img src="https://emoji.discourse-cdn.com/google/unamused_face.png?v=14" title=":unamused_face:" class="emoji" alt=":unamused_face:" loading="lazy" width="20" height="20">
<blockquote>
It hasn’t even been morning yet!
</blockquote>
PS ( <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> ): My P1 submission had passed all the basic sanity checks on 15th February. No breaking modifications to the Github repo nor the DockerHub image have been made since then. There’s something bugged in your scripts. Kindly check.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/614016)

same issue here
i have my git repo public but its saying i don’t have public git repo, also i have dockerfile in my root folder but its also said fail, same for mit license<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be.png" data-download-href="/uploads/short-url/iPty7381OeKUfIPiWsQ5KVy6oY6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be_2_690x373.png" alt="image" data-base62-sha1="iPty7381OeKUfIPiWsQ5KVy6oY6" width="690" height="373" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be_2_690x373.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be_2_1035x559.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/3/83f8c6d4eb6481e3b9089ce75d1665cf312904be_2_1380x746.png 2x" data-dominant-color="14181E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1889×1022 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/614037)

yes sir same problem<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png" data-download-href="/uploads/short-url/8eyfQqJ8vzcH4OKnZONZa6tydHd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png" alt="image" data-base62-sha1="8eyfQqJ8vzcH4OKnZONZa6tydHd" width="690" height="269" data-dominant-color="070906"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×346 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png" data-download-href="/uploads/short-url/r1n9wAbkyVZ6YE3LxAtiumMQsLt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png" alt="image" data-base62-sha1="r1n9wAbkyVZ6YE3LxAtiumMQsLt" width="690" height="372" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_1035x558.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png 2x" data-dominant-color="12171C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×718 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
please check and say sir.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411.png" data-download-href="/uploads/short-url/kpyOJTQ8silacxhloviYc9zXUVH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png" alt="image" data-base62-sha1="kpyOJTQ8silacxhloviYc9zXUVH" width="690" height="387" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_1035x580.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_1380x774.png 2x" data-dominant-color="1E1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1078 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
sir it seems like there was a problem when i pushed this files to the repo but i defenitely did correctly. PLease allow me to add docker file alone with your permission. As you can see i haven’t opened the dockerfile since the last date of project 1. Kindly allow this sir. and i have MiT license in my repo but still showing fail . kindly check that also sir.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/614094)

yes sir same problem<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png" data-download-href="/uploads/short-url/8eyfQqJ8vzcH4OKnZONZa6tydHd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/9/39b684382d117b9388443c38b9f83bad7be3e0ab.png" alt="image" data-base62-sha1="8eyfQqJ8vzcH4OKnZONZa6tydHd" width="690" height="269" data-dominant-color="070906"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×346 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png" data-download-href="/uploads/short-url/r1n9wAbkyVZ6YE3LxAtiumMQsLt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png" alt="image" data-base62-sha1="r1n9wAbkyVZ6YE3LxAtiumMQsLt" width="690" height="372" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_690x372.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f_2_1035x558.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd62713ca6104d0402b6d5a3592551e4e47e520f.png 2x" data-dominant-color="12171C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×718 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
please check and say sir.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411.png" data-download-href="/uploads/short-url/kpyOJTQ8silacxhloviYc9zXUVH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png" alt="image" data-base62-sha1="kpyOJTQ8silacxhloviYc9zXUVH" width="690" height="387" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_690x387.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_1035x580.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/f/8f0f30201aeb3a71b6a2167b9f42246665cf2411_2_1380x774.png 2x" data-dominant-color="1E1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1078 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
sir it seems like there was a problem when i pushed this files to the repo but i defenitely did correctly. PLease allow me to add docker file alone with your permission. As you can see i haven’t opened the dockerfile since the last date of project 1. Kindly allow this sir. and i have MiT license in my repo but still showing fail . kindly check that also sir.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/614097)

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . <a class="mention" href="/u/carlton">@carlton</a> sir . <a href="https://github.com/veershah1231/tds_proj_1" class="inline-onebox" rel="noopener nofollow ugc">GitHub - veershah1231/tds_proj_1: Tds project</a> and i have made them 2 months ago and is not a new commit.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg" data-download-href="/uploads/short-url/iaQhsusUKxcxiJH2300WMPkeWv9.jpeg?dl=1" title="1000105386" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg" alt="1000105386" data-base62-sha1="iaQhsusUKxcxiJH2300WMPkeWv9" width="299" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_448x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_598x1000.jpeg 2x" data-dominant-color="252A29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000105386</span><span class="informations">1072×1787 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/614326)

I came pretty close, but too close(double entendre) to the deadline. Classic ICARUS stuff
0/20 <img src="https://emoji.discourse-cdn.com/google/neutral_face.png?v=14" title=":neutral_face:" class="emoji" alt=":neutral_face:" loading="lazy" width="20" height="20"><img src="https://emoji.discourse-cdn.com/google/ok_hand/2.png?v=14" title=":ok_hand:t2:" class="emoji" alt=":ok_hand:t2:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/project-1-llm-based-automation-agent-discussion-thread-tds-jan-2025/615829)

