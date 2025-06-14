# Post No: 71141
# Tds-official-Project1-discrepencies
**Topic Slug**: tds-official-project1-discrepencies
**Created At**: March 28, 2025 18:34:40

Please post any discrepancies related to project1.
<a class="mention" href="/u/carlton">@carlton</a>
<h2><a name="p-612319-who-were-evaluated-how-did-we-decide-what-to-evaluate-1" class="anchor" href="#p-612319-who-were-evaluated-how-did-we-decide-what-to-evaluate-1"></a>Who were evaluated? How did we decide what to evaluate?</h2>
All the image ids we evaluated were what <em>you</em> submitted to us. This is the list of docker repos that was given to us by <a class="mention" href="/u/s.anand">@s.anand</a> as the official list that met all the pre-requisites of Project 1. Therefore we will only evaluate those on this list who are eligible for evaluation with the repos <em>you</em> gave us.
For clarity. Your docker repo gets a unique id every time it is changed. We will ONLY evaluate the image id which was present at the time of the docker repo being pulled. This acts as a time stamped frozen version of your repo. No other image id will be evaluated.
<h2><a name="p-612319-how-to-fix-bugs-in-our-scripts-2" class="anchor" href="#p-612319-how-to-fix-bugs-in-our-scripts-2"></a>How to fix bugs in our scripts</h2>
Create Pull requests to <a href="https://github.com/Jivraj-18/tds-jan25-project1" rel="noopener nofollow ugc">Jivraj-18/tds-jan25-project1</a> .
<h3><a name="p-612319-docker-image-architecture-issue-report-3" class="anchor" href="#p-612319-docker-image-architecture-issue-report-3"></a><strong>Docker Image Architecture Issue Report</strong></h3>
If your Docker image was run on the wrong architecture, please fill out this form:<br>
<a href="https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing" rel="noopener nofollow ugc">Submit Report</a>
<h2><a name="p-612319-bug-fixes-4" class="anchor" href="#p-612319-bug-fixes-4"></a>Bug fixes</h2>
If you find bugs in our evaluation scripts, you might benefit from more marks because of the bug fix. So it is in your interest to look through our scripts and logs and identify bugs or anomalies. You might just go from 0 to heros.
Kind regards,<br>
TDS Team

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612319)



[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612320)

What is the highest mark anyone has scored? Is it 22/20<br>
<a class="mention" href="/u/carlton">@Carlton</a>?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612327)

How come me and my group used same code but some got 10 some 11 some 12?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612331)

<a class="mention" href="/u/carlton">@carlton</a> Please make clear what the average marks are, what highest marks are, and how the project will be evaulated.
We are very close to the end semester exam, and we are still not clear on assignment and project marks. It is a bit frustrating to plan in such circumstances.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612332)

You have to see the logs for that. We have shared the logs. Everyone was graded by the exact same code, so there is no partiality. Your code did not produce consistent results.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612333)

I have noticed that my image was run on a <code>x86_64</code> architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is <code>ARM</code>. This is why I can see that my docker image never ran properly and threw the <code>exec format error</code>.
This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612334)

My evaluation log file is missing, although I followed all the steps to generate the docker image correctly, it’s showing the server didn’t start for 5 minutes but when I uploaded it, it was working fine. Please help me out sir, I worked hard on the project. I’ll get a zero, but I made the submissions correctly. Some other student also got the “server didn’t start in 5 minutes” but he has an evaluation log file. Please kindly help me out. My roll no. is 22f2001389

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612335)

We will check and rerun on arm if we ran it on the wrong emulation.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612336)

Any suggestions for my case sir ? I’m really tensed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612338)

<aside class="quote group-ds-students" data-username="22f3002933" data-post="7" data-topic="171141" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png" class="avatar"> 22f3002933:</div>
<blockquote>
I have noticed that my image was run on a <code>x86_64</code> architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is <code>ARM</code>. This is why I can see that my docker image never ran properly and threw the <code>exec format error</code>.
This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.
</blockquote>
</aside>
<a class="mention" href="/u/carlton">@carlton</a>  same issue, My image was also run on a <code>x86_64</code> architecture. I too built on my mac which is <code>ARM</code> (M1 Processor). I too can see that my docker image never ran properly and threw the <code>exec format error</code>  and  <strong>Evaluation log file</strong> is MISSING.
Actually my image was run on x86_64 architecture as it was present in that log file and because of the wrong architecture it never started.
I also request that my evaluation be done again on the right machine.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d.png" data-download-href="/uploads/short-url/1D9GWomxCCPhEXmDHFBTtjBrktv.png?dl=1" title="Screenshot 2025-03-29 at 12.51.59 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png" alt="Screenshot 2025-03-29 at 12.51.59 AM" data-base62-sha1="1D9GWomxCCPhEXmDHFBTtjBrktv" width="690" height="77" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_1035x115.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_1380x154.png 2x" data-dominant-color="14181E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 12.51.59 AM</span><span class="informations">1613×182 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Even just now I tried running the exact image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png" data-download-href="/uploads/short-url/aEKJ3xEMEb2zZOOQ8zF6qW7COTU.png?dl=1" title="Screenshot 2025-03-29 at 12.53.35 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png" alt="Screenshot 2025-03-29 at 12.53.35 AM" data-base62-sha1="aEKJ3xEMEb2zZOOQ8zF6qW7COTU" width="690" height="95" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_1035x142.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png 2x" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 12.53.35 AM</span><span class="informations">1220×169 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
It is running fine on my macbook air m1 (ARM)
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612339)

<aside class="quote group-ds-students" data-username="22f2001389" data-post="8" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001389/48/12849_2.png" class="avatar"> 22f2001389:</div>
<blockquote>
uploaded
</blockquote>
</aside>
Facing the same issue sir, kindly look into it. I had made sure all the files including the docker file were working perfectly fine. Please help me out.<br>
Roll no. 23f1002056

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612341)

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly. I request for re evaluation of my project. my roll no is 22f1000703

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612342)

Respected,
I haven’t received any mail yet regarding the TDS Project 1 marks.<br>
Please look into it.
Regards,<br>
Soham

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612343)

My evaluation log file is missing.<br>
The 2 other log files i’m given doesnt have my email inside it listed.<br>
the Image id which is given in the MAIL is not present in my docker desktop, my project’s docker image is listed in docker desktop, which doesnot matches the image id given in the MAIL,<br>
What was evaluated? How it was evaluated?
This is the id of the docker image that was evaluated: 0ade87d1bf07
My terminal shows 2 images as last, with respective image ids. I am not sure which one is the real, so please check with both the ids.<br>
tds-project-1              latest    c854274f078d   5 weeks ago    1.38GB<br>
ayush6871/fastapi-agent    latest    27e8375b0ab1   6 weeks ago    1.66GB
I am requesting to look into this case. I think there has been some mistake somewhere.
21f3001194

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612344)

I have also built the image on Mac and facing the same issue
<code>exec format error</code>
It is running fine on my Macbook Pro M1
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612346)

Sir I have noticed a technical glitch for the docker issue, wherein I mistakenly uploaded the wrong docker image link so kindly please kindly re evaluate it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612347)

Sir I haven’t received any mail regarding this Project1 marks. <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612349)

<a class="mention" href="/u/carlton">@carlton</a> Sir , my Docker image is built on Macbook M1 which as you know uses ARM64 architecture . But evaluated with x86_64 which caused the exec format error due to cross platform compatibility issues . I am kindly requesting you to re-evaluate the project once again .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612350)

This is the id of the docker image that was evaluated: d0f14a872042  , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.
Please, look over it.
Regards,<br>
Harsh Jaiswal<br>
23f1001995

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612351)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
I wanted to kindly request if you could review the bonus additional tasks, as they were not reflected in the evaluation, despite being mentioned in the instructions. Apart from that I understand and accept my score overall, especially since I had hardcoded the folder paths in my prompt for some questions, which I believe led to those failures.
<ul>
<li><strong>Bonus: Additional tasks</strong>. We <em>may</em> pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.<br>
Regards,</li>
</ul>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612352)

Would you mind reviewing the evaluation.log screenshot I have attached? I believe I may deserve marks for Task B6. <a class="mention" href="/u/carlton">@carlton</a>, could you kindly take a look?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png" data-download-href="/uploads/short-url/bhTEWgYwF8mPxpMmqTUo8H2BOwB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png" alt="image" data-base62-sha1="bhTEWgYwF8mPxpMmqTUo8H2BOwB" width="690" height="276" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_1035x414.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_1380x552.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1460×585 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612356)

I am also facing the same Please help my roll no is 21f3001750

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612357)

can you please take a look at this screenshot?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3.png" data-download-href="/uploads/short-url/zQmUvbkImebrxLIxoqBdCe1LVVF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_690x304.png" alt="image" data-base62-sha1="zQmUvbkImebrxLIxoqBdCe1LVVF" width="690" height="304" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_690x304.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_1035x456.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_1380x608.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1451×640 64.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The task was done but the LLM made a mistake. I think this type of mistake was outside our control. <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612358)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Please correct me if I’m wrong, but I noticed that for tasks <strong>B7</strong>, <strong>B8</strong>, and <strong>B10</strong>, the evaluation log does not include any <strong><code>POST</code> or <code>GET</code> request traces</strong>, unlike the other tasks which have clearly recorded request flows, generated code, and outputs. In these three cases, the log shows only the failure message without any indication that the script was executed or that the output file was read.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png" data-download-href="/uploads/short-url/rAPE8z6usRTHkquLBzH81ERRoZU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png" alt="image" data-base62-sha1="rAPE8z6usRTHkquLBzH81ERRoZU" width="690" height="256" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_1035x384.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_1380x512.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2003×745 95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612359)

Same issue with my. I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture (I can see this in the logs shared for x86_server_start.log)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612360)

<a class="mention" href="/u/carlton">@carlton</a> sir i have same issue.<br>
I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612362)

Sir even my evaluation log file is missing and I really don’t know what to do because during submission 8/10 of my A tasks were working. Please look into it sir. This is really going to affect my grade and I remember how hard I tried just to get my A tasks running. Please sir<br>
Role nom 23f2000599<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac.jpeg" data-download-href="/uploads/short-url/qT39rwpei3ylAuEBaKKlto3y2w4.jpeg?dl=1" title="1000472083" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_225x500.jpeg" alt="1000472083" data-base62-sha1="qT39rwpei3ylAuEBaKKlto3y2w4" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_450x1000.jpeg 2x" data-dominant-color="2D2E33"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000472083</span><span class="informations">1080×2400 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612363)

Hi <a class="mention" href="/u/jivraj">@jivraj</a>,
The contents of Expected and Result matches, but still test case’s failed.<br>
Is there formatting check for answer , Isn’t prettier to be done ?<br>
I see that your expected answer isn’t formatted using prettier , am i wrong ?
eg:
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> EXPECTED:<br>
[{‘first_name’: ‘Kevin’, ‘last_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first_name’: ‘Kimberly’, ‘last_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first_name’: ‘Kathleen’, ‘last_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first_name’: ‘Jason’, ‘last_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first_name’: ‘Tami’, ‘last_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first_name’: ‘Brenda’, …
<img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
[<br>
{<br>
“first_name”: “Kevin”,<br>
“last_name”: “Allen”,<br>
“email”: “<a href="mailto:tonya41@example.com">tonya41@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Kimberly”,<br>
“last_name”: “Allison”,<br>
“email”: “<a href="mailto:vmendoza@example.com">vmendoza@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Kathleen”,<br>
“last_name”: “Baldwin”,<br>
“email”: “<a href="mailto:amclean@example.com">amclean@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Jason”,<br>
“last_name”: “Banks”,<br>
“email”: “<a href="mailto:sharptara@example.org">sharptara@example.org</a>”<br>
},<br>
{<br>
“first_name”: “Tami”,<br>
“last_name”: “Bass”,<br>
“email”: “<a href="mailto:kristy61@example.com">kristy61@example.com</a>”<br>
},<br>
{<br>
“first_name”: “Brenda”,<br>
“last_name”: “Bradford”,<br>
“email”: “<a href="mailto:amandakeith@example.com">amandakeith@example.com</a>”<br>
},…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612365)



[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612371)

Hi <span class="mention">@all</span>
We will identify why arm images created a problem and were run using x86 platform.
We will also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.
<aside class="quote group-ds-students" data-username="23f3003302" data-post="31" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3003302/48/67422_2.png" class="avatar"> 23f3003302:</div>
<blockquote>
Hi <a class="mention" href="/u/jivraj">@jivraj</a>,
</blockquote>
</aside>
<a class="mention" href="/u/23f3003302">@23f3003302</a> output from your server’s response is correct, we will update our evaluation script.
<aside class="quote group-ds-students" data-username="23f2004912" data-post="24" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2004912/48/108710_2.png" class="avatar"> 23f2004912:</div>
<blockquote>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png" data-download-href="/uploads/short-url/bhTEWgYwF8mPxpMmqTUo8H2BOwB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png" alt="image" data-base62-sha1="bhTEWgYwF8mPxpMmqTUo8H2BOwB" width="690" height="276" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_1035x414.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_1380x552.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1460×585 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</blockquote>
</aside>
<a class="mention" href="/u/23f2004912">@23f2004912</a> We will discuss internally if we can do something about it, but I can’t assure if you will get marks for it, since output from your server is a bit different.
<aside class="quote group-ds-students quote-modified" data-username="23f1001611" data-post="27" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001611/48/67277_2.png" class="avatar"> 23f1001611:</div>
<blockquote>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png" data-download-href="/uploads/short-url/rAPE8z6usRTHkquLBzH81ERRoZU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png" alt="image" data-base62-sha1="rAPE8z6usRTHkquLBzH81ERRoZU" width="690" height="256" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_1035x384.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_1380x512.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2003×745 95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
image2003×745 95 KB
</blockquote>
</aside>
<a class="mention" href="/u/23f1001611">@23f1001611</a> we will look into it
<aside class="quote group-ds-students" data-username="HarshJaiswal" data-post="21" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/harshjaiswal/48/69560_2.png" class="avatar"> HarshJaiswal:</div>
<blockquote>
This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.
</blockquote>
</aside>
<a class="mention" href="/u/harshjaiswal">@HarshJaiswal</a> I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information  <code>harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB </code>
<a class="mention" href="/u/ayush_singh">@AYUSH_SINGH</a>
<aside class="quote group-ds-students" data-username="AYUSH_SINGH" data-post="16" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png" class="avatar"> AYUSH_SINGH:</div>
<blockquote>
ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB
</blockquote>
</aside>
This was submitted to us through google form, for project1.
<aside class="quote group-ds-students" data-username="AYUSH_SINGH" data-post="16" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png" class="avatar"> AYUSH_SINGH:</div>
<blockquote>
The 2 other log files i’m given doesnt have my email inside it listed.
</blockquote>
</aside>
We are aware about it results for 12 students are not generated, we will look into it, and see what caused those 12 images not to run.
<a class="mention" href="/u/22f1000703">@22f1000703</a>
<aside class="quote group-ds-students" data-username="22f1000703" data-post="14" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f1000703/48/125463_2.png" class="avatar"> 22f1000703:</div>
<blockquote>
My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly.
</blockquote>
</aside>
It would have run at your end but it was supposed to run at anywhere, after dockerising it didn’t run, reason is taskA module was not found.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612372)

Same issue for me sir. When I evaluated my file using evaluate.py my 9 cases out of the 10 in Task A was passed but the email I received shows that my evaluation log file is missing. I don’t understand why does it show like that. Please do check and help me out sir.
Reg no. 24f1002633

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612379)

I suspect there is something wrong with how the evaluation has been done. Although A1 task succeeded, all of my A tasks failed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612382)

I have checked my log file in all of the cases where a file is required it says file not found or directory not found error in the code, how can I check /data folder was provided to the program?
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612387)

<a class="mention" href="/u/jivraj">@Jivraj</a> , <a class="mention" href="/u/carlton">@carlton</a><br>
It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the <code>os</code> library. As a result, all file evaluations returned errors such as “can’t read the file.”
I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076.png" data-download-href="/uploads/short-url/oJVfpgHJTo53TpCxytaHv96KM6O.png?dl=1" title="Screenshot (177)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_690x388.png" alt="Screenshot (177)" data-base62-sha1="oJVfpgHJTo53TpCxytaHv96KM6O" width="690" height="388" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_690x388.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_1035x582.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_1380x776.png 2x" data-dominant-color="BBBBBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (177)</span><span class="informations">1920×1080 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/7/078748473287587894e2c880e392cb511618d1f2.png" data-download-href="/uploads/short-url/14BbmQkfIVUg0JdjR6HlE90whq2.png?dl=1" title="Screenshot (179)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_690x388.png" alt="Screenshot (179)" data-base62-sha1="14BbmQkfIVUg0JdjR6HlE90whq2" width="690" height="388" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_690x388.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_1035x582.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_1380x776.png 2x" data-dominant-color="1D2228"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (179)</span><span class="informations">1920×1080 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612391)

Same here. I also dis not recieve any mail sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612392)

I noticed that my Docker image was run on an x86_64 architecture (as indicated by my email in the shared logs), whereas I originally built it on my Mac (ARM architecture). Due to this mismatch, the image failed to run properly and resulted in an exec format error.
Since there was no prior mention of the architecture on which our images would be evaluated, I request that my evaluation be conducted again on the appropriate machine. Please help as after doing it correctly getting 0 marks because of such an error feels wrong

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612407)

<a class="mention" href="/u/23f2001975">@23f2001975</a> we had to rely on docker telling us whether an image was arm or x86. So thats why we just did what docker software told us. If it classified an image as arm then we ran it on arm. If it did not then we ran it on x86. Thats why we need students to look through the logs and identify issues so that we can make sure you get the correct evaluation.
If students notify us their image is actually arm based, then we will run it on arm. So dont worry, just inform us of any discrepancy as well as bugs. Our evaluation might not be perfect, there may be bugs. If students can precisely create bug reports then we can take that into consideration when evaluating students as well. The benefit being you might get extra marks because of the bug fix.
We have a script that looks at this discourse post each day and tells us who requires a fresh evaluation. So we will check your image on arm.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612408)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png" data-download-href="/uploads/short-url/xqSaHAFarUTS4I13ycaCKbHTBFc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png" alt="image" data-base62-sha1="xqSaHAFarUTS4I13ycaCKbHTBFc" width="633" height="197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×197 4.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This is a screenshot of my docker log file. This works if you pass the actual value of the airproxy token at the command line while pulling the docker image. Please do look into this as I’ve put a lot of effort into this.
Thank you
Regards,<br>
23f3002677

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612410)

<span class="mention">@cartlon</span> Same issue.
My image was also run on a <code>x86_64</code> architecture. I too built on my mac which is <code>ARM</code> (M1 Processor). I too can see that my docker image never ran properly and threw the <code>exec format error</code> and <strong>Evaluation log file</strong> is MISSING.
Can you please rerun the image on ARM based

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612411)

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png" data-download-href="/uploads/short-url/cQ8bgXIjD37N3gxBAEHvJ8iStNL.png?dl=1" title="image"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png" alt="image" data-base62-sha1="cQ8bgXIjD37N3gxBAEHvJ8iStNL" width="633" height="197"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×197 5.21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612412)

You have to identify the exact bug for your claim to be considered. Thats why we have provided you with the scripts and the logs. You might get lots of marks. Its in your interest to identify the bug.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612413)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> what do I do sir am seriously clueless and heartbroken rn pls help atleast for A tasks we should get it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612416)

We demoed in the live session the complete process of how to dockerise your project so that it can be run anywhere. Running on your local machine is not a sufficient criteria for passing the evaluation. It is absolutely vital for students to understand deployment. This is a critical skill for anyone who is serious about working in this field.
Also just check if yours is an arm based image or x86. Sometimes that makes a difference. For us there is no way to know other than docker software telling us. As it turns out several students had an arm based image but docker did not tell us that. So we will re run those.
If yours has been run on the wrong emulation then we will re run.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612417)

<a class="mention" href="/u/carlton">@carlton</a>
I encountered an HTTP 500 error with the following detail:
<pre><code class="lang-auto">{
"detail": "'choices'"
}
</code></pre>
This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY_TOKEN. Could you please look into this?
Additionally, my solution is very similar to the one shared by the System Commands team in their email.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png" data-download-href="/uploads/short-url/3dAmgzuVyjwlNrp6pmYrmadLbHH.png?dl=1" title="Screenshot 2025-03-29 103327" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png" alt="Screenshot 2025-03-29 103327" data-base62-sha1="3dAmgzuVyjwlNrp6pmYrmadLbHH" width="690" height="342" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 103327</span><span class="informations">1511×749 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612418)

We have given you the evaluation scripts. Identify where exactly you believe the bug is.
Just guesses is not going to get you extra marks. You have to give us something specific.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612419)

<a class="mention" href="/u/jivraj">@Jivraj</a> sir please kindly look into it. Please re-evaluate my image, everything was working fine it is an issue with the docker image. Please re-evaluate it sir and please guide me as what to do

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612424)

I encountered the same issue with <code>evaluate.py</code>. However, since you previously advised against coding strictly with <code>evaluate.py</code>, I didn’t pursue it further. Now, I’m concerned—how is this a mistake?
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png" data-download-href="/uploads/short-url/9Mog0nVzFPLg21siivqYUrUFaqZ.png?dl=1" title="Screenshot (56)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png" alt="Screenshot (56)" data-base62-sha1="9Mog0nVzFPLg21siivqYUrUFaqZ" width="690" height="167" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (56)</span><span class="informations">1492×362 22.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612427)

Please provide more time for this. Right now, we are also busy with the second project. There are other courses as well.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612434)

yaa same issue i am also facing ,<br>
and this LLM thing is very new for us , and we tried our best to complete. , but because of local machine issue , or anything , people end up getting 0 marks , or 4-5 marks , ..<br>
As a lot of students are getting 0 , so please give some bonus , or some marking for there efforts ,<br>
TDS dont have quiz , ,and getting 0 in project will decrease our CGPA too .<br>
please think for it sir <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612440)

This is the id of the docker image that was evaluated: 468630ef32b8<br>
I believe this is not my docker ID that was submitted, my docker ID is “bd2d0e570ec6”:
proof:<br>
REPOSITORY                           TAG          DIGEST                                                                    IMAGE ID       CREATED        SIZE<br>
rohit23f1001156/project1_tds         v3           sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542   bd2d0e570ec6   5 weeks ago    816MB
Please, look over it.
Also, in my docker log file, it is showing the error as:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69.png" data-download-href="/uploads/short-url/ldBEby0LkRjZoaTLvE4vhz7dhA5.png?dl=1" title="Screenshot 2025-03-29 at 11.10.03 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_690x462.png" alt="Screenshot 2025-03-29 at 11.10.03 AM" data-base62-sha1="ldBEby0LkRjZoaTLvE4vhz7dhA5" width="690" height="462" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_690x462.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_1035x693.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_1380x924.png 2x" data-dominant-color="F3F2F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 11.10.03 AM</span><span class="informations">2360×1582 503 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
what is the reason for this?<br>
It was running properly before, please help.
Regards,<br>
Rohit<br>
23f1001156
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612441)

<a class="mention" href="/u/rohit_b_lakshmanan">@ROHIT_B_LAKSHMANAN</a>
This is <strong>exactly</strong> what <strong>you</strong> submitted. We will ONLY consider this as valid.
2/16/2025 9:30:05	23f1001156@ds.study.iitm.ac.in	<a href="https://github.com/Rohit23f1001156/project1_tds" class="inline-onebox">GitHub - Rohit23f1001156/project1_tds</a>	rohit23f1001156/project1_tds

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612444)

Yes, I agree.<br>
So, did my docker ID change when I submitted?<br>
I am sorry sir, but I did not make any changes after submitting the project, so I guess my Docker ID should remain the same as before, if I am not mistaken. I kindly request you to check just once more please, as I really don’t know where I have went wrong.
Jivraj Sir had checked liked this for another student, so I just wanted to confirm the same for me.<br>
<em>" I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information <code>harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB </code>"</em>
Also sir, could you please tell me why the error as shown in my previous message is being shown? and if there is no chance of it getting correct.
thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612454)

Hi <a class="mention" href="/u/carlton">@carlton</a> !
I am reaching out with deep frustration and concern regarding the evaluation of my project. I have worked tirelessly on this for almost two weeks, dedicating day and night to ensure that the tasks were executed correctly. During my own testing, I was able to get at least 7 out of 10 A tasks working as expected. However, after the evaluation, I was informed that none of the tasks were executed properly, which was quite shocking!
Given the effort and time I have put in, I kindly request you to review my project once more. I am more than willing to demonstrate the functionality in real time to clarify any issues or misunderstandings. Please let me know if there is a possibility to discuss this further, as I genuinely believe my work deserves another review.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612462)

<a class="mention" href="/u/carlton">@carlton</a>,
Jivraj said, <em>“We will discuss internally if we can do something about it.”</em> I understand this well. The output from my server is slightly different, but it still achieves over 95% accuracy. Please do consider it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612463)

Hi <a class="mention" href="/u/pritul_raut">@Pritul_raut</a><br>
No, we won’t reevaluating it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612464)

Hi <a class="mention" href="/u/22f2001389">@22f2001389</a>
<pre data-code-wrap="Traceback"><code class="lang-Traceback">  File "/app/app.py", line 4, in &lt;module&gt;
    from tasksA import *
ModuleNotFoundError: No module named 'tasksA'
</code></pre>
The error occurs because Python cannot find the <code>tasksA</code> module. This is due to the file not existing, not being in the correct directory.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612479)

<aside class="quote group-ds-students" data-username="ROHIT_B_LAKSHMANAN" data-post="54" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png" class="avatar"> ROHIT_B_LAKSHMANAN:</div>
<blockquote>
This is the id of the docker image that was evaluated: 468630ef32b8
</blockquote>
</aside>
We evaluated you on correct file
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png" data-download-href="/uploads/short-url/uI24JOoUGpaMo1DE4B3RCtyoavI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png" alt="image" data-base62-sha1="uI24JOoUGpaMo1DE4B3RCtyoavI" width="690" height="98" data-dominant-color="1D211C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1757×250 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<aside class="quote group-ds-students" data-username="ROHIT_B_LAKSHMANAN" data-post="54" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png" class="avatar"> ROHIT_B_LAKSHMANAN:</div>
<blockquote>
what is the reason for this?<br>
It was running properly before, please help.
</blockquote>
</aside>
Try running docker container after pulling, check if evaluate.py is able to do it’s job.
If you feel there is some issues from our side, we have provided with scirpts we used. You can create a pull request to <a href="https://github.com/Jivraj-18/tds-jan25-project1" rel="noopener nofollow ugc">Jivraj-18/tds-jan25-project1</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612484)

I’m facing “exec /usr/local/bin/uvicorn: exec format error” ,  My roll number is 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612488)

I cannot understand why the project marks are marked zero for me ? i have used the same code as usual but the results are not same ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612493)

No no sir, I can send you an SS of my code, it’s very much there sir, the tasksA file, i really don’t know why this happened.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f.jpeg" data-download-href="/uploads/short-url/4V496m6te2DxSAFIVIfmsQkWF3x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_281x500.jpeg" alt="image" data-base62-sha1="4V496m6te2DxSAFIVIfmsQkWF3x" width="281" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_281x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_421x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_562x1000.jpeg 2x" data-dominant-color="393D3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2160×3840 1.92 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612494)

Same issue with me also

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612499)

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.<br>
Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.
<pre><code class="lang-auto">FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612500)

<a class="mention" href="/u/carlton">@carlton</a> good afternoon sir,<br>
I completed my project 1 and submitted it as instructed. But the result show that evaluate file missing. I did everything right but don’t know how this as the result come. I also had evaluation file in my project too. Please go through things again as this is very unfair for those who took 2 weeks to do this project. My roll no. is 22f3001664. I hope I will get marks, of not full then should be 10/20.<br>
Thank you sir

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612503)

What to do now sir ? Is there no way to fix this now ? I can change the docker file and overwrite the docker image if you allow me to do so.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612506)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg" data-download-href="/uploads/short-url/2nn1zIAthBLXkd1lj0DKNcL1Jy7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg" alt="image" data-base62-sha1="2nn1zIAthBLXkd1lj0DKNcL1Jy7" width="474" height="474"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">474×474 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612512)

Figure out the problem in our script and do a pull request to it, we will fix it if it’s a valid bug.
<aside class="quote group-ds-students" data-username="Jivraj" data-post="1" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar"> Jivraj:</div>
<blockquote>
Create Pull requests to <a href="https://github.com/Jivraj-18/tds-jan25-project1" rel="noopener nofollow ugc">Jivraj-18/tds-jan25-project1</a> .
</blockquote>
</aside>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612517)

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.
Line number 81 of your app.py
<code>subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)</code>
which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612520)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>
I’m writing here to express my concerns regarding the evaluation of my TDS Project-1. Also, kindly pardon me for the long message.
I have received a MISSING statement in my evaluation log file in the project 1 score mail that was released yesterday.
These are the detailed point wise concerns :
<ol>
<li>
I at the earlier stages, found the Tools in Data Science course relatively challenging as it’s just my second term in Diploma and I have only completed BDM and MLF Course till now. Hence, I decided to drop the course in February, however when I could still view the course on the portal, and raised concerns, the assistance provided to me was very grim and low, and after numerous follow-ups, I was finally informed 2½ weeks after dropping my course, that my drop application was received in draft and they would not proceed with it, and I had to continue my course.
</li>
<li>
By this time, I had already missed 2 graded assignment deadlines and the project 1 submission was due in the coming 2 days. Not losing my spirit and with whatever I could learn and implement I completed the TDS project 1. However, I accidentally attached the wrong docker image link, and I also raised the issue, but didn’t receive a reply.
</li>
<li>
I understand that it was a fault on my part, but evaluating a student as 0, even though all their functions are right, and they give the required answers, is also wrong since we are expected to provide correct answers, and learn to build the docker image, however, there can be occurrences where a student might make a small mistake like uploading the wrong link, and they must be given a small chance to reprimand them.
</li>
<li>
I also didn’t receive the mail from the TDS Team which they issued for students whose docker image or GitHub link was erroneous, and hence I realised after the deadline that I had uploaded the wrong docker image link.
</li>
</ol>
I have rechecked all my function, and they are all correct, giving a 0 to a student, who worked hard within the limited available time(given the student had dropped the course but the course team didn’t process it) is very unfair.
Kindly provide me a way to either re-upload my project-1 Docker image link, or ask them to provide me marks on the basis of the functions and codes written, whichever is feasible, atleast to encourage the efforts and time put into the project with little knowledge.
I hope you would look into my plight, and take necessary measures.
Thanks and Regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612522)

I haven’t received any mails regarding the tds project 1 please look into my concern<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612523)

Sir please consider a re-evaluation for me, please :’)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612538)

Please consider my situation a peer whos results were exactly same as mine has received 9, then how could I get 1 . 23f1002630 this is my role number please reconsider<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612543)

Few Students including me have not received any mails regarding TDS Project 1. We don’t even know what went wrong or why we didn’t received. Initially I thought that it can be due to some sending error and i will receive little late but even after 14hrs we have not received anything from the team. How are we supposed to check log and see our mistakes when we didn’t even received marks and logs. I request to check into it and provide us our marks and logs.<br>
Thank You.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612544)

I had built the project well on my Mac OS machine. I am very disappointed with the scores. How do i make amends for revaluation as I feel the code ran well for all tasks on my machine. Please give written steps for revaluation.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612573)

Its saying that my evaluation log file is missing, i submitted everything properly. It also says no module named TasksA is found while i got 9/10 marks in the tasksA evaluation script. Kindly look into this, i worked really harrd for this project, <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612574)

<a class="mention" href="/u/22f3000935">@22f3000935</a> <a href="https://hub.docker.com/r/pscoeds24/dataworks-agent" rel="noopener nofollow ugc">Page Not Found | Docker Hub</a>
you submitted this docker url through form response for project1, this repo doesn’t exists on docker.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612576)

<a class="mention" href="/u/jivraj">@Jivraj</a> sir please tell me whats the issue am very confused and worried

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612577)

We are aware about such mistakes and we are looking into it. We will reevaluate those images.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612578)

If evaluation file is missing for anyone, we will reevaluate it once more and send same through email.
Can you fill form for architecture detection.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612579)

Also please , kindly share evaluation log file after execution

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612581)

I did upload all the necessary files but it stil says tasksA is missing, and i am getting zero marks. Kindly help out <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d.png" data-download-href="/uploads/short-url/yeR2mOnkHjHPdYbccO0CFRjlyPP.png?dl=1" title="Screenshot 2025-03-29 141448" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_690x335.png" alt="Screenshot 2025-03-29 141448" data-base62-sha1="yeR2mOnkHjHPdYbccO0CFRjlyPP" width="690" height="335" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_690x335.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_1035x502.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_1380x670.png 2x" data-dominant-color="FAFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 141448</span><span class="informations">1387×674 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612582)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png" data-download-href="/uploads/short-url/5TjaGaQAJ4PO7nlS4AZlyiKBdq4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png" alt="image" data-base62-sha1="5TjaGaQAJ4PO7nlS4AZlyiKBdq4" width="469" height="233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">469×233 8.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
linux/amd64<br>
which form should i fill sir?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612583)

<aside class="quote group-ds-students" data-username="Aditya_Naidu" data-post="62" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/aditya_naidu/48/12438_2.png" class="avatar"> Aditya_Naidu:</div>
<blockquote>
21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> .
</blockquote>
</aside>
please fill the form for collecting architecture, so that we can rerun evals earlier we relied on docker api to tell us which architecture is being used, but it didn’t classify them correctly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612586)

Hi <a class="mention" href="/u/23f2000599">@23f2000599</a> check this out
<aside class="quote group-ds-students" data-username="Jivraj" data-post="1" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar"> Jivraj:</div>
<blockquote>
<h3><strong>Docker Image Architecture Issue Report</strong></h3>
If your Docker image was run on the wrong architecture, please fill out this form:<br>
<a href="https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing" rel="noopener nofollow ugc">Submit Report</a>
</blockquote>
</aside>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612588)

mine is linux/amd64 sir it doesnt come under arm or x86 i think

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612590)

Hi <a class="mention" href="/u/23f2002400">@23f2002400</a>
Check your Dockerfile if it copies tasksA.py file to docker container.<br>
If it does where does it copy, these are possible mistakes. You were expected to test docker images.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612591)

Hi <a class="mention" href="/u/23f2000599">@23f2000599</a>
amd64 is x86

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612592)

Ok sir, will fill the form, thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612594)

One issue file is my app is listening on port 8000. But evaluations being done on 8219 port. so how it will succeed. Please guide what to do.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612596)

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.
Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612599)

There is a mistake in the url I guess check this out I have a fully functional image which was pushed 1 month ago<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da.png" data-download-href="/uploads/short-url/5l2bo7P1lKeo45HJ4CciEHSugiK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da_2_690x382.png" alt="image" data-base62-sha1="5l2bo7P1lKeo45HJ4CciEHSugiK" width="690" height="382" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da_2_690x382.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da_2_1035x573.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da.png 2x" data-dominant-color="171D23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1103×611 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Please check this out
url::<a href="https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general" rel="noopener nofollow ugc">https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612612)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png" data-download-href="/uploads/short-url/g2HlbzZmJzgiPojlLNz4l8Gocqt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png" alt="image" data-base62-sha1="g2HlbzZmJzgiPojlLNz4l8Gocqt" width="690" height="221" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×431 9.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the correct answer, eval script is not considering newlines properly. <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612621)

same with me <img src="https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"> i dont understand how i got 0.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612641)

This is the id of the docker image that was evaluated: 2a8ffa96b140 , but i had never provided this docker image instead my image id is 735a5a477fb2 then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.
Please, look over it <a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> .
Regards,<br>
Atharva Antapurkar<br>
23f1002558

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612646)

Sir, my evaluation log file is missing, even though I followed all the steps to generate the Docker image correctly. The system indicates that the server didn’t start within 5 minutes, but when I uploaded it, everything was working fine. I put in a lot of effort into this project, and I’m worried I might receive a zero despite making the submission correctly. Kindly help me resolve this issue. My roll number is 22F3004068.
Additionally, my Docker image ID was <strong>d2f27c03b878</strong>, but the ID mentioned in the email was <strong>dfac8596cd4c</strong>. Please provide clarity on this discrepancy.
I have also attached my Docker <a href="https://drive.google.com/file/d/1exrdQOCjbrCFux2hC4OQH_BfgiijCzD1/view?usp=drivesdk" rel="noopener nofollow ugc">log file</a> for reference<br>
Docker <a href="https://hub.docker.com/repository/docker/docaravind21/tds-project-1/tags" rel="noopener nofollow ugc">image</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612648)

I realized that I made a mistake in my project by forgetting to uncomment a single line of code: os.path.join(os.getcwd(), “path_given”). I feel really bad about this oversight, especially after working so hard on the project and formatting everything carefully. It was an honest mistake, and I take full responsibility for it.
I sincerely request you to consider re-evaluating my work, as I believe it reflects the effort and dedication I put into it. I truly regret this error and will be more careful in the Project 2
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612655)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png" data-download-href="/uploads/short-url/jRv3cgpzOzFxkgTGnj3fAbSqqEW.png?dl=1" title="Screenshot (423)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png" alt="Screenshot (423)" data-base62-sha1="jRv3cgpzOzFxkgTGnj3fAbSqqEW" width="690" height="415" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (423)</span><span class="informations">1486×895 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Sir so the  user_email isn’t passed while pulling the docker image?
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612663)

Hi Team,
I have resolved the issues and pushed a new Docker image.<br>
<strong>New Docker Image ID:</strong> <code>913320f92eb3</code><br>
<strong>Tag:</strong> <code>latest</code><br>
<strong>OS/ARCH:</strong> <code>linux/amd64</code><br>
Please evaluate my updated submission.
Thanks!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612664)

Hello,
My log file shows a “file not found” or “directory not found” error. Could you confirm whether <code>datagen.py</code> was executed inside the Docker container or on the host OS? If it ran on the host, I don’t see any mounting process for the <code>/data</code> folder into the container. Could you please clarify this?
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612666)

is it like this: FileNotFoundError: [Errno 2] No such file or directory: ‘system_input.txt’ ?<br>
I am getting this error.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612674)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> sir, I have fixed my docker image issue that was causing the error. Please re-pull my docker image so that I can get score. Please consider me for re-evaluation. All the codes were correct, only issue was a glitch in the docker image.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612680)

Hello Sir, I am facing the same issue. Please look into it. Before submission, I ran my Docker file with the evaluation script to ensure it was working, and it worked fine. Kindly help me out. My roll number is 23F3004321.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612700)

Yes, something like that, My log file shows when script tries to access file it says file not found or directory not found.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612702)

Sir, I checked my evaluation log, and the error occurred because the <strong>AI proxy token limit was exceeded</strong>. I ran the evaluation script to verify, and I scored <strong>12/20</strong>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png" data-download-href="/uploads/short-url/gwD7SZY75yucA5CeD6a6hXj3CuA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png" alt="image" data-base62-sha1="gwD7SZY75yucA5CeD6a6hXj3CuA" width="690" height="362" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1456×765 41.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png" data-download-href="/uploads/short-url/l8bjD57G9c5qcDceIuFC3WTZPyi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png" alt="image" data-base62-sha1="l8bjD57G9c5qcDceIuFC3WTZPyi" width="690" height="161" data-dominant-color="080A0F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1094×256 9.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612735)

Sir, my project scored 1/20, with only B1 passed. However, when I ran the evaluation script, I got 6/10 in A tasks. Is there any way this can be checked, as the project works on deployed.<br>
Kind Regards and thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612756)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir,<br>
This is the id of the docker image that was evaluated: 82aeb74ca739  ,<br>
but i had never provided this docker image instead my image id is de8235663462<br>
then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.
Please, look over it <a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> .
Regards,<br>
S Sharmile<br>
23f3001688

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612760)

Sir the evaluated docker file ID was mentioned as  5b28fd5b25a7 in the mail sent by you but my docker file ID is 4d8c0cc34e35. I think my docker file is not evaluated properly. Kindly do check this and help me out. My reg no 24f1002633.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612772)

<a class="mention" href="/u/carlton">@carlton</a><br>
My docker logs shows that <code>OSError: Cannot find resource</code> error occurred when the data generation script tried to access font files in generation for a8.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png" data-download-href="/uploads/short-url/vVy1Zl2FILIE7YmcgLMAd1engpp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png" alt="image" data-base62-sha1="vVy1Zl2FILIE7YmcgLMAd1engpp" width="690" height="374" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1485×807 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png" data-download-href="/uploads/short-url/eQVQww2TLZd4V84EezSUFxCArFA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png" alt="image" data-base62-sha1="eQVQww2TLZd4V84EezSUFxCArFA" width="302" height="252"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">302×252 3.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.
So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .
Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612775)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png" data-download-href="/uploads/short-url/wGBtBjy5Hn6BmqWVgWkMoWH9dX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png" alt="image" data-base62-sha1="wGBtBjy5Hn6BmqWVgWkMoWH9dX" width="690" height="126" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1505×276 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
this is a 429 from sanand which is an error from your side. The evaluation already so delayed now has such issues because of which I am getting 1/20. <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612784)

does that mean our script is not evaluated?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612818)

Hi <a class="mention" href="/u/vihaanv07">@Vihaanv07</a>
This was a good spot, we will rerun all the images where string <code>Agent Errro: 429 Client Error....</code> is present.
Thanks and kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612840)

Hi <a class="mention" href="/u/jayeshbansal">@Jayeshbansal</a>
There were 12 emails for which we didn’t rerun, we will be fair with grading you and will take care of it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612842)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png" data-download-href="/uploads/short-url/lPAoFwQ51S3kK27PvChwTcqAd1b.png?dl=1" title="Screenshot 2025-03-29 at 7.53.20 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png" alt="Screenshot 2025-03-29 at 7.53.20 PM" data-base62-sha1="lPAoFwQ51S3kK27PvChwTcqAd1b" width="690" height="431" data-dominant-color="111111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-29 at 7.53.20 PM</span><span class="informations">1440×900 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My docker image id is different than the one I submitted<br>
“This is the id of the docker image that was evaluated: 10f11a0e0cd6”
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a> plz check this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612854)

Hi <a class="mention" href="/u/23f300327">@23F300327</a>
This is what you submitted to us in the gform.
23f3003027@ds.study.iitm.ac.in	mishkat02/automation-agent:latest
We will only evaluate this image.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612875)

<a class="mention" href="/u/carlton">@carlton</a> then why is the image id different?
in the docker hub as well as my local terminal the image id is 07b16dc68225

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612877)

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.
In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.
But we can detect changes made to the docker repo through our image id. I hope that is clear.
We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612890)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
My logs show,  ‘exec format error’ and it is due to architecture issue,  image was built on mac.
I have updated the google form regarding the architecture. Please rerun my image. Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612935)

<aside class="quote group-ds-students" data-username="Jivraj" data-post="1" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar"> Jivraj:</div>
<blockquote>
<h3><strong>Docker Image Architecture Issue Report</strong></h3>
If your Docker image was run on the wrong architecture, please fill out this form:<br>
<a href="https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing" rel="noopener nofollow ugc">Submit Report</a>
</blockquote>
</aside>
Just fill the google form, we are rerunning such images.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/612956)

Greetings, Sir,
I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between <code>pandas</code> and <code>numpy</code> caused the container to fail. To my surprise, the same versions (<code>pandas==2.0.3</code> and <code>numpy==1.24.3</code>) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.
To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.
I’ve pushed the updated image to Docker Hub (<code>santoshsharma003/tds-project-one-1:latest</code>). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.
Thank you for your assistance!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613139)

Hi <a class="mention" href="/u/carlton">@carlton</a>, I checked my Docker log file now and realised I missed to push a couple of files to the image. Is there anything I could do now? I have all the required files in my Git repo though. Please help.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613141)

Sir in my logs it is showing that there’s cv2 module missing i mightve missed adding that in the requirements. Is there anything you could do to help me please?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613213)

I am also facing the same issue. I tried evaluating the scripts with the evaluation file also. Please rerun and let me know. My Roll No is 21F1002866.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613359)

Hi,
For Tasks A8, A9 &amp; A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.
For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK
<pre><code class="lang-auto">ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

</code></pre>
Similarly for task B2.
<pre><code class="lang-auto">INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK
</code></pre>
For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.
For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?<br>
Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613369)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build
<pre><code class="lang-auto">ARG http_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.&lt;xxx&gt;.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}
</code></pre>
This was required  as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..
So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container  started up without issues..
Checkin url: <a href="https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583" class="inline-onebox" rel="noopener nofollow ugc">Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub</a>
Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well..  didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613592)

I am also with the same situation sir. Please help with this issue. I have submitted everything correctly and it was working fine. Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613688)

Hello Sir,
Greetings,
I have not recieved amy mail regarding my Project 1 Marks, can you please look into it.
Thank you/

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613767)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> please sir could you help me with this issue previously when i ran on my system it was working perfectly fine

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613768)

Hello sir
I noticed that the log mentioned:<br>
“python: can’t open file ‘/app/app/main.py’: [Errno 2] No such file or directory.”
However, my main file was named run.py, which might have caused the issue. Since the code was present, I was given a 0. Would it be possible to run it again or consider partial marks for the submission?
Thank you for your time and consideration. I appreciate your help!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613804)

Even my file saying the same. I got the ‘No module named tasksA’ error whereas at the time of submission it was working perfectly fine. Please kindly look into this issues sir.<br>
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613831)

no taskA.py even though i ran the evalution getting 12 score still no evalution.log<br>
help the students please give them second chance

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613847)

on a side note, to validate and test our docker/podman images on a platform outside of our dev environment we can use <a href="https://labs.play-with-docker.com/" rel="noopener nofollow ugc">https://labs.play-with-docker.com/</a>.. this is a free platform to download run and test docker images …

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613862)

Hi <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?
Thanks for considering, any help would be appreciated. Worked very hard for this

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613878)

The docker id of the image that was evaluated (as specified the mail 1ae3f64427f0) is not correct, the correct id is 51168f246618.
Name of Docker image -<br>
garriimaa/llm_automation:latest<br>
Please evaluate with the above image name.
GitHub repository for reference - <a href="https://github.com/Garima1603/llm_automation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Garima1603/llm_automation</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/613952)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> sir I fixed my issue with docker during the given window for discrepancy and requested a re-pulling of the image but still got a mail of score 0. Please sir, I request you to do a re-evaluation, the docker issue is fixed long back by me. It’s an earnest request sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614001)

Dear sir,  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
I got result as fail for the project 1 and the reasons listed are as in the screenshot. But as you can see in the second screenshot, i still have that repository which is public, have license file and docker file in it, created 2 months back. I actually don’t know how this issues come in, please resolve this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397.jpeg" data-download-href="/uploads/short-url/6mibDRJspDln0P0tPtHV2gZLc4n.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397_2_690x294.jpeg" alt="1" data-base62-sha1="6mibDRJspDln0P0tPtHV2gZLc4n" width="690" height="294" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397_2_690x294.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">885×378 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c.jpeg" data-download-href="/uploads/short-url/sFuQEAX6TU2c9PhcjC2BnDKDPis.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c_2_690x439.jpeg" alt="2" data-base62-sha1="sFuQEAX6TU2c9PhcjC2BnDKDPis" width="690" height="439" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c_2_690x439.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c.jpeg 2x" data-dominant-color="12161D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">908×579 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614002)

<a class="mention" href="/u/carlton">@carlton</a><br>
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:
“Is Dockerfile present in root of GitHub repo?”
Despite this, my dockerfile is present in the root directory of my repository.
Github repo link: <a href="https://github.com/karthiksirimilla/tds_project1_final" rel="noopener nofollow ugc">GitHub - karthiksirimilla/tds_project1_final</a>
My evaluation.log , contains the score 6/20<br>
Roll no : 23f1002398<br>
Mailid: 23f1002398@ds.study.iitm.ac.in
My evaluation.log<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868.jpeg" data-download-href="/uploads/short-url/vfZJp9E32S2QSOkawO36N5d1048.jpeg?dl=1" title="IMG_6418" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_246x500.jpeg" alt="IMG_6418" data-base62-sha1="vfZJp9E32S2QSOkawO36N5d1048" width="246" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_246x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_369x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_492x1000.jpeg 2x" data-dominant-color="151515"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6418</span><span class="informations">1290×2619 566 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614004)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png" data-download-href="/uploads/short-url/1uIRebCprKWS8VSClyptr3riMaG.png?dl=1" title="IMG_6417" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png" alt="IMG_6417" data-base62-sha1="1uIRebCprKWS8VSClyptr3riMaG" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_345x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_460x1000.png 2x" data-dominant-color="2F3033"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6417</span><span class="informations">1290×2796 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614005)

<a class="mention" href="/u/carlton">@carlton</a>  Sir, the image id written in my notification email is wrong. The correct image is this: <a href="https://hub.docker.com/repository/docker/24f1002064/project1/general" rel="noopener nofollow ugc">https://hub.docker.com/repository/docker/24f1002064/project1/general</a>
can you please double check this? You can also verify that I have made no changes to it since the due date.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614007)

<a class="mention" href="/u/carlton">@carlton</a><br>
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:
“Is Dockerfile present in root of GitHub repo?”
Despite this, my dockerfile is present in the root directory of my repository.
Github repo link:  <a href="https://github.com/karthiksirimilla/tds_project1_final" class="inline-onebox" rel="noopener nofollow ugc">GitHub - karthiksirimilla/tds_project1_final</a>
My evaluation.log , contains the score 6/20<br>
Roll no : 23f1002398<br>
Mailid: 23f1002398@ds.study.iitm.ac.in<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png" data-download-href="/uploads/short-url/1uIRebCprKWS8VSClyptr3riMaG.png?dl=1" title="IMG_6417" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png" alt="IMG_6417" data-base62-sha1="1uIRebCprKWS8VSClyptr3riMaG" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_345x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_460x1000.png 2x" data-dominant-color="2F3033"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_6417</span><span class="informations">1290×2796 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614011)

Your dockerfile is misspelt.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614009)

Thanks for your quick response sir. I just wanted to clarify that my dockerfile was recognized by Docker, and my image was successfully built, so it seems that Docker itself didn’t have an issue with the filename.
However, I understand that the evaluation script might be case-sensitive and specifically looking for “Dockerfile” with an uppercase “D”. If that’s the issue, should I rename and push the file again to the repo sir.
Please let me know if that’s the right fix or if I need to do anything else sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614014)

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.
But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614015)

I recently received an email stating that my Docker image is not publicly available, resulting in a failed prerequisite check for the TDS Project 1. However, I have ensured that my Docker image is publicly accessible. Please help.
<a class="mention" href="/u/carlton">@carlton</a>
My Docker image ID is "<strong>99d08f2002fa</strong> ", and it is set to public. I kindly request you to review this issue, as I have worked very hard on this project and would appreciate the opportunity for a fair evaluation.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614017)

can you share the sha?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614019)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
There might be some glitches in the system. Could you kindly verify the process again?
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266.jpeg" data-download-href="/uploads/short-url/inhkCz9MkKtkDK3tKRKZEdZxxdk.jpeg?dl=1" title="1000430602" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_223x500.jpeg" alt="1000430602" data-base62-sha1="inhkCz9MkKtkDK3tKRKZEdZxxdk" width="223" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_223x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_334x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_446x1000.jpeg 2x" data-dominant-color="28272C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000430602</span><span class="informations">1080×2412 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I’ve already received my score in the evaluation log. Additionally, the Docker Hub run logs show no errors, and both the GitHub repo and Docker image are publicly accessible. All the content has been verified and meets the prerequisites.
Let me know if any further action is needed from my end.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614021)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> please kindly re-pull my docker image and re-evaluate my project sir. I fixed the issue long back. Please reply kindly. My roll no is : 22f2001389. I have been trying to get to you for long now. Please kindly help me out. Please reply.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614043)

<a class="mention" href="/u/carlton">@carlton</a><br>
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:
“Is Dockerfile present in root of GitHub repo?”
Despite this, my dockerfile is present in the root directory of my repository.
Github repo link: <a href="https://github.com/Vansh-22f300/project_tds.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Vansh-22f300/project_tds</a>
My evaluation.log , contains the score .<br>
Roll no : 22f3001851<br>
Mail id:22f3001851@ds.study.iitm.ac.in<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389.jpeg" data-download-href="/uploads/short-url/un90N0luaNkJjOgXOEn5pozxIJb.jpeg?dl=1" title="Screenshot_2025-04-01-09-11-54-385_com.android.chrome" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_225x500.jpeg" alt="Screenshot_2025-04-01-09-11-54-385_com.android.chrome" data-base62-sha1="un90N0luaNkJjOgXOEn5pozxIJb" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_450x1000.jpeg 2x" data-dominant-color="13171E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2025-04-01-09-11-54-385_com.android.chrome</span><span class="informations">1080×2400 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614051)

dockerfile is spelling mistake it should be Dockerfile same thing happened to me .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614053)

<a class="mention" href="/u/carlton">@carlton</a>
Pls look into this evaluation.py contains two result<br>
Can u confirm that u guys will use 10/20 one ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608.jpeg" data-download-href="/uploads/short-url/rt4RWLXkL84tt2DQxU3WClYumFi.jpeg?dl=1" title="Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_230x500.jpeg" alt="Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs" data-base62-sha1="rt4RWLXkL84tt2DQxU3WClYumFi" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_230x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_345x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_460x1000.jpeg 2x" data-dominant-color="171717"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs</span><span class="informations">1080×2340 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3.jpeg" data-download-href="/uploads/short-url/znT50jIE99YegW4vR9yWjtcBrQ7.jpeg?dl=1" title="Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_230x500.jpeg" alt="Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs" data-base62-sha1="znT50jIE99YegW4vR9yWjtcBrQ7" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_230x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_345x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_460x1000.jpeg 2x" data-dominant-color="141414"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs</span><span class="informations">1080×2340 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614058)

HELLO SIR , DOCKET IMAGE PRESENT IN DOCKER HUB  AND IT IS PUBLIC THEN WHY IT IS FAIL<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png" data-download-href="/uploads/short-url/gDCCqNTeh9GKxT8mQBZUoKyScfs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png" alt="image" data-base62-sha1="gDCCqNTeh9GKxT8mQBZUoKyScfs" width="619" height="241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">619×241 5.07 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a.png" data-download-href="/uploads/short-url/vKQI0vMHHClcpfJd06nEaO4ELmG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a_2_690x451.png" alt="image" data-base62-sha1="vKQI0vMHHClcpfJd06nEaO4ELmG" width="690" height="451" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a_2_690x451.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a.png 2x" data-dominant-color="141A20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">919×602 28.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_690x37.png" alt="image" data-base62-sha1="ydvrO1fjQgdMqo0a5x65bOoQisL" width="690" height="37" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_690x37.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_1035x55.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_1380x74.png 2x" data-dominant-color="1A222B"><br>
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614062)

same issue i am also facing ,<br>
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614086)

Respected Sir,
I have received a <strong>FAIL</strong> status for the prerequisite check:<br>
<em>“Is Docker image present in Docker Hub AND is public.”</em>
However, as shown in my Docker Hub repository, my Docker images are publicly accessible.
I have attached a screenshot for the reference.
Thank you for your time and support.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830.png" data-download-href="/uploads/short-url/rRayoYIeHU0431yG3fWuiAcvsVG.png?dl=1" title="Screenshot From 2025-04-01 11-17-44" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_690x110.png" alt="Screenshot From 2025-04-01 11-17-44" data-base62-sha1="rRayoYIeHU0431yG3fWuiAcvsVG" width="690" height="110" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_690x110.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_1035x165.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_1380x220.png 2x" data-dominant-color="131920"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot From 2025-04-01 11-17-44</span><span class="informations">1866×300 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614089)

Dear team,
The evaluation shows that the Github repo was not found, however the repository has published and public.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png" data-download-href="/uploads/short-url/cRQspPlKpiRwam8T7Vcbpu5YlhL.png?dl=1" title="2025-04-01_13:10:20" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png" alt="2025-04-01_13:10:20" data-base62-sha1="cRQspPlKpiRwam8T7Vcbpu5YlhL" width="564" height="317"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-04-01_13:10:20</span><span class="informations">564×317 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Github URL <a href="https://github.com/22f3003029/llm_agent" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 22f3003029/llm_agent</a>
Roll Number: 22f3003029
Request your assistance on the issue.
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614123)

Respected Team,<br>
I received an email stating I failed to fulfil prerequisite and scored 0 because of it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png" data-download-href="/uploads/short-url/6ls596muMFXc6CGVVeUMcWQYEP1.png?dl=1" title="Screenshot 2025-04-01 132313" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png" alt="Screenshot 2025-04-01 132313" data-base62-sha1="6ls596muMFXc6CGVVeUMcWQYEP1" width="651" height="276"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 132313</span><span class="informations">651×276 6.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I checked my Docker Hub and there it is showing “Public”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c.png" data-download-href="/uploads/short-url/hEfU6wbscFJINnFVBoMWCuuVoyE.png?dl=1" title="Screenshot 2025-04-01 131944" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_690x57.png" alt="Screenshot 2025-04-01 131944" data-base62-sha1="hEfU6wbscFJINnFVBoMWCuuVoyE" width="690" height="57" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_690x57.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_1035x85.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_1380x114.png 2x" data-dominant-color="161B21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 131944</span><span class="informations">1479×124 7.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Can Anyone explain what I did wrong ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614128)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65.png" data-download-href="/uploads/short-url/5kcw1smiWWAisr8aFhSlEQWSU2p.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65_2_396x500.png" alt="image" data-base62-sha1="5kcw1smiWWAisr8aFhSlEQWSU2p" width="396" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65_2_396x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">593×747 61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac.png" data-download-href="/uploads/short-url/73Q5a0YN2MZgu6hFbEc1yBnD2Bm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_690x335.png" alt="image" data-base62-sha1="73Q5a0YN2MZgu6hFbEc1yBnD2Bm" width="690" height="335" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_690x335.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_1035x502.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_1380x670.png 2x" data-dominant-color="FAFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1525×741 52.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Sir, I have the image in the docker and it is upload last month and it is public. So why have I received a message saying that the image is not available in the hub. Can you confirm and reevaluate the error.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614144)

Hi <a class="mention" href="/u/jayeshbansal">@Jayeshbansal</a> ,
The docker repo name that you submitted through submission form was different than what your screenshot shows. <code>/jayeshbansal/add9a05689d3</code> docker repo doesn’t exists or might not be public, that’s why it failed for you.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19.png" data-download-href="/uploads/short-url/fL78lx1cRlHCV2KzCLiLJv0GA89.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_690x83.png" alt="image" data-base62-sha1="fL78lx1cRlHCV2KzCLiLJv0GA89" width="690" height="83" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_690x83.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_1035x124.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_1380x166.png 2x" data-dominant-color="1A1F26"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1826×222 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614149)

The log file provided to me too contains File not found error for task A. However, running the code on the evaluate.py files gave me results. Could you please look into the datagen part?<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614153)

It is the request to the team,to consider this since it is a problem of just a case letter otherwise the whole hardwork of doing the project will be wasted.<br>
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614156)

Dear instructors, I received the mail today regarding project 1 TDS scores and I have been marked fail because the MIT license is not present. But as can be seen in the screenshot below the MIT license file is present in my GitHub repository. Pls look into this matter.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086.png" data-download-href="/uploads/short-url/tB3aE4RkTmDqa8uC7Ck86pAcMv4.png?dl=1" title="Screenshot 2025-04-01 at 2.45.57 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_690x406.png" alt="Screenshot 2025-04-01 at 2.45.57 PM" data-base62-sha1="tB3aE4RkTmDqa8uC7Ck86pAcMv4" width="690" height="406" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_690x406.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_1035x609.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_1380x812.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 at 2.45.57 PM</span><span class="informations">1776×1046 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614160)

It depends where you tested it running, if it’s running inside a docker container and you feel there is problem with our script then you can debug our code and create a pull request on repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614164)

Hi <a class="mention" href="/u/24ds2000125">@24ds2000125</a>
You didn’t meet the standard naming convention for mit license naming.  Name should be LICENSE(all caps) or LICENSE.md.<br>
check this out.<br>
<a href="https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository" rel="noopener nofollow ugc">Adding a license to a repository - GitHub Docs</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614165)

Hi <a class="mention" href="/u/22f3001851">@22f3001851</a>
Standard naming convention for Dockerfile name was not followed we won’t be able to evaluate it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614167)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png" data-download-href="/uploads/short-url/3HoFXyYqbYD2IGHEd2R2HnPbOkR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png" alt="image" data-base62-sha1="3HoFXyYqbYD2IGHEd2R2HnPbOkR" width="412" height="167"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">412×167 4.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
                    <a href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png" width="439" height="204">
          </a>


My email is 22f3001642@ds.study.iitm.ac.in<br>
<a class="mention" href="/u/jivraj">@Jivraj</a>  Could you please check what’s wrong?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614171)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> any updates for the people like me whose image was run on the wrong architecture - mine was ARM ( was evaluated or ×86 ). I filled the form that was later sent for selecting the architecture.
I haven’t received any mail since then. But found many mails are sent to others in while.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614172)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3.png" data-download-href="/uploads/short-url/3WTyyL0UYr3kDjSEpts5cutfQwX.png?dl=1" title="Screenshot 2025-04-01 at 3.17.14 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_690x486.png" alt="Screenshot 2025-04-01 at 3.17.14 PM" data-base62-sha1="3WTyyL0UYr3kDjSEpts5cutfQwX" width="690" height="486" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_690x486.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_1035x729.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_1380x972.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 at 3.17.14 PM</span><span class="informations">2054×1448 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea.png" data-download-href="/uploads/short-url/wCyRjbKJqbqbnnXopUNDisHFFma.png?dl=1" title="Screenshot 2025-04-01 at 3.19.32 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_690x172.png" alt="Screenshot 2025-04-01 at 3.19.32 PM" data-base62-sha1="wCyRjbKJqbqbnnXopUNDisHFFma" width="690" height="172" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_690x172.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_1035x258.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_1380x344.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 at 3.19.32 PM</span><span class="informations">1894×474 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Sir , I received the mail today regarding project 1 TDS scores and I have been marked fail because my repo is not public , and no docker file , no licence . but they all are present in my repo , and it is public too , , i am attaching the screenshot , you can see that too ,<br>
My email is 23f1000598@ds.study.iitm.ac.in<br>
Could you please check what’s wrong?<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614183)

The task B6 was<br>
<a href="https://quotes.toscrape.com/">https://quotes.toscrape.com/</a> has quotes from famous people.<br>
The .author class has the quote author’s name.<br>
Extract and save all authors from the first page, in order, to /data/b6.json as an array of strings.<br>
E.g. <code>["Douglas Adams", "J.K. Rowling", ...]</code>
The output in your file is not an array of double quoted strings.
Instead it is an array of an json object with the keyword author and values as an array of authors.
These are two different things. Almost there but not quite.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614185)

Hi Course Team,
I have also received an email today saying that my Project1 failed. But few days back I received an email with evaluation log saying I got 8/20. Which one is true?
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc.jpeg" data-download-href="/uploads/short-url/9VsjXkzgu3WEc9ewu0oPFV54Buk.jpeg?dl=1" title="1000112508" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_314x500.jpeg" alt="1000112508" data-base62-sha1="9VsjXkzgu3WEc9ewu0oPFV54Buk" width="314" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_314x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_471x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_628x1000.jpeg 2x" data-dominant-color="E6E8ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000112508</span><span class="informations">1080×1716 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614190)

Can someone from TA team reply to this?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614193)

can somebody tell me how the dockerfile not running in 5 mins is my fault? i had the same requirements.txt as many other people and their file ran in given time while mine did not. what was the need for this, sorry for my harsh words but i’m frustrated, stupid rule?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614252)

For your case there was problem with our script that, we have correct, and your submission have dockerfile, license and repo exisits as well, it will be evaluated.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614261)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png" data-download-href="/uploads/short-url/4ys581fZCiMPGysNGcdlklVUpf7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png" alt="image" data-base62-sha1="4ys581fZCiMPGysNGcdlklVUpf7" width="522" height="190"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">522×190 5.51 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
my dockerfile is available in github, Please look into the issue<br>
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614266)

<a class="mention" href="/u/jivraj">@Jivraj</a>
I also have same issue, can you check this…
<a href="https://github.com/21f3001076/TDS_Project_1" rel="noopener nofollow ugc">Repo link</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301.jpeg" data-download-href="/uploads/short-url/mhIHxSHv8gKxbKuAN8vHwJgEbD.jpeg?dl=1" title="1000431136" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_258x500.jpeg" alt="1000431136" data-base62-sha1="mhIHxSHv8gKxbKuAN8vHwJgEbD" width="258" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_258x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_387x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_516x1000.jpeg 2x" data-dominant-color="1B1F23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000431136</span><span class="informations">1079×2087 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614269)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> My P1 submission successfully passed all the basic sanity checks on February 15th and obtained a satisfactory score in the P1 evaluation, which was disclosed on March 29th. However, I received a communication today, April 1, stating that my Docker image is not present or public on DockerHub. I kindly request the TDS course team to investigate this matter at the earliest and provide a resolution for students encountering similar issues.
This situation is particularly disheartening—<strong>seeing days of effort and dedication to Project 1 reduced to nothing, especially given the already demanding pace of the course.</strong>
I will appreciate your prompt attention to this matter.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614276)

I understand the problem. It may be possible that the image id i gave may be different as i had multiple dockerfile and there is a possibility that i gave the wrong image id due to some confusion. Is it possible for reevaluation. I have worked very hard and I don’t want to lose my marks because of some wrong id misconfusion. I request to check my dockerfile once again and provide the marks accordingly

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614290)

dear <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
Dear Sirs,
I have seen that many others have posted similar issues to mine, and you have responded to some of them. To seek your attention, I am replying to this thread.
Please consider my request as well, as I do not want to lose marks on a project I have worked hard on, while also helping others. I am expecting a timely and positive response from your end.
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614294)

Dear Sir,<br>
I hope you’re doing well. I haven’t received any email regarding the results of Project 1. Could you please check if my result was sent or if there’s any update on this?<br>
I would really appreciate your confirmation.<br>
Mail id - 23f2000798@ds.study.iitm.ac.in

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614302)

<a class="mention" href="/u/carlton">@carlton</a><br>
Respected Sir,<br>
I have submitted my project following all the guidelines and fulfilling all the prerequisites. My docker file is available publicly and it is present in the root directory of github repo, still the mail says that the file is missing and my score is zero. Can you please look into this issue
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png" data-download-href="/uploads/short-url/7iIyskH9R9kGi1qOzu0xcMx25Mm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png" alt="image" data-base62-sha1="7iIyskH9R9kGi1qOzu0xcMx25Mm" width="690" height="201" data-dominant-color="10141A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×334 7.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614304)

Name of your dockerfile doesn’t match the standard’s.<br>
It should be <code>Dockerfile</code>(with D caps).

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614322)

No we are doing another run of evaluations. Results will be sent soon.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614323)

dockerfile name should be Dockerfile as this is the standard they are considering .so it was not evaluated you better change that, if they revaluate it will be passed

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614324)

Your submission have Dockerfile, LICENSE and repo exists as well, we found some problems because of redirects not handled in our script.
Your submission will be evaluated.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614325)

We won’t be considering changes after deadline, our script looks for commits before deadline and fetches latest commits before deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614327)

That’s not possible, anything after deadline is not appreciated.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614328)

We have updated just files names will it be considered??

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614329)

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . <a class="mention" href="/u/carlton">@carlton</a> sir . <a class="mention" href="/u/jivraj">@Jivraj</a> <a href="https://github.com/veershah1231/tds_proj_1" class="inline-onebox" rel="noopener nofollow ugc">GitHub - veershah1231/tds_proj_1: Tds project</a> and i have made them 2 months ago and is not a new commit.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg" data-download-href="/uploads/short-url/iaQhsusUKxcxiJH2300WMPkeWv9.jpeg?dl=1" title="1000105386" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg" alt="1000105386" data-base62-sha1="iaQhsusUKxcxiJH2300WMPkeWv9" width="299" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_448x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_598x1000.jpeg 2x" data-dominant-color="252A29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000105386</span><span class="informations">1072×1787 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614330)

<img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> Did Not Receive Project 1 Score – Need Clarification
<strong>Post Content:</strong>
<blockquote>
<strong>Hello, sir</strong>   <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
I received the evaluation email for my <strong>Project 1 Docker Image</strong> submission, but unlike my friend (who got an email with his score), my email did <strong>not</strong> include my score.
My Docker image ID: <strong>6f446c9b84da</strong>
The email I received only contains logs and attachments, but no information about my actual score. in the mail recieved by my friend the score is clearly mentioned,
I would really appreciate it if you could <strong>clarify my project score</strong> and let me know if it was properly evaluated. If there is any issue, I request a reconsideration of my project evaluation.
Thank you for your help!
<strong>Attachments:</strong>
</blockquote>
but in the email which i recieved i got the below thing , there is no information about the project score
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png" data-download-href="/uploads/short-url/zrJWpyvYs0kFhH1fIh2XCIWkpFd.png?dl=1" title="my email without score" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png" alt="my email without score" data-base62-sha1="zrJWpyvYs0kFhH1fIh2XCIWkpFd" width="690" height="398" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">my email without score</span><span class="informations">1403×811 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
sir could you please clarify about my project score ???<br>
waiting for the response

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614337)

I am also facing the same issue sir please provide proper answer for our query. Please consider to recheck the project once again.<br>
Docker image - 5ff55c499b54<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad.jpeg" data-download-href="/uploads/short-url/6zreCSyS83WmoSFchL5SR1LCK8B.jpeg?dl=1" title="1000161685" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_225x500.jpeg" alt="1000161685" data-base62-sha1="6zreCSyS83WmoSFchL5SR1LCK8B" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_450x1000.jpeg 2x" data-dominant-color="2A2B31"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000161685</span><span class="informations">1080×2400 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<a class="mention" href="/u/carlton">@carlton</a> , <a class="mention" href="/u/jivraj">@Jivraj</a> , <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614338)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Got a email stating that prereq failed stating below..<br>
Is Docker image present in dockerhub AND is public: FAIL
but i can see that image is public as shown below image.. am i missing something..
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09.png" data-download-href="/uploads/short-url/xoDlk983XatraaLwQ7sMZsgKmmd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09_2_690x135.png" alt="image" data-base62-sha1="xoDlk983XatraaLwQ7sMZsgKmmd" width="690" height="135" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09_2_690x135.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09.png 2x" data-dominant-color="FAFAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">902×177 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614343)

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.
<pre><code class="lang-auto">tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) &lt;= DEADLINE
                ),
                (None, 0),
            )

</code></pre>
This is part of our script that does the validation check for docker repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614344)

Sir,
The License file is present in the github repository however i received a mail that said that it was absent.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8.png" data-download-href="/uploads/short-url/nIybIgx7rnz9Qp6cQRDxjlaX65O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8_2_690x405.png" alt="image" data-base62-sha1="nIybIgx7rnz9Qp6cQRDxjlaX65O" width="690" height="405" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8_2_690x405.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8_2_1035x607.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8.png 2x" data-dominant-color="13171D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×673 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png" data-download-href="/uploads/short-url/7q3y5vSuNCEbRkULMI3gUy7P9vF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png" alt="image" data-base62-sha1="7q3y5vSuNCEbRkULMI3gUy7P9vF" width="633" height="336"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×336 7.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.<br>
Can you please look into it. Thankyou!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614349)

<a class="mention" href="/u/jivraj">@Jivraj</a>
Can you also clarify my issue?
My submission meets all the prerequisites according to my Git repository and Docker image. Additionally, I can see the results in the evaluation log.<br>
You can check the details in the images below. Screenshot of mail and repository
Roll no. : 21f3001076
<a href="https://github.com/21f3001076/TDS_Project_1" rel="noopener nofollow ugc">GitHub Repo link</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68.jpeg" data-download-href="/uploads/short-url/y1kV0vEmiom5WjxyEyvDrC348Qw.jpeg?dl=1" title="1000431410" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68_2_690x352.jpeg" alt="1000431410" data-base62-sha1="y1kV0vEmiom5WjxyEyvDrC348Qw" width="690" height="352" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68_2_690x352.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68_2_1035x528.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68.jpeg 2x" data-dominant-color="2F2E32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000431410</span><span class="informations">1080×551 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e.jpeg" data-download-href="/uploads/short-url/lafOzLmuSSKeEmkALLiqMsHU72S.jpeg?dl=1" title="1000431413" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e_2_690x472.jpeg" alt="1000431413" data-base62-sha1="lafOzLmuSSKeEmkALLiqMsHU72S" width="690" height="472" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e_2_690x472.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e_2_1035x708.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e.jpeg 2x" data-dominant-color="2D2C34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000431413</span><span class="informations">1080×740 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe.jpeg" data-download-href="/uploads/short-url/fV4QnuH9MvAmuN27DyG9yqPSOku.jpeg?dl=1" title="1000431415" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_330x500.jpeg" alt="1000431415" data-base62-sha1="fV4QnuH9MvAmuN27DyG9yqPSOku" width="330" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_330x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_495x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_660x1000.jpeg 2x" data-dominant-color="181D21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000431415</span><span class="informations">1079×1630 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614351)

Standard name of dockerfile is Dockerfile that’s why it didn’t pass Dockerfile check

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614352)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
I understand sir Dockerfile name was misspelt sir. Since my Docker image was built and recognized, I didn’t realize this would prevent evaluation.<br>
I worked hard on this project sir, and my Docker image was built successfully. Please consider my submission sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614366)

I  have been trying to resolve all the errors but just noticed that my docker image id associated with the project is “c9dc7fbcf405” , meanwhile the mail I received mentions that some other image id was evaluated.<br>
Can you please look into this matter and evaluate the correct Image ID.<br>
Roll number: 23F1001012
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614367)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@Carlton</a> I completely understand that changes to the Docker image after the deadline cannot be accepted.
<em><strong>However, there are specific cases like mine where the Project 1 submission successfully passed the sanity checks on Feb 15 and received a decent score when the evaluation results were released on Mar 29.</strong></em>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png" data-download-href="/uploads/short-url/m5oZT6ccNhYAMcg96GqKgDnNOWO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png" alt="image" data-base62-sha1="m5oZT6ccNhYAMcg96GqKgDnNOWO" width="690" height="214" data-dominant-color="EEEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×395 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
But here’s the catch:** Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:*
<ul>
<li>Implementing a ReAct-based workflow planning &amp; orchestration agent, inspired by the paper <a href="https://arxiv.org/abs/2210.03629" rel="noopener nofollow ugc">ReAct: Synergizing Reasoning and Acting in Language Models</a>.</li>
<li>Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.</li>
<li>Enhancing Shell-use &amp; Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.</li>
<li>Adding useful API endpoints, including an <strong><code>/api/</code></strong> multipart/form endpoint, alongside the existing <strong><code>/read</code></strong> and <strong><code>/run</code></strong> endpoints from Project 1, plus a <strong><code>/clear</code></strong> endpoint to reset the agent’s conversation memory if the context window gets saturated.</li>
<li><strong>Deploying the entire project on a paid GCP VM Instance with a static IP</strong>, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.</li>
</ul>
All this hard work evolved my project into something far beyond a simple Tool-Calling Agent—it essentially became a ReAct Principles based Computer-Using Agent capable of executing complex, non-linear workflows entirely within a container. And I’m not exaggerating: You could ask it to perform something like <strong>hyperparameter tuning for a Random Forest Classifier, offloading the results locally on a JSON file and displaying its contents</strong>, and it would do that for you—without <strong>ever</strong> declining the request. I like to think of it as a <strong>terminal version of</strong> <a href="https://openai.com/index/computer-using-agent/" rel="noopener nofollow ugc">OpenAI’s Computer-Using Agent</a>.
<hr>
Given all the effort, time, and money that went into this, it’s incredibly discouraging to see my project <strong>naturally fail a sanity check (Docker image digest mismatch) (because of the aforesaid updates)</strong> and not get evaluated as a result. This is not the kind of experience that encourages students to learn, experiment, and innovate.
<h2><a name="p-614374-to-clarify-all-the-updates-mentioned-above-took-place-after-march-29-after-project-1-had-already-been-evaluated-and-results-had-been-handed-out-furthermore-we-were-never-informed-that-a-reevaluation-would-take-place-on-april-1-had-i-known-i-would-have-ensured-that-my-original-submission-remained-unchanged-and-considered-creating-a-duplicate-of-my-docker-image-and-implementing-all-the-aforementioned-enhancements-on-it-1" class="anchor" href="#p-614374-to-clarify-all-the-updates-mentioned-above-took-place-after-march-29-after-project-1-had-already-been-evaluated-and-results-had-been-handed-out-furthermore-we-were-never-informed-that-a-reevaluation-would-take-place-on-april-1-had-i-known-i-would-have-ensured-that-my-original-submission-remained-unchanged-and-considered-creating-a-duplicate-of-my-docker-image-and-implementing-all-the-aforementioned-enhancements-on-it-1"></a>To clarify, <strong>all the updates mentioned above took place after March 29</strong>, <strong>after Project 1 had already been evaluated, and results had been handed out.</strong> Furthermore, we were <strong>never informed</strong> that a reevaluation would take place on April 1. Had I known, I would have ensured that my original submission remained unchanged and considered creating a duplicate of my Docker image and implementing all the aforementioned enhancements on it.</h2>
My only request is that if my <strong>updated P1 submission cannot be evaluated</strong> due to the changes made after March 29 (before the P1 reevaluation on April 1), I would really appreciate it if my <strong>original P1 eval score could be reinstated</strong> instead of receiving a <strong>0</strong>—since it was already evaluated and graded.
Would highly appreciate your prompt support in this regard <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614374)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8.jpeg" data-download-href="/uploads/short-url/1X2YuVK73sp5O87IjN3SvRjvvkY.jpeg?dl=1" title="pro 1" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_225x500.jpeg" alt="pro 1" data-base62-sha1="1X2YuVK73sp5O87IjN3SvRjvvkY" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_450x1000.jpeg 2x" data-dominant-color="302622"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pro 1</span><span class="informations">720×1600 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Actually I got the email as my docker file is not in root git hub repository. But everything thing looks fine and my docker file also runs well.. I want to check my repo again ..sir kindly do my my evaluation again and we have put lot of efforts doing this project 1 . Hope the team evaluated and gives the deserved marks<br>
<a class="mention" href="/u/carlton">@carlton</a><br>
@ TDS TEAM

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614391)

There is no Dockerfile in the root directory of your GitHub repository. The standard naming convention for a Dockerfile is Dockerfile.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614390)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> please let know if any issues in my end on the docker image not present issue.. As explained in earlier thread , the only reason docker image had to be pushed  was the removal my office proxies in the docker image which was making the container not to startup from orchestration environment.. any help is appreciated..

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614402)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>  I updated google form 4 days ago on the architecture, Could you let me know when it will be re-evaluated ? Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614453)

Hi <a class="mention" href="/u/thinkmachine">@thinkmachine</a> <a class="mention" href="/u/22f3002723">@22f3002723</a>
Since you updated docker repo few days ago and docker api doens’t support timestamp based pulling we will pull your GitHub repo before 18 th feb and will build through it and run evaluations.
We also have your docker repo evaluation score, will discuss which one to keep.
This is for anyone who updated their docker repo and there are around 10-20 such cases

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614462)

Thanks for the understanding <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614474)

Hi <a class="mention" href="/u/thinkmachine">@thinkmachine</a><br>
As we said before that changes in Docker image after deadline won’t be accepted. Even an extension of the deadline won’t help in this case, simply because Docker API doesn’t support timestamp based pulling. However we would be pulling your GitHub repositories before 18th Feb build a Docker container and run evaluations on that.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614498)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> request your help in clarification for the same, the Github repo has been always present but it is marking it as fail. Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614499)

A sigh of relief! Thank you so much for the heads up <a class="mention" href="/u/jivraj">@Jivraj</a>.
<a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> Yup! The Docker issue is perfectly understandable. Even I checked my Hub repo, and I couldn’t seem to find an image having the pre-18th Feb digest. Had I been aware of this issue, and the fact that a re-eval would be carried out, I would’ve tagged the updated image differently. Hopefully, cases like mine will aid in resolving any issues in the future.
Once again, thank you both!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614504)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
I am still uncertain as to why I received a second email regarding my project 1 score, indicating a failure due to unmet pre-requisites. I have inquired multiple times, yet I have not received a response. Meanwhile, several other posts, both before and after mine, have been addressed. Kindly clarify about that mail.
Thankyou

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614596)

<a class="mention" href="/u/carlton">@carlton</a>   Sir pls see my issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614604)

I have the same issue. I also received a second mail stating I had failed due to some missing prerequisites though in the first mail my project evaluation had been carried out.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614613)

Hi <a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a>
Dont worry you passed pre-requsites. The script that was used earlier for basic checks used a stricter criteria, the newer one we wrote allowed for a looser check. You have scored very well in your latest run. 12 correct tasks.
We have not responded quickly because we are in the midst of finalising all the scores and doing normalisation etc, i.e operational work for Project 1 and 2.
We hope to have Project 2 scores out by this weekend.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614620)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir can you also see the case of Dockerfile name. Many students have named it dockerfile , lower case ‘d’ character instead of upper case.<br>
Please sir see through it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614623)

Thanks <a class="mention" href="/u/carlton">@carlton</a> , for your response.
I was never worried about the result, whether it comes late or early. I know you will release it once everything is processed correctly. My concern was only about getting a response. Anyway, thanks for replying.
Also, today’s session has been canceled. I wanted to ask about the issue with editing responses in the Project 2 form. Is there any update on this?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614624)

Hi just wanted to know, there was no mail prior stating to keep the Dockerfile in the root folder of the repo (correct me if im wrong). Therefore i have put everything inside a folder - wont this be considered? Please clarify if possible.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268.png" data-download-href="/uploads/short-url/yGLJpNbDtFyR6odAOMjGDE5bwWA.png?dl=1" title="Screenshot 2025-04-02 at 11.41.14 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_690x274.png" alt="Screenshot 2025-04-02 at 11.41.14 PM" data-base62-sha1="yGLJpNbDtFyR6odAOMjGDE5bwWA" width="690" height="274" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_690x274.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_1035x411.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_1380x548.png 2x" data-dominant-color="15191E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-02 at 11.41.14 PM</span><span class="informations">1884×750 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c.png" data-download-href="/uploads/short-url/j4C45mP7RXlVlYJb4gGqAqA8rXC.png?dl=1" title="Screenshot 2025-04-02 at 11.43.17 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_690x224.png" alt="Screenshot 2025-04-02 at 11.43.17 PM" data-base62-sha1="j4C45mP7RXlVlYJb4gGqAqA8rXC" width="690" height="224" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_690x224.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_1035x336.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_1380x448.png 2x" data-dominant-color="13161B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-02 at 11.43.17 PM</span><span class="informations">2290×744 55.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614709)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d.png" data-download-href="/uploads/short-url/v9euyRFlunvnEWfZc7qWgGwUtop.png?dl=1" title="1000004176" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d_2_690x259.png" alt="1000004176" data-base62-sha1="v9euyRFlunvnEWfZc7qWgGwUtop" width="690" height="259" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d_2_690x259.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d_2_1035x388.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d.png 2x" data-dominant-color="141414"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000004176</span><span class="informations">1187×446 55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Can anyone explain what errors of this sort mean?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614711)

You have to show which task triggered this error. Is it all of them or only one of them. Only then we can diagnose what the problem is.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614725)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e.png" data-download-href="/uploads/short-url/f8POUeYUc14WP3S01hUZIrrPUOW.png?dl=1" title="1000004190" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_519x500.png" alt="1000004190" data-base62-sha1="f8POUeYUc14WP3S01hUZIrrPUOW" width="519" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_519x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_778x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_1038x1000.png 2x" data-dominant-color="131313"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000004190</span><span class="informations">1193×1149 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here it is with the task, however the error doesn’t seem to be related to the task itself based on the returned message in the JSON. It seems to be something wrong with the OpenAI API key. From the reading I did, it seems that the key was perhaps not set properly during evaluation? Not completely sure but please look into it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614740)

Did all tasks produce the same error?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614754)

Yes except B1 somehow.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614757)

Hi <a class="mention" href="/u/aryantikam">@AryanTikam</a>
I looked at your github repo, You have used python’s <code>openai</code> module for doing project1, but AIPROXY_TOKEN is supposed to be used through anand sir’s proxy.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614768)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Can you pls tell me my project 1 marks<br>
My evaluation.py had 2 score<br>
First one 1/20 where every task showed error second one had 10/20…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614769)

Dockerfile has to be insider root directory of github repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614770)

This was mistake from our end we rectified it and reevaluated your submission.<br>
Your submission has a good score.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614787)

<a href="https://github.com/swati-iitm/project1_final" rel="noopener nofollow ugc">swati-iitm/project1_final</a>
This is your github repo which doesn’t have a Dockerfile. That’s why It didn’t pass Prechecks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614790)

We have reevaluated it, we have scores avaliable for your submission.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614792)

Sir I understand you will be busy evaluating all the files and reevaluating them as well. I just wanted to know if its a confirm 0 for those who got evaluation log file MISSING and didnt get the other mail that many got in the past 2 days… Just to confirm… cause i think am getting 0 from that <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614796)

So can anything be done about it now as it seems to pass more tasks without the proxy requirement? It is fine if not.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614804)

Please, can you put a screenshot of where it has been communicated, prior to the deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614814)

We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.
We discussed it internally with <a class="mention" href="/u/s.anand">@s.anand</a> and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it <strong>regardless of whether we explicitly mentioned it or not</strong> on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.
In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by <a class="mention" href="/u/s.anand">@s.anand</a>
So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.
Kind regards,<br>
TDS team

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614825)

<a class="mention" href="/u/carlton">@carlton</a> Sir, I would like to respectfully ask if this is some sort of April Fool’s joke, as it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0 Score.
I am not the only one facing this issue; several others have encountered the same problem. I kindly request you to review my submission again.
Additionally, I have faced multiple technical issues in recent times. Initially, I was failed in the L1 viva due to a typing mistake, which was later acknowledged. Similarly, in both OPPE 1 and OPPE 2, many students experienced Google Meet issues. On March 29, during my SC OPPE, I faced camera issues in Google Meet, along with VM lagging. Many students have raised similar concerns with Proctor.
Given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b.png" data-download-href="/uploads/short-url/rAtKM461XD9XoJ6jwMBzL4HpfnB.png?dl=1" title="Screenshot 2025-04-01 020618" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b_2_690x344.png" alt="Screenshot 2025-04-01 020618" data-base62-sha1="rAtKM461XD9XoJ6jwMBzL4HpfnB" width="690" height="344" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b_2_690x344.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b_2_1035x516.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b.png 2x" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 020618</span><span class="informations">1335×667 57.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614834)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg" data-download-href="/uploads/short-url/9cVv4NyVXvwIVWEBlYSIuNPvtiN.jpeg?dl=1" title="IMG_7078" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg" alt="IMG_7078" data-base62-sha1="9cVv4NyVXvwIVWEBlYSIuNPvtiN" width="394" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_591x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_788x1000.jpeg 2x" data-dominant-color="333437"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_7078</span><span class="informations">828×1049 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Same for me sir, i had everything correct still its showing:- Is Docker image present in dockerhub
AND is public: FAIL
I have submitted everything correctly . Please carefully look into this and recheck the project submitted.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614092)

Sir,it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0<br>
<a class="mention" href="/u/carlton">@carlton</a> Sir please look into this.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg" data-download-href="/uploads/short-url/9cVv4NyVXvwIVWEBlYSIuNPvtiN.jpeg?dl=1" title="IMG_7078" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg" alt="IMG_7078" data-base62-sha1="9cVv4NyVXvwIVWEBlYSIuNPvtiN" width="394" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_591x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_788x1000.jpeg 2x" data-dominant-color="333437"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_7078</span><span class="informations">828×1049 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a class="mention" href="/u/carlton">@carlton</a> Sir, given  this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614093)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a.png" data-download-href="/uploads/short-url/rIrFRUWhRQtmzIx5E6g379UXFYC.png?dl=1" title="Screenshot 2025-04-01 at 12.50.38 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_690x439.png" alt="Screenshot 2025-04-01 at 12.50.38 PM" data-base62-sha1="rIrFRUWhRQtmzIx5E6g379UXFYC" width="690" height="439" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_690x439.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_1035x658.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_1380x878.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-01 at 12.50.38 PM</span><span class="informations">2062×1314 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<a class="mention" href="/u/carlton">@carlton</a> sir, i would like to ask why marks showing 0 infact i am submitting all my requirements things in that form so plz look into this matter.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614118)

<a class="mention" href="/u/carlton">@carlton</a> sir, similar thing happened to me as well, I had got the mail that git repo, dockerfile and lisence is not present or accessible while all the prerequisites are completed from my end. Can you please reevaluate my submission.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab711c7e3854b0163bab1970630905785492718.jpeg" data-download-href="/uploads/short-url/xunX3JZhHo3tnY4NZHV2dUWiaUg.jpeg?dl=1" title="1000051556" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_290x500.jpeg" alt="1000051556" data-base62-sha1="xunX3JZhHo3tnY4NZHV2dUWiaUg" width="290" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_290x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_435x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_580x1000.jpeg 2x" data-dominant-color="EAE4E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000051556</span><span class="informations">1238×2131 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614694)

Hi Prashant,
Your prerequisites have passed and your evaluation is 6 tasks have been completed successfully. The email was auto sent because we were doing some checks with an older, stricter script. The newer script passes your evaluation.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614737)

Thanks for the quick reply, i don’t have a convincing argument to counter. Just a suggestion it would have been better if you have explicitly put in the sanity check requirements. Something so obvious to you might not be so for others.<br>
if you are referring to this email even here, it was not explicit. Might have missed it in the gmeet. A mail would have been good.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8.png" data-download-href="/uploads/short-url/oGK7nrhrkpLKwup6YAJn9UiNs8w.png?dl=1" title="Screenshot 2025-04-03 at 12.28.22 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_690x281.png" alt="Screenshot 2025-04-03 at 12.28.22 PM" data-base62-sha1="oGK7nrhrkpLKwup6YAJn9UiNs8w" width="690" height="281" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_690x281.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_1035x421.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_1380x562.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-03 at 12.28.22 PM</span><span class="informations">2236×912 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614838)

I agree with you. It should have been explicitly mentioned in the project page (even if we have mentioned it in live sessions)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614839)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Put some light on this poor soul’s message also ;')

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614842)

my repo has both the dockerfile with correct name (Dockerfile and in the root folder), license and is public. Please look into this . <a class="mention" href="/u/carlton">@carlton</a> sir . <a class="mention" href="/u/jivraj">@Jivraj</a> <a href="https://github.com/veershah1231/tds_proj_1" rel="noopener nofollow ugc">GitHub - veershah1231/tds_proj_1: Tds project</a> and i have made them 2 months ago and is not a new commit.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg" data-download-href="/uploads/short-url/iaQhsusUKxcxiJH2300WMPkeWv9.jpeg?dl=1" title="1000105386" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg" alt="1000105386" data-base62-sha1="iaQhsusUKxcxiJH2300WMPkeWv9" width="299" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_448x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_598x1000.jpeg 2x" data-dominant-color="252A29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000105386</span><span class="informations">1072×1787 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
why is it saying i got 0? please look into it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614862)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@jivraj</a> Sir I received a mail like everyone that my git-hub repository is not public and not MIT licensed. I even filled the g-form correctly while submitting.<br>
But I had fulfilled the above required criteria. Please look into this matter ASAP.<br>
Here is my git repo link : [<a href="https://github.com/23f1001415/llm_aa_tds_project" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 23f1001415/llm_aa_tds_project</a>]. (<a href="https://github.com/23f1001415/llm_" rel="noopener nofollow ugc">https://github.com/23f1001415/llm_</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7.png" data-download-href="/uploads/short-url/ndtNLIGeLGE5lrqS43j1aAch6Wr.png?dl=1" title="Screenshot (390)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_690x388.png" alt="Screenshot (390)" data-base62-sha1="ndtNLIGeLGE5lrqS43j1aAch6Wr" width="690" height="388" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_690x388.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_1035x582.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_1380x776.png 2x" data-dominant-color="DCDADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (390)</span><span class="informations">1920×1080 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e.png" data-download-href="/uploads/short-url/kJRYrGZPuOJKpBriQd6q0xuXUV8.png?dl=1" title="Screenshot (391)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_690x388.png" alt="Screenshot (391)" data-base62-sha1="kJRYrGZPuOJKpBriQd6q0xuXUV8" width="690" height="388" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_690x388.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_1035x582.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_1380x776.png 2x" data-dominant-color="191A20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (391)</span><span class="informations">1920×1080 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
aa_tds_project).<br>
I have attached screenshots for your reference.
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614863)

<a class="mention" href="/u/jivraj">@Jivraj</a> I too had the same issue (image was run on wrong architecture) and filled the gform that was circulated. When should we expect to get our scores?
Thanks<br>
Pradeep Mondal

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614872)

Hi <a class="mention" href="/u/21f2000709">@21f2000709</a>
We have used another approach because of architecture problem, by pulling through latest commit from github before 18th feb. Just checked we have results for you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614874)

Hi <a class="mention" href="/u/23f1001415">@23f1001415</a>
This was a problem from our side and we rechecked and now we score against your submission.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614875)

Hi <a class="mention" href="/u/23f1001524">@23f1001524</a>
This was a problem from our end, we have recitified it your submission was valid.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614876)

Your latest score through pulling from github and building image thorugh dockerfile have higher score than these 2.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614877)

Hi <a class="mention" href="/u/23f2004563">@23f2004563</a>
I checked we have scores against your submission.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614882)

There was some problem with our script, later we correct and your submission was valid, I have just checked and confirm you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614883)

Can u pls share marks :') dying with curiosity

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614887)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05.png" data-download-href="/uploads/short-url/fBvMyl3Z079CHiFhl22LyGjsknj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_690x92.png" alt="image" data-base62-sha1="fBvMyl3Z079CHiFhl22LyGjsknj" width="690" height="92" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_690x92.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_1035x138.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_1380x184.png 2x" data-dominant-color="1A1F26"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1841×248 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This was your submission and we could not locate a docker repo against it.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/2/12102c6f548ec1535363f91201441acbc019a484.png" data-download-href="/uploads/short-url/2zNfglZ6jA6ItUzOzMLVUXP9LMw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_690x336.png" alt="image" data-base62-sha1="2zNfglZ6jA6ItUzOzMLVUXP9LMw" width="690" height="336" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_690x336.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_1035x504.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_1380x672.png 2x" data-dominant-color="154061"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1885×918 92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614888)

Your submission was valid there was some issues with our script for checking. But after building your image after pulling github repo, it didn’t one <code>taskA</code> module was missing.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614890)

If you used openai’s python module then you were needed to pass your own api key, hardcode it in code.
API key that we were sending was only valid through proxy server created by professor anand.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614893)

mail will be sent by either today or tomorrow.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614894)

any idea on this sir?..

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614895)

No we pulled through github and build image on gcloud vm. Anyone with valid submission didn’t receive mail, your submission was valid.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614898)

but my evaluation log file was missing… so that would make it a 0 right..I have accepted my fate that it would be a 0 but just a lil hope <img src="https://emoji.discourse-cdn.com/google/melting_face.png?v=14" title=":melting_face:" class="emoji" alt=":melting_face:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614899)

We reevaluated and found your submission was valid but it was running on a different port, 5000 but it was expected to run on 8000 port.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614900)

oh so… is it going to be considered? like will i get some score other than a 0… am sorry for asking so much

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614901)

No it won’t be considered. It was supposed to be running on 8000 port.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614902)

Ok got it. Thank you so much <img src="https://emoji.discourse-cdn.com/google/cry.png?v=14" title=":cry:" class="emoji" alt=":cry:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614903)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f.png" data-download-href="/uploads/short-url/oe9Wber3XqC0AT3u9HyVjnlWqh9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_690x290.png" alt="image" data-base62-sha1="oe9Wber3XqC0AT3u9HyVjnlWqh9" width="690" height="290" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_690x290.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_1035x435.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_1380x580.png 2x" data-dominant-color="FCFCFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×787 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi sir, my Architecture says amd64, in the google docs I have selected x86, i hope it is correct. Also,  I have used podman to test the pull and its working well. Please let me know if i need to do anything else.
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614905)

We are rebuilding all docker submissions from github commit before 18th of Feb, using your Dockerfile manifest present in the repo.
That way there is no architecture issues.
Its part of our secondary check. And more students have gotten scores in this  check. So dont worry.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614662)

I just checked from my side also, wow a very dumb mistake now costing me a 0…should have read the project document more clearly <img src="https://emoji.discourse-cdn.com/google/cry.png?v=14" title=":cry:" class="emoji" alt=":cry:" loading="lazy" width="20" height="20"> So sorry for asking.
Am assuming no lenient correction can be done for that? like during the evaluation …
podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:5000 $IMAGE_NAME

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614911)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8.png" data-download-href="/uploads/short-url/aTj1rnns5ewnPZe1QS9eAZzC11S.png?dl=1" title="Screenshot 2025-04-03 160336" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8_2_690x466.png" alt="Screenshot 2025-04-03 160336" data-base62-sha1="aTj1rnns5ewnPZe1QS9eAZzC11S" width="690" height="466" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8_2_690x466.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8_2_1035x699.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8.png 2x" data-dominant-color="151B21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-03 160336</span><span class="informations">1373×928 80.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I checked it multiple times before submitting, I got 9/10 in task A.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614918)

No. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614923)

Ok… I do have a doubt tho, i actually have app.py and main.py in my github, my main.py is running on 8000 and app.py on 5000 …

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614927)

but in Dockerfile in your github repo you didn’t run main.py,

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614930)

In your Dockerfile you didn’t copy taskA.py to the container.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614932)

Ouch, ok sir… hopefully project 2 doesnt disappoint <img src="https://emoji.discourse-cdn.com/google/sob.png?v=14" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614934)

It is there in the master branch of the repository. Now, will the previous evaluation mail that we got be considered or this one?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/614958)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
I recently received an email with an evaluation file for Project 1, which included a score. However, in the recent email, I noticed that my score was recorded as zero, despite fulfilling all the prerequisites.<br>
I kindly request a re-evaluation of my project, as I believe this may be an error.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615048)

<a class="mention" href="/u/jivraj">@Jivraj</a><br>
My discrepancy is still not fixed. Please take a look at it

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615061)

<a class="mention" href="/u/jivraj">@Jivraj</a><br>
Hlo, could you please check and let me know how much am I scoring in Project 1 after the latest evaluation?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615070)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Sir,<br>
In the mail that i got about project 1 report. In the log file it was written as TasksA.py file not found in docker, which was the case i observed with many students.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528.png" data-download-href="/uploads/short-url/ltGd9jH4WOl0KbWRMzDWE1C4JCw.png?dl=1" title="Screenshot 2025-04-04 at 10.31.02 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528_2_690x460.png" alt="Screenshot 2025-04-04 at 10.31.02 AM" data-base62-sha1="ltGd9jH4WOl0KbWRMzDWE1C4JCw" width="690" height="460" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528_2_690x460.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528_2_1035x690.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-04 at 10.31.02 AM</span><span class="informations">1358×906 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This is my Github repo:
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e.png" data-download-href="/uploads/short-url/1QdmND2RTCa9GGGlQ6Ppunr9gMS.png?dl=1" title="Screenshot 2025-04-04 at 10.44.24 AM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_690x372.png" alt="Screenshot 2025-04-04 at 10.44.24 AM" data-base62-sha1="1QdmND2RTCa9GGGlQ6Ppunr9gMS" width="690" height="372" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_690x372.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_1035x558.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_1380x744.png 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-04 at 10.44.24 AM</span><span class="informations">3324×1794 497 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I built the image using docker build command in vs code terminal. And pushed it same way to dockerhub using docker push command. How is it possible that the docker container missed the TasksA.py file while building or pushing it?
After getting this mail, I ran the project locally again mutliple times just to check if there was any issues in the code. It was getting 9/10 test cases passed.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615124)

This is a common mistake many, many students made. They created a working application but not a working container.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e.png" data-download-href="/uploads/short-url/zTvhuV9P7svIcyq9FN5wLIOBno.png?dl=1" title="Screenshot 2025-04-04 at 11.13.32 am"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png" alt="Screenshot 2025-04-04 at 11.13.32 am" data-base62-sha1="zTvhuV9P7svIcyq9FN5wLIOBno" width="690" height="493" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_1035x739.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_1380x986.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-04 at 11.13.32 am</span><span class="informations">2116×1512 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
You only copied <code>app.py</code> into your docker image.
How do you expect your application to run without the other files that your repo clearly shows is needed?
Thats why many people are failing this. Hope the image makes this clear.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615131)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e.jpeg" data-download-href="/uploads/short-url/z13Ubyd03fcUA0Wfe6tP2tcsDw2.jpeg?dl=1" title="1000050348" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_230x500.jpeg" alt="1000050348" data-base62-sha1="z13Ubyd03fcUA0Wfe6tP2tcsDw2" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_230x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_345x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_460x1000.jpeg 2x" data-dominant-color="252529"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000050348</span><span class="informations">1080×2340 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d.jpeg" data-download-href="/uploads/short-url/rDoyKZcglIJ0o6SLLgD51BzVqB.jpeg?dl=1" title="1000050349" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_230x500.jpeg" alt="1000050349" data-base62-sha1="rDoyKZcglIJ0o6SLLgD51BzVqB" width="230" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_230x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_345x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_460x1000.jpeg 2x" data-dominant-color="161A20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000050349</span><span class="informations">1080×2340 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am getting license not present at root of github repo but i have the license added could someone please explain why ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615135)

<a class="mention" href="/u/thinkmachine">@thinkmachine</a>
Firstly, you have passed evaluation and got a decent score (on a more lenient script that we used for everyone.) The email was sent by a script that used a more stricter evaluation (which understandably caused some stress). So you can breathe a sigh of relief. <img src="https://emoji.discourse-cdn.com/google/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">
<em>However</em> with regards to your long post…
Let me tell you a true story. I personally know a <em>very</em> experienced senior engineer at a top defense contractor for the US, here is some pearls of wisdom from him.
What you have done is what is called in industry as <strong>gold plating</strong>. Its a cardinal sin in software engineering. NEVER gold plate. ALWAYS build to spec.
In fact its a good reason to fire an engineer. Why?
<ol>
<li>Because it does not deliver what was required,</li>
<li>Wastes valuable time and resources</li>
<li>Increases technical debt (this is actually a huge cost over the expected lifetime of the project!)</li>
<li>Complicates testing</li>
<li>Leads to scope creep</li>
</ol>
His advice to me was simple: NEVER gold plate.
I hope you take this pearl of wisdom in your career. It will help you advance and make you stand out.
For personal hobbies this does not apply. But for a client (including us) if you fail to deliver the minimum spec then we cannot grant you an evaluation (by the way this post is not targetted specifically for you, it just felt like an appropriate place to explain this).
Kindest regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615138)

Hi Sir,<br>
I just realized that I mistakenly submitted the image tag “abhay227/version1” instead of the correct image ID. The correct image ID is <strong>4db729a03f74</strong> , which is part of version1 that is already present and publicly available.<br>
I have worked very hard on this project, and I am concerned that due to this error, my whole effort may be wasted. Unfortunately, I did not receive any notification regarding an invalid submission after I submitted the Project1 form, and I only recently became aware of this mistake. I kindly request you please consider this correct image ID.
Thank you for your understanding and assistance. I look forward to your positive response.<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png" data-download-href="/uploads/short-url/fDipvC3jgzS5ipBufnfHjh2NUC5.png?dl=1" title="Screenshot 2025-04-02 132214" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png" alt="Screenshot 2025-04-02 132214" data-base62-sha1="fDipvC3jgzS5ipBufnfHjh2NUC5" width="690" height="93" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_1035x139.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_1380x186.png 2x" data-dominant-color="131920"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-02 132214</span><span class="informations">1843×250 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615182)

Hi Abhay,
This was a basic error. Unfortunately for basic errors we are not able to relax the requirements. All students were given a clear directive on what the minimum requirements were in order to be evaluated. Failure to follow those clear instructions prevents us from making any exceptions, because then we just have to dump all those requirements for all students and that would not be fair to those that took the care to be careful about their submissions.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615197)

Hi sir, hope you are doing well.<br>
Could you please check and let me know if I have passed the project 1 and if yes then how much am I scoring in Project 1 after the latest evaluation?<br>
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615384)

Thanks for the clarification regarding the evaluation, <a class="mention" href="/u/carlton">@carlton</a>. It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.
Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible <strong>within the scope of the problem statement</strong>.
What began as just another (pun intended) <em>tedious</em> assignment slowly evolved into a hobbyist research project on LLM agents. <img src="https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:" loading="lazy" width="20" height="20">
<em>(…caution: long post ahead <img src="https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20">)</em>
I noticed that <strong>test cases in Project 1 and 2 were highly specific and often overlapping on Python &amp; Shell use</strong>. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the <strong>inherent randomness in LLM-generated payloads</strong>. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.
Some might suggest using <code>temperature=0</code> to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.
<strong>Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers</strong>: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.
At the core of it, it’s all about <strong>how much flexibility vs rigidity</strong> we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.
Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,
<ul>
<li>Reason about the task, understand intent,</li>
<li>Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. <em>design</em> a DAG, where each node can be a python step or a shell step or something else)</li>
<li>Execute those workflows (<em>walk</em> the DAG) observing the feedback at each step and reiterating if needed.</li>
<li>Observe the final result, and repeat if needed.</li>
</ul>
Interestingly, a similar framework was suggested in <a href="https://arxiv.org/abs/2210.03629" rel="noopener nofollow ugc">this ICLR 2022 paper</a>. That was all the validation I needed to know I was stepping in the right direction.
To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of <strong>general-purpose tools</strong>:
<ul>
<li>A REPL executor (for quick calcs)</li>
<li>A Python script runner</li>
<li>A Shell executor</li>
</ul>
With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.
As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training &amp; tuning ML models autonomously, reporting results etc.) — that was <strong>emergent behavior</strong>, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. <em>Frankly, I AM personally very keen about researching stuff!</em>
I am actually very thankful to the TDS course team &amp; <a class="mention" href="/u/s.anand">@s.anand</a> for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. <strong>Food for thought! Really!</strong>
As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.
PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects: <strong>thoughtful use of LLMs in agent design</strong>. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride. <img src="https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:" loading="lazy" width="20" height="20">
<hr>
<strong>TL;DR</strong><br>
My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615386)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>  Sir please Consider this request!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615471)

Hello Sir,
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405.jpeg" data-download-href="/uploads/short-url/LaX1V7OeSTc3OFGFXVHcf2GlSJ.jpeg?dl=1" title="Screenshot_2025-04-05-18-51-43-721_com.google.android.gm" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_225x500.jpeg" alt="Screenshot_2025-04-05-18-51-43-721_com.google.android.gm" data-base62-sha1="LaX1V7OeSTc3OFGFXVHcf2GlSJ" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_450x1000.jpeg 2x" data-dominant-color="23241C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2025-04-05-18-51-43-721_com.google.android.gm</span><span class="informations">1080×2400 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I got this mail regarding my project 1 scores. My github repo is present and public as well as MIT License and Dockerfile  is also present at the root of the repo
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SrishtySnehi/Project_1_tds">
  <header class="source">

      <a href="https://github.com/SrishtySnehi/Project_1_tds" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/9/f93c7a8f75b0e5f3c99be032499e49464d57c7a2_2_690x344.png" class="thumbnail" data-dominant-color="F4F5F6">

  <h3><a href="https://github.com/SrishtySnehi/Project_1_tds" target="_blank" rel="noopener nofollow ugc">GitHub - SrishtySnehi/Project_1_tds</a></h3>

    <span class="github-repo-description">Contribute to SrishtySnehi/Project_1_tds development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615606)

Hi <a class="mention" href="/u/srishty_snehi">@Srishty_Snehi</a>
Your submission is valid, we but it failed while running server, with this error.
taskA module missing
For regenerating this error:
<ol>
<li>Pull github repo(latest commit before 18th Feb)</li>
<li>Build image using Dockerfile of fetched repo</li>
<li>Run that image.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615610)

We are not considering Dockerfile’s with wrong name(anything other than Dockerfile), and wrong location(anything other than root) in github repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615612)

Will I still get a zero?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615614)

Can we expect the results for project 1 and 2 by tomorrow? <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615651)

when can we expect our project 1 result?<br>
<a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615666)

I got my result!! 2/20 so happy its not a 0 thank you for the bonus <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <img src="https://emoji.discourse-cdn.com/google/sob.png?v=14" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20">
Also really great how yall have given the error logs for everyone individually <img src="https://emoji.discourse-cdn.com/google/saluting_face.png?v=14" title=":saluting_face:" class="emoji" alt=":saluting_face:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615984)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> in earlier evaluation of P1 in that my B1 is passed but in this final scores email it is showing as 0 for B1 pls help<br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/04980bbcf7941e08ba08f59e10a384708518a9eb.png" alt="finalB1" data-base62-sha1="EDFktEIUeMCoRlZZvWtvjRGTSr" width="111" height="81"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0.png" data-download-href="/uploads/short-url/bVPNsc87d4pYQAMPAvhdt6ls7Ti.png?dl=1" title="b1passed" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0_2_690x87.png" alt="b1passed" data-base62-sha1="bVPNsc87d4pYQAMPAvhdt6ls7Ti" width="690" height="87" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0_2_690x87.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0_2_1035x130.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b1passed</span><span class="informations">1109×141 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615988)

Request for Clarification on Zero Marks Given – Repository Was Public with All Required Files
Dear <a class="mention" href="/u/carlton">@Carlton</a> sir<br>
I wanted to kindly request a clarification regarding the evaluation of my project submission. I noticed that I have been awarded zero marks, and I’m a bit confused because I had made sure that everything was in place.
<ul>
<li>My GitHub repository was <strong>public</strong> at the time of submission.</li>
<li>I had included the <strong>Dockerfile</strong> as required.</li>
<li>I also added the <strong>MIT License</strong> to the project.</li>
<li>For your reference, I am also attaching a <strong>snapshot</strong> of the repository as it was during the submission time.</li>
</ul>
Given all these were in place, I would really appreciate it if you could provide a <strong>concrete reason</strong> for giving <strong>zero marks</strong>. I’m eager to understand what went wrong so I can avoid it in the future and improve myself. But u saying in email that my repo was not public , not having dockerfile and not having mit licsence .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437.png" data-download-href="/uploads/short-url/kihBOn21R8PtVRLgXOmmQh1HkX5.png?dl=1" title="emailsnapshotfor_discourse" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_690x369.png" alt="emailsnapshotfor_discourse" data-base62-sha1="kihBOn21R8PtVRLgXOmmQh1HkX5" width="690" height="369" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_690x369.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_1035x553.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_1380x738.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">emailsnapshotfor_discourse</span><span class="informations">1785×957 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd.png" data-download-href="/uploads/short-url/fbouz9wOGqAIrg53sbSMycbiylv.png?dl=1" title="repo_snapshotforDiscourse" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_690x362.png" alt="repo_snapshotforDiscourse" data-base62-sha1="fbouz9wOGqAIrg53sbSMycbiylv" width="690" height="362" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_690x362.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_1035x543.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_1380x724.png 2x" data-dominant-color="F8F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">repo_snapshotforDiscourse</span><span class="informations">1842×968 84.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
please just check my repo  manually  and clarify whether it was public or not . What is going on this degree .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615991)

And also i ran the evaluate.py and got the 10/10 during submission , atleast you can give 4-5 by which i can pass this course .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615993)

Hi sir<br>
I noticed a discrepancy in my Project 1 results. In the initial results shared on March 29th, I had received 8/20 based on the evaluation logs. However, the final result I received today states that none of the tasks in Task A and B were working, and I was awarded only 1 bonus mark.
During my own testing, I was consistently getting 7/10 correct in Task A, so I’m a bit confused about the change.<br>
Kindly request you to look into this discrepancy sir<br>
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615995)

Dear <a class="mention" href="/u/carlton">@carlton</a> Sir,
I was getting 8 marks in your evaluation but today I checked the mail, I was awarded 0 marks. I am not sure what happened. Everything was in place. I would really appreciate if you can provide a reason for zero marks. I rechecked everything and looks good. Awaiting your reply. Thanks.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png" data-download-href="/uploads/short-url/lUWCNqwaeVX5ibm4gFUBnc5LIST.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png" alt="image" data-base62-sha1="lUWCNqwaeVX5ibm4gFUBnc5LIST" width="452" height="132"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">452×132 6.53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/615996)

same i also got 8 marks but today in mail i got 0 marks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616004)

Same issue for me, I was getting 10/20 earlier and now, in mail it shows 1.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616008)

Same issue for me, i had got 4/20 before but in the mail, my marks is given as 0. Please help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616011)

Respected sir,<br>
I have passed all pre-requisites however my file wasn’t evaluated due to port error (127.0.0.1). Please allow me rectify it as it everything else has passed and is in accordance to the guidelines and I had worked really hard for it not to be evaluated only.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616019)

Dear <a class="mention" href="/u/carlton">@carlton</a> Sir,<br>
I’ve noticed discrepancies in my Project 1 results. During the tests I ran before submitting, I consistently got about 7/10 in Task A. In the results shared earlier, I was informed that my evaluation log file was missing. Later, a Gform regarding the architecture was sent, which I filled and submitted. Now, the final result I received today, shows that the taskA module is missing and I’ve been given a bonus of 1 mark.<br>
I kindly request you to look into the matter and provide an explanation and solution in this regard.<br>
Thank you.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616020)

Respected Sir,
I hope you’re all doing well. I’m writing regarding my Project 1 evaluation, as I’ve encountered a discrepancy that I’d like some help with.
According to the evaluation email I received, my score was 0 for all the tasks with an additional bonus of 1 (totaling a P1 score of 1). However, when I ran the provided evaluation script before my submission, I got 7 in Phase A. Additionally, after reviewing the Docker logs, evaluation logs, and the p1_evaluation_error_logs (from the linked Google Sheets), I couldn’t find any reference to my roll number.
Could someone please help me investigate this issue? I’d really appreciate any guidance from the evaluation team.
Thank you for your time and assistance!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616038)

<a class="mention" href="/u/carlton">@carlton</a> i am sure i had cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found my be but still i have been alloted 0 in all the cases , this is no small issue as project holds a significant amount of weightage in the end term<br>
I had spent hours finishing my project and this i am sure my marks are not on par with the desired work i did<br>
Look into this matter as it signifies if i will be able yo pass tds in this term or not.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616039)

I am facing the exact same issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616040)

Hi Hari,
I just <em>manually</em> checked your repo.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg" data-download-href="/uploads/short-url/5Pc8doq0Qsv0W9yCDCdawqbbEYp.jpeg?dl=1" title="Screenshot 2025-04-06 at 5.32.06 pm"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_690x436.jpeg" alt="Screenshot 2025-04-06 at 5.32.06 pm" data-base62-sha1="5Pc8doq0Qsv0W9yCDCdawqbbEYp" width="690" height="436" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_690x436.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_1035x654.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_1380x872.jpeg 2x" data-dominant-color="ADB9B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-06 at 5.32.06 pm</span><span class="informations">1504×952 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This is what <em>you</em> submitted:

2/15/2025 21:08:32<br>
21f3002112@ds.study.iitm.ac.in<br>
<a href="https://github.com/harrypandey829/tds_llm_automation-agent"> https://github.com/harrypandey829/tds_llm_automation-agent</a><br>
hariompandey6388/ll-automation-agent2<br>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616044)

<a class="mention" href="/u/carlton">@carlton</a>  sir  When I submitted project 1, I was passing part A with 8/10 marks but today it is showing 0 marks on my email, but when I run it just now it is showing 4/10 on my vs code.<br>
Whereas when I download the file from GitHub and run it, it is showing 1/10 now.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618.png" data-download-href="/uploads/short-url/msUKaHFancESX8hfFIglGtezbfy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_690x351.png" alt="image" data-base62-sha1="msUKaHFancESX8hfFIglGtezbfy" width="690" height="351" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_690x351.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_1035x526.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_1380x702.png 2x" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1897×965 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5.jpeg" data-download-href="/uploads/short-url/97nvuIRMFIEIuCEkd2FfDvH3O97.jpeg?dl=1" title="WhatsApp Image 2025-04-06 at 17.28.47_927a687b" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_666x500.jpeg" alt="WhatsApp Image 2025-04-06 at 17.28.47_927a687b" data-base62-sha1="97nvuIRMFIEIuCEkd2FfDvH3O97" width="666" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_666x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_999x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_1332x1000.jpeg 2x" data-dominant-color="5A5D5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2025-04-06 at 17.28.47_927a687b</span><span class="informations">1600×1200 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616051)

To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.
<pre data-code-wrap="python"><code class="lang-python"># /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&amp;per_page=1&amp;page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

    # Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

        # Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

        # Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

        with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

        # Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

    else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")
</code></pre>
Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.
<code>docker build -t &lt;your image name&gt;   .</code>
Run new docker image using<br>
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 &lt;your image name&gt;</code>
Keep datagen.py and evaluate.py in same folder<br>
<code>uv run evaluate.py --email &lt;any email&gt; --token_counter 1 --external_port 8000</code>
This then re-produces the exact environment how your application was  tested.<br>
You have to provide a token from your environment for testing.
These instructions are same for everyone. So check first before posting here.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616053)

I am also facing same issue cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found  but still i have been alloted 0 in all the cases

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616054)

<a class="mention" href="/u/arunvembu">@Arunvembu</a> <a class="mention" href="/u/22f2000008">@22f2000008</a> <a class="mention" href="/u/23f1000879">@23f1000879</a> <a class="mention" href="/u/22f3003201">@22f3003201</a> <a class="mention" href="/u/23f2000926">@23f2000926</a> <a class="mention" href="/u/22f3001702">@22f3001702</a> <a class="mention" href="/u/santoshsharma">@Santoshsharma</a> <a class="mention" href="/u/kartikay1">@kartikay1</a> <a class="mention" href="/u/kasif">@Kasif</a>
Check first by following the instructions show here:<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
git clone &lt;your repo url&gt; 
cd &lt;your repo directory&gt; 
docker build -t &lt;your image name&gt; 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt; 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  </blockquote>
</aside>

Then post with your queries after testing as mentioned above.<br>
Also check the evaluation logs first to see why it failed. Address that question.<br>
Posting “it ran before submission” is insufficient evidence.<br>
The whole point of deployability is that it runs anywhere at anytime.<br>
That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616058)

But in email u said n , your repo was not public, even not had dockerfile nor mit licence that’s what I mentioned.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616063)

Your repo is not public! Thats why we cannot see any other files either. If its not public we cannot see if other files exist. We cannot evaluate an invisible repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616066)

I got email , your repo was not public even had not a dockerfile nor mit licence, that’ what I mentioned.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616067)

My repo is public even before it was. How can I set to public..thisis same n while creating new repo u just select the public and not private that’s it n.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616068)

What else I can do . For public.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616069)

You misspelt your repo. Did you even check the post i sent with your details?
<aside class="quote quote-modified" data-post="314" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    Hi Hari, 
I just manually checked your repo. 
 <a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg" data-download-href="/uploads/short-url/5Pc8doq0Qsv0W9yCDCdawqbbEYp.jpeg?dl=1" title="Screenshot 2025-04-06 at 5.32.06 pm">[Screenshot 2025-04-06 at 5.32.06 pm]</a> 
This is what you submitted: 

2/15/2025 21:08:32 
21f3002112@ds.study.iitm.ac.in 
<a href="https://github.com/harrypandey829/tds_llm_automation-agent"> https://github.com/harrypandey829/tds_llm_automation-agent</a> 
hariompandey6388/ll-automation-agent2 
Kind regards
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616072)

Dear <a class="mention" href="/u/jivraj">@Jivraj</a>  <a class="mention" href="/u/carlton">@carlton</a> Sir,<br>
I run evalution  script that you provide us via mail recently, my code is actively running and able to pass 11 task but I was awarded 1 Marks pls check where is the issue,[My full code was done in linux Environment]  (github codespace)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2.png" data-download-href="/uploads/short-url/9wvbcrQ9VPMr8UroyhLEhM16ria.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_690x170.png" alt="image" data-base62-sha1="9wvbcrQ9VPMr8UroyhLEhM16ria" width="690" height="170" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_690x170.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_1035x255.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_1380x340.png 2x" data-dominant-color="D1CFD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1380×341 63.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616075)

You have to replicate this test environment for testing.
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
git clone &lt;your repo url&gt; 
cd &lt;your repo directory&gt; 
docker build -t &lt;your image name&gt; 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt; 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…
  </blockquote>
</aside>

Please replicate this first. We also run it on a linux server.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616077)

I am not talking about this , just see the snapshot that I applied above on that email u said your repo is not public

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616078)

We are ONLY going to evaluate what you submitted. Its the same rule for everyone. If the repo you provided is not accessible,  you will not be evaluated.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616081)

Okay tell me one thing if I got fail in this course then in the next term, I will have not to give roe because it’s rule for every other courses.And see provide the content of tds in Indian guy youtuber because we belong to rural areas and not able to understand the accent of foreigners youtuber . It’s kind your sympathy.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616083)

<strong>Things i have done for my project to work locally:</strong>
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>git clone &lt;your repo url&gt;</code>
</blockquote>
</aside>
cloned my repo which looked like this after cloning(ignore those green dots)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png" data-download-href="/uploads/short-url/bCYFeHxVzBnl2fAh3CxgzgJ8Xdw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png" alt="image" data-base62-sha1="bCYFeHxVzBnl2fAh3CxgzgJ8Xdw" width="205" height="88"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">274×118 2.87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
All the files are  in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
Keep datagen.py and evaluate.py in same folder
</blockquote>
</aside>
when i do this( <img src="https://emoji.discourse-cdn.com/google/down_arrow.png?v=14" title=":down_arrow:" class="emoji" alt=":down_arrow:" loading="lazy" width="20" height="20">) i get this error
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>docker build -t &lt;your image name&gt;</code>
</blockquote>
</aside>
<pre><code class="lang-auto">PS D:\TDS_Project_1\tds-project-1&gt; docker build -t "tushar2k5/tds-project-1"                                                                 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build
</code></pre>
Instead,in order to run the docker image successfully  we have to do either of the two things(taken help from chatgpt <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">):<br>
1)
<pre><code class="lang-auto">Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1
</code></pre>
<strong>OR</strong><br>
2)
<pre><code class="lang-auto">Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .
</code></pre>
<em>Both the things work for me</em>(<img src="https://emoji.discourse-cdn.com/google/up_arrow.png?v=14" title=":up_arrow:" class="emoji" alt=":up_arrow:" loading="lazy" width="20" height="20">)
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 &lt;your image name&gt;</code>
</blockquote>
</aside>
<pre><code class="lang-auto">docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1
</code></pre>
Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)
<aside class="quote group-ds-students" data-username="carlton" data-post="316" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar"> carlton:</div>
<blockquote>
<code>uv run evaluate.py --email=&lt;any email&gt; --token_counter 1 --external_port 8000</code>
</blockquote>
</aside>
<pre><code class="lang-auto">uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000 
</code></pre>
Done this to evaluate my project
Any finally the main part (DRUM ROLLS <img src="https://emoji.discourse-cdn.com/google/drum.png?v=14" title=":drum:" class="emoji" alt=":drum:" loading="lazy" width="20" height="20">,not this one <img src="https://emoji.discourse-cdn.com/google/oil_drum.png?v=14" title=":oil_drum:" class="emoji" alt=":oil_drum:" loading="lazy" width="20" height="20"> (IUKUK))
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png" data-download-href="/uploads/short-url/A19AAp90vJqY6Tc8TKnucEVq8qg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png" alt="image" data-base62-sha1="A19AAp90vJqY6Tc8TKnucEVq8qg" width="690" height="143" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1462×305 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<strong>THATS 6/25</strong>
Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png" data-download-href="/uploads/short-url/cguFlhUIw1ujkDBstIwdfq9uP3T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png" alt="image" data-base62-sha1="cguFlhUIw1ujkDBstIwdfq9uP3T" width="686" height="141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">686×141 5.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Hopping to get a response from you guys,<br>
Thanks a lot(wrote this much for first time for any course)<br>
(PS:This course has some special place in my heart <img src="https://emoji.discourse-cdn.com/google/heart.png?v=14" title=":heart:" class="emoji" alt=":heart:" loading="lazy" width="20" height="20">)<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616101)

We fetched your latest github commit before 18th Feb and build image through that and evaluated.
Your latest github repo before 18 has:<br>
username : <code>singh-yash129</code><br>
Repo : <code>Large-Language-Model</code><br>
commit_sha: <code>88f7439471151283f1218b46d209030dd7f4e5ae</code>
Use <code>https://github.com/&lt;username&gt;/&lt;repo&gt;/archive/&lt;commit_sha&gt;.zip</code> for downloading repo.
If You feel there is any problem with our evaluation script suggest edits to the scirpt.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616103)

<aside class="quote group-ds-students" data-username="23f2003751" data-post="330" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003751/48/68010_2.png" class="avatar"> 23f2003751:</div>
<blockquote>
Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly
</blockquote>
</aside>
Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616107)

<aside class="quote group-ds-students" data-username="Jivraj" data-post="332" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar"> Jivraj:</div>
<blockquote>
Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.
</blockquote>
</aside>
Sorry but its not possible to attend every single session and you guys haven’t informed us via email so how its our fault.For cases like this you guys should allow us to move our files to the root directory so it can work…(we just have to move files  in the repo please consider it)<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/s.anand">@s.anand</a><br>
(i have already made a rookie mistake in my dockerfile otherwise i would have got 9/25 but keeping that aside please let me get 6/25)<br>
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41dc27831c97af2f02287cec795a281e9672723d.gif" alt="PuppyDogEyesSadGIF" data-base62-sha1="9oCIgWPIw9YoJzkRHedgTRNFgkZ" width="373" height="299" class="animated"> <img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/e/3e588079c65a2f9979f97bb5f1d81e3c1691ab20.gif" alt="GojoSadGojoGIF" data-base62-sha1="8Txdua9I8G62oB8mXByH6iPUNhe" width="260" height="312" class="animated">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616117)

Good evening sir.
My original project evaluation conducted by IITM gave me 7/20, however the new evaluation gave me 0/20.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17.png" data-download-href="/uploads/short-url/tb883n42c5TMle3vrZL5uPPvaBx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17_2_361x500.png" alt="image" data-base62-sha1="tb883n42c5TMle3vrZL5uPPvaBx" width="361" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17_2_361x500.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17_2_541x750.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17.png 2x" data-dominant-color="C9C8C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">650×898 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This was from the official evaluation sir, could you kindly look into it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616125)

did everything as mentioned i got 7/25 but in mail i got 2 which is bonus?<br>
i know i didn’t add flask in docker it was my mistake <img src="https://emoji.discourse-cdn.com/google/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> but can we just for once neglect that. pleaseeeeeeeee
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png" data-download-href="/uploads/short-url/1nnIu71aAEAWmgX7JASmZ6W1Em9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png" alt="image" data-base62-sha1="1nnIu71aAEAWmgX7JASmZ6W1Em9" width="690" height="218" data-dominant-color="170525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">787×249 8.87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616128)

Please do consider allowing us to change the position of the dockerfile to the root. We are doing nothing but changing its location in the repo. This was not mentioned anywhere in the prerequisites before the submission and it is unfair to not consider all our work for a criteria that was nowhere mentioned in the course page before the submissions. It may be standard practice but a lot of us were unaware. Please do consider this request.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616129)

Sir, could you please fetch my latest GitHub commit before 18th Feb and build the image through that one?<br>
I received a mail saying that the Docker image is not accessible, but it is already there. Kindly request you to evaluate my submission.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616130)

Hi <a class="mention" href="/u/abhay222">@Abhay222</a>
Docker image submitted by you doesn’t exists.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/6/f633d628d646e068273aef8682b5405527cabb65.png" data-download-href="/uploads/short-url/z80w3xlHyTgN8aLgm9GStYGi7mB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_690x342.png" alt="image" data-base62-sha1="z80w3xlHyTgN8aLgm9GStYGi7mB" width="690" height="342" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_690x342.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_1035x513.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_1380x684.png 2x" data-dominant-color="154060"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×943 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616133)

Hi <a class="mention" href="/u/23f1000879">@23f1000879</a>
This basically tells you didn’t validate docker Dockerfile and docker image by building and running them, otherwise you would have corrected the mistake.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616135)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png" data-download-href="/uploads/short-url/fDipvC3jgzS5ipBufnfHjh2NUC5.png?dl=1" title="Screenshot 2025-04-02 132214" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png" alt="Screenshot 2025-04-02 132214" data-base62-sha1="fDipvC3jgzS5ipBufnfHjh2NUC5" width="690" height="93" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_1035x139.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_1380x186.png 2x" data-dominant-color="131920"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-02 132214</span><span class="informations">1843×250 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
but it is available under version1.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616136)

repo that you submitted through google form was different then this one.
Your Gform response
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f.png" data-download-href="/uploads/short-url/qlMyWlexbzC3vojpkB27vkd28IT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_690x100.png" alt="image" data-base62-sha1="qlMyWlexbzC3vojpkB27vkd28IT" width="690" height="100" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_690x100.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_1035x150.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_1380x200.png 2x" data-dominant-color="1A212C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1660×242 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616140)

Hi, I work in the IT industry. There is no standard like “docker file has to be only in the root folder.”
If at all you are setting a requirement why was this not mentioned in the project page?
We were asked to build an app which solves the given tasks. You were OK for whatever code/tools/method to use as long as it works, there the “industry standard” didn’t show up ironically!!!
Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.
In the same industry that I work - we build the dockers and give it for prod push.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616141)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Dear Sir,<br>
I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.<br>
I debugged that I had a small issue in the dockerfile that was submitted and it is<br>
CMD [“/root/.local/bin/uv”, “run”, “app.py”]  has an <strong>invisible Unicode non-breaking space</strong> (<code>U+00A0</code>) between <code>"run", "app.py"</code> instead of a regular space. This causes the shell to misread the command.<br>
I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE.  Expecting a positive response from your end.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616146)

sir, but before submission i run evluate.py and it gave me 8/10 in task A. after submission i also got result mail stating that i got 8/20.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/6/6689843088265aa67624484279c35e788ed5d74c.png" data-download-href="/uploads/short-url/eD5kqmOu4yE6aBKl8uZmG6o2EuU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_690x341.png" alt="image" data-base62-sha1="eD5kqmOu4yE6aBKl8uZmG6o2EuU" width="690" height="341" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_690x341.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_1035x511.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_1380x682.png 2x" data-dominant-color="CAC9C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1895×938 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
also this mail result Earlier i got From your side. <img src="https://emoji.discourse-cdn.com/google/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616150)

Sir, I realized that I mistakenly submitted the image tag <code>"abhay227/version1"</code> instead of the correct image ID. The correct image ID is <code>4db729a03f74</code>, which is part of version1 and is already present and publicly available.<br>
Unfortunately, I didn’t receive any notification about this issue after submission. Receiving this mail at this stage feels disheartening after all the effort I’ve put into the project.  I kindly request you please consider this correct image ID.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616151)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png" data-download-href="/uploads/short-url/zUXCv89JCNRQwOB0Ig4VD9EbO2F.png?dl=1" title="Screenshot 2025-04-06 202736" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png" alt="Screenshot 2025-04-06 202736" data-base62-sha1="zUXCv89JCNRQwOB0Ig4VD9EbO2F" width="662" height="141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-06 202736</span><span class="informations">662×141 5.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Hi, all my pre-requisites have been fulfilled, and the evaluation logs say I have a score of 10/25. But I have gotten a score of 0, saying ‘Task A module missing’. This is a kind request to confirm the scores.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616154)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388.png" data-download-href="/uploads/short-url/f20KUUxWpvkyDSACNDccXUDXDPW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_690x282.png" alt="image" data-base62-sha1="f20KUUxWpvkyDSACNDccXUDXDPW" width="690" height="282" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_690x282.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_1035x423.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_1380x564.png 2x" data-dominant-color="F4F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×783 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e.png" data-download-href="/uploads/short-url/oS7oODUISGSSWst3MfISEPcF4Cy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_690x236.png" alt="image" data-base62-sha1="oS7oODUISGSSWst3MfISEPcF4Cy" width="690" height="236" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_690x236.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_1035x354.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_1380x472.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×654 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda.png" data-download-href="/uploads/short-url/1y3HWgRloAVFDTcEalIMKh9qfuW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_690x240.png" alt="image" data-base62-sha1="1y3HWgRloAVFDTcEalIMKh9qfuW" width="690" height="240" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_690x240.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_1035x360.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_1380x480.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1899×663 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I cannot find my docker_logs nor evaluation_logs and nor anything on the forms . The mail I got says that i received 0 in project tasks but clearly my project is not evaluated. Please look into this. during earlier evaluation i got 7 marks but this time it is 0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b.png" data-download-href="/uploads/short-url/yaxDMke8HoCGdMeRqZ61SmVXbRx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_690x386.png" alt="image" data-base62-sha1="yaxDMke8HoCGdMeRqZ61SmVXbRx" width="690" height="386" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_690x386.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_1035x579.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_1380x772.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×814 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
My roll number is 23f1001524 .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616155)

<a class="mention" href="/u/carlton">@carlton</a> and <a class="mention" href="/u/jivraj">@Jivraj</a> , for Task A i had tested before and all the test cases passed, but all my A tasks has failed with 0, In the evaluation logs, i could see that all task A tests failed due to datagen.py not available.
Could you rerun the test ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616156)

Respected Sir,
Thank you for your response and for providing the steps to replicate the test environment.<br>
Steps Taken to Replicate the Test Environment<br>
I cloned my repository using:
<pre><code class="lang-auto">bash
git clone &lt;my_repo_url&gt;
cd &lt;my_repo_directory&gt;
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=&lt;any_email&gt; --token_counter 1 --external_port 8000
</code></pre>
Issue with Original Submission<br>
After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.
However, during your evaluation, this incompatibility caused the container to fail.<br>
I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.
Action Taken<br>
To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:
The application initializes correctly on port 8000 within 5 minutes.
It responds to requests within the required timeframe.
I have pushed this updated image to Docker Hub under the same repository:<br>
Docker Hub URL: santoshsharma003/tds-project-one-1:latest
Request for Re-Evaluation<br>
I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.
Previous Message for Reference<br>
For your convenience, here is my earlier message explaining this issue in detail:
"Greetings, Sir,
I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.
To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.
I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.
Thank you for your assistance!"

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616168)

same for me<br>
my roll number is 23f1003094

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616189)

Same with me sir <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616191)

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  </blockquote>
</aside>

Because if you did, you will realise why your evaluation failed.<br>
You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616193)

You can take it up with <a class="mention" href="/u/s.anand">@s.anand</a><br>
I did not come up with the standard.<br>
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.
<blockquote>
Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.
</blockquote>
Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand if we could make the allowance. He made the decision to enforce this protocol.
Kindest regards.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616195)

<a class="mention" href="/u/carlton">@carlton</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c.png" data-download-href="/uploads/short-url/6NrbGjttDAtAU7aWm5jII996wPO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_690x348.png" alt="image" data-base62-sha1="6NrbGjttDAtAU7aWm5jII996wPO" width="690" height="348" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_690x348.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_1035x522.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_1380x696.png 2x" data-dominant-color="C0C0C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×955 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Respected Sir,<br>
see the above image its from the scores we got from mail just before the latest one, in that I had got 7/20 and now new mail shows I got 0?? how is this possible…<br>
the link for evaluation in which i got 7/20 is : <a href="https://drive.google.com/file/d/1cNVy9KSfSITZg_KGLF2_wwLWjzNl8mb5/view" class="inline-onebox" rel="noopener nofollow ugc">23f2001390@ds.study.iitm.ac.in_evaluation.log - Google Drive</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e.png" data-download-href="/uploads/short-url/p4Gtp6UGhC7NKXFdAngZUi3avUy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e_2_690x384.png" alt="image" data-base62-sha1="p4Gtp6UGhC7NKXFdAngZUi3avUy" width="690" height="384" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e_2_690x384.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e_2_1035x576.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1315×732 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
MOST importantly mail shows :<br>
<strong>Your final t score</strong> calculation is based on
MIN (20, (task score + bonus))
<strong>Github repo submitted:</strong> <a href="https://github.com/23f2001390/llmagent" class="inline-onebox" rel="noopener nofollow ugc">GitHub - 23f2001390/llmagent</a>
<strong>Docker repo submitted:</strong> 23f2001390/llmagent
<strong>Pre-requisites check: (1 for pass, 0 for fail)</strong>
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1<br>
Your task score is: 0<br>
Your bonus is: 1<br>
Your P1 score is: 1
<hr>
So according to the above, I passed the pre-requisites and also in mail u have mentioned that:<br>
We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.
but I don’t find my mail id or roll number in the docker_logs.zip or evaluation_logs.zip  that has been given in the mail(latest), if I passed the pre requisites my logs should be there in the zip files included in this latest mail right, my roll number is 23f2001390 and email id is 23f2001390@ds.study.iitm.ac.in<br>
and nor do i find my id in the p1_evaluation_error_logs so please help sir<br>
Thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b.png" data-download-href="/uploads/short-url/9jP46fB7vquZ92zeRUCvDlWsRVV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b_2_690x327.png" alt="image" data-base62-sha1="9jP46fB7vquZ92zeRUCvDlWsRVV" width="690" height="327" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b_2_690x327.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b_2_1035x490.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b.png 2x" data-dominant-color="FDFDFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1078×511 8.14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0.png" data-download-href="/uploads/short-url/uCh4VEtWox32lJF2n9N4jHKn6h2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0_2_690x336.png" alt="image" data-base62-sha1="uCh4VEtWox32lJF2n9N4jHKn6h2" width="690" height="336" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0_2_690x336.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0_2_1035x504.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0.png 2x" data-dominant-color="FDFDFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1083×528 8.42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df.png" data-download-href="/uploads/short-url/rMjfMvzCYJHxo15IcaCSe5HYAUf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_690x351.png" alt="image" data-base62-sha1="rMjfMvzCYJHxo15IcaCSe5HYAUf" width="690" height="351" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_690x351.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_1035x526.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_1380x702.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×970 78.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616197)

<a class="mention" href="/u/carlton">@carlton</a><br>
Same for sir. I have made my post similarly, roll number is 23f2001390 and email is 23f2001390@ds.study.iitm.ac.in

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616203)

<a class="mention" href="/u/carlton">@carlton</a><br>
i  also not found anything in this form  , but i got mail to score=0<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3.png" data-download-href="/uploads/short-url/mzh3ffonvO0fEkOcy3Pw93PVidJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_690x305.png" alt="image" data-base62-sha1="mzh3ffonvO0fEkOcy3Pw93PVidJ" width="690" height="305" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_690x305.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_1035x457.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_1380x610.png 2x" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1893×837 85.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <img src="https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20">

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616205)

Hi Hari,
Your docker failed to build.
Did you try to replicate the test environment as mentioned in
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  </blockquote>
</aside>

If you tried you would find that it will not build. Thats why you have no logs.<br>
90 such cases are there where the image could not be built from your repo.
The specific error in your case is:<br>
tried copying requirements.txt which doesn’t exists
Thats why there are no logs.<br>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616206)

Hello <a class="mention" href="/u/carlton">@carlton</a> Sir, please reply to my query

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616212)

We cannot allow changes to repos. This is a blanket rule for everyone. No exceptions. Since the only way to get your project to work is to make changes to it, we cannot score you for changes.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616213)

Thanks for the response. We can go on endless discussions using “nice words” “professionally” with the number of questions we have. Finally we are at the receiving end as students in this setup.
What’s the take away for everyone? Let’s move on. This isn’t the end.
Positive or Negative - Real world outside will make everyone realise and everyone change their opinions (including me) as the time and environment changes.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616214)

What I observed is that most of the repositories appear to be copied from a single source. This original repository contains several issues, such as an incorrectly named Dockerfile and missing instructions to copy all necessary data. Unfortunately, many students seem to have uploaded it blindly without reviewing or fixing these problems.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616233)

Hi I have my Dockerfile saved as dockerfile, given 0 for project 1 due to this. This doesn’t seem to be a big issue to grade me 0 for this. Kindly correct the score please.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616239)

Most common reason for during running docker image was <code>taskA module was missing</code> which is because a lot of students blindly copied from someone with building and running image, if they would have done that they could have corrected it at early stage.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616305)

For you check failed because of the naming of Dockerfile(It was named as dockerfile(d in small).

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616311)

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists
In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616312)

<aside class="quote group-ds-students" data-username="MITALI_R" data-post="351" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/mitali_r/48/66886_2.png" class="avatar"> MITALI_R:</div>
<blockquote>
23f1003094
</blockquote>
</aside>
While running docker image create by your github repo, we got following error <code>taskA module missing</code>
For regenerating it follow steps that are mentioned here : <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316" class="inline-onebox">Tds-official-Project1-discrepencies - #316</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616314)

For you naming of MIT License was not correct.<br>
This shows naming criteria for adding License.<br>
<a href="https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository" rel="noopener nofollow ugc">Adding a license to a repository - GitHub Docs</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616316)

Sir actually my project doesn’t have requirements.txt, instead it installs automatically<br>
when:<br>
<code>uv run app.py</code> is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).<br>
my dockerfile from the repo:
<pre><code class="lang-auto">FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh &amp;&amp; rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
</code></pre>
here u can see it installs using pip install …
here it’s requiring <code>.env</code> file to be present in the project folder because my project when I was uploading to both git and docker had <code>.env</code> file for AIPROXY_TOKEN and I uploaded to docker with that <code>.env</code> file but as git doesn’t allow upload of <code>.env</code> file I couldn’t upload<code>.env</code> to git
the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because<code>.env</code> file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the <code>.env</code> file so it didn’t build so I had to create the <code>.env</code> file now to create the docker image, and for the dockerimage I had submitted, I built it with the <code>.env</code> file(it supports both<code>.env</code> file and environment variable one)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616318)

After filling form you didn’t double check form.
<aside class="quote group-ds-students" data-username="Abhay222" data-post="346" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/abhay222/48/66780_2.png" class="avatar"> Abhay222:</div>
<blockquote>
I kindly request you please consider this correct image ID.
</blockquote>
</aside>
We can’t reconsider it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616319)

Yes problem was missing <code>.env</code> file, Your repo, was supposed to run in a test environment.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616323)

Yes sir, please help me

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616325)

Sorry We can’t do any help, we won’t be considering for eval.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616326)

But sir, It was supposed to run right…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616328)

It Should build in any test environment using Dockerfile from your github repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616329)

<a class="mention" href="/u/jivraj">@Jivraj</a> please tell me what was my mistake?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616330)

It was named wrongly.<br>
You named it LICENCE but it should be LICENSE or LICENSE.md.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616332)

But sir, just because the repository doesn’t have .env file it couldn’t build the dockerimage, the docker image will build in any test environment as u said but it requires the .env to be included which the git didn’t have(it doesn’t allow upload of it ofcourse), don’t rerun the evaluation again but please sir atleast give me those 7/20 marks along with the pre-requisite bonus(1mark) that was mailed earlier to me along with logs…this is my primary degree after 12th, I’m also not asking any extra marks just the marks that i got earlier:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e.png" data-download-href="/uploads/short-url/3fYWhioqF0dVCW0CqLGyjCLCVMa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_690x380.png" alt="image" data-base62-sha1="3fYWhioqF0dVCW0CqLGyjCLCVMa" width="690" height="380" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_690x380.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_1035x570.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_1380x760.png 2x" data-dominant-color="BBBBBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1850×1021 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616338)

Hi <a class="mention" href="/u/23f2002600">@23f2002600</a> <a class="mention" href="/u/21f1005908">@21f1005908</a>
<aside class="quote quote-modified" data-post="354" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    You can take it up with <a class="mention" href="/u/s.anand">@s.anand</a> 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616340)

Runned for you, it A1 Fails.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616341)

Your docker image and github repo are not consistent,  your docker image was not built with the latest code before 18th feb that’s present in your github repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616342)

We can’t consider any changes after deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616343)

Your docker image and github repo are not consistent.
While running docker image we got following error: <code>flask module missing</code><br>
For regenerating this error follow steps mentioned in below post.<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616344)

Anything after deadline we can’t consider any changes, it was just a matter of time, you didn’t tests running evaluate.py on docker container that was created, otherwise you would have spotted this mistake and rectified it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616345)

In your github repo, Dockerfile should be named as Dockerfile(D caps).

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616346)

I don’t know reason behind it, earlier evaluation was done by pulling docker image.<br>
Latest one was done through github repo, if code in github repo is not consistent with docker image it might cause problems.
LLM won’t provide same results every time, for that reason we have give bonus marks.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616347)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@jivraj</a> sir it is my humble request to do something. We are losing our marks because of small negligence or mistakes like i fogot to commit my requirements.txt in my github repository. Already the course has taken tolls on our mind. Please give partial marks for the correct run of the docker image or please evaluate my latest commit with the requirements.txt. Because of this project I will lose my cgpa and the hardwork that I have done till this term. A small mistake is causing me my full marks and grades. Atleast consider partial marking for the docker image which does the tasks. I have maintained 9+ cgpa in the diploma and I took other subjects which are easy this term like BDM still is really difficult to cope with the subject. Please consider something. atleast give 50% of the marks for each task which my image passes.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616354)

Sir but i did test my project via evaluate.py and got the 8/10 in my tasks A. A simple port error has resulted in no evaluation at all after all the hardwork.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616355)

Sir, how my git repo is not consistent i used the same repo which i have given you in the form even i did not commit any changes after 18th feb also in my docker file there is just a simple mistake that i forgot to add flask dependency just because of that mistake i am losing my marks. I also used same docker image which i have given you through form. Its my humble request please consider or give some solution. It felt like betrayal because we put effort’s.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616361)

Dear Sir,<br>
I understand that this request is coming at a late stage, and I truly apologize for the timing. However, I felt it was important to express how much effort and dedication I have invested in this project and throughout the course. The recent issue has been disheartening for me, especially because the work I submitted was not a blind copy from someone else.
Had it been otherwise, I wouldn’t have had the courage to reach out. I genuinely care about this course and the learning it offers, and I’m proud of the commitment I’ve shown so far.
With utmost respect, I kindly request you to reconsider evaluating my project again, if there’s any possible way to do so. It would mean a lot to me and would really motivate me to keep pushing forward in this subject.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616388)

Hi <a class="mention" href="/u/23f1001524">@23f1001524</a> <a class="mention" href="/u/afsalshah">@afsalshah</a> <a class="mention" href="/u/23f1000879">@23f1000879</a> <a class="mention" href="/u/23f1002056">@23f1002056</a>
I understand your situation. We discussed all these scenarios in our weekly meets, and it was decided that we cannot make allowances for these because there was ample time to test your deployments and also ample sessions were conducted to address any difficulties you might have faced. A basic minimum standard was expected and we are unable to relax that threshold because then it would make evaluations meaningless.
We are not just evaluating on your agent functions. We require deployability as a minimum target. If you solution was not deployable and functional then we cannot evaluate the functioning of your application. Once again I sympathise with what might seem minor errors. But they are not minor, even though it may only be a line that needs changing or a spelling mistake. They actually cause a critical failure.
<strong>A minor mistake is a function not working that does not prevent other things from working.</strong>
<strong>Critical failures prevents everything else from working</strong> and thus most of these what seems like minor failures are missclassified. They are in fact critical failures.
I know its not of much comfort right now, but the learnings from this will be important going forward in your career.
Kindest regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616396)

Hi <a class="mention" href="/u/carlton">@carlton</a> ,
I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png" data-download-href="/uploads/short-url/A7coZQExGa1MqCCfz5m4svLGMDf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png" alt="image" data-base62-sha1="A7coZQExGa1MqCCfz5m4svLGMDf" width="690" height="164" data-dominant-color="252424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×268 9.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Would really appreciate it if you could take a look. Thanks in advance!

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616428)

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:<br>
tried copying multiple files for that you need to give directory name and it should end with a /
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616429)

<a class="mention" href="/u/carlton">@carlton</a>  , I followed all the steps instead of <code>curl -LO https://github.com/&lt;username&gt;/&lt;repo&gt;/archive/&lt;commit_sha&gt;.zip</code>
<code>unzip &lt;path to downloaded zipped repo&gt;</code> , I used git clone .

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616431)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Not able to see the my id in 22f3002723 in evaluation logs or docker logs.. just curious if there was  any issues in creating the image out of github ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616433)

Thanks for the fixes (I have updated the code now). It was put together quickly and not tested before we actually posted it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616476)

Happy to help sir <img src="https://emoji.discourse-cdn.com/google/saluting_face.png?v=14" title=":saluting_face:" class="emoji" alt=":saluting_face:" loading="lazy" width="20" height="20"><br>
(Was expecting some different response from your side,but ig we need to accept our faith <img src="https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14" title=":upside_down_face:" class="emoji" alt=":upside_down_face:" loading="lazy" width="20" height="20">)
Thank you,<br>
(Kindest regards)<br>
Tushar

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616480)

We are checking you submission. We will get in touch shortly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616486)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a>,
I hope you’re doing well. I wanted to humbly request a reconsideration regarding the evaluation of my project submission.
I understand there was an issue with building the Docker image from the repository. However, I had successfully built and pushed the Docker image earlier, and I believe it demonstrates that my solution is deployable. If the final evaluation was solely based on building from the repository, I’m a bit confused about why the Docker image was considered earlier and why we were also asked to upload it to Docker Hub if it wasn’t going to be taken into account later. Also the earlier evaluation score where we got some marks at least and now are hopes are crushed after one night.
I do realize that in the real world, these kinds of errors can be critical, and I truly appreciate that the course is structured to prepare us for such expectations. That said, this course has been quite challenging, and for many students—including myself—it has been a source of considerable stress and demotivation.
I sincerely request that you kindly consider awarding some partial marks for the working Docker image that was built and pushed earlier. It does reflect an understanding of deployable solutions, which I’ve worked hard to demonstrate.
I know you all have our best interests in mind, and I’m grateful for the efforts put into making this a rigorous and enriching course. My only concern is that such harsh penalties—especially for a single oversight—can significantly affect our CGPA and future opportunities. I hope my request can be considered with empathy.
Thank you for your time and understanding.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616511)

Issues with your submission has been resolved.<br>
Thanks for raising the issue and checking it at your end.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616519)

Sir, I sincerely apologize for the mistake I made in naming the LICENSE file as “LIcense” instead of “LICENSE”. I now understand how important these details are, and it was an unintentional oversight on my part. I had put in a lot of hard work into the project, and it would mean a lot to me if you could kindly consider evaluating it, even though the deadline has passed and results are out. I completely understand if it’s not possible, but I just wanted to request a chance as this project was very important to me and I genuinely learned a lot from it.<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616523)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png" data-download-href="/uploads/short-url/9I5fpbJw2BZCgC9OiBFdLxT1OHO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png" alt="image" data-base62-sha1="9I5fpbJw2BZCgC9OiBFdLxT1OHO" width="690" height="405" data-dominant-color="202122"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1188×699 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
cloned the repository using
<pre><code class="lang-auto">git clone https://github.com/23f2001390/llmagent.git
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png" data-download-href="/uploads/short-url/22V3LBhcGLeGbfQ8Uw5xhgoYWD6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png" alt="image" data-base62-sha1="22V3LBhcGLeGbfQ8Uw5xhgoYWD6" width="690" height="477" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1041×721 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
created the <code>.env</code> for the aiproxy token as its needed to build the docker image as per my Dockerfile and <code>.env</code> file cannot be uploaded to git we have to create it while building docker image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2.png" data-download-href="/uploads/short-url/gB0UNUrNZnqpMbje7Mt23Lft27w.png?dl=1" title="evalue" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2_2_378x499.png" alt="evalue" data-base62-sha1="gB0UNUrNZnqpMbje7Mt23Lft27w" width="378" height="499" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2_2_378x499.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2_2_567x748.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2.png 2x" data-dominant-color="222323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">evalue</span><span class="informations">752×994 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
added the new <code>evaluate.py</code> and <code>datagen.py</code> from the mail, trying to replicate the test environment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png" data-download-href="/uploads/short-url/NuYhBW6qFDhU777JjKITbgetdA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png" alt="image" data-base62-sha1="NuYhBW6qFDhU777JjKITbgetdA" width="690" height="436" data-dominant-color="212322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">730×462 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
moved the new <code>datagen.py</code> and <code>evaluate.py</code> into the project folder
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e.png" data-download-href="/uploads/short-url/nG2OeUgbHUGz9z7CBwVf90BsE1w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_690x378.png" alt="image" data-base62-sha1="nG2OeUgbHUGz9z7CBwVf90BsE1w" width="690" height="378" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_690x378.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_1035x567.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_1380x756.png 2x" data-dominant-color="1C1F20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1805×989 79.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
docker image built successfully using
<pre><code class="lang-auto">docker build -t llm-agent .
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1.png" data-download-href="/uploads/short-url/dCf5SPGmN96pXgVqQb2UwLcUaaZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_690x396.png" alt="image" data-base62-sha1="dCf5SPGmN96pXgVqQb2UwLcUaaZ" width="690" height="396" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_690x396.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_1035x594.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_1380x792.png 2x" data-dominant-color="202020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1694×974 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
running the evaluate.py using:
<pre><code class="lang-auto"> uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png" data-download-href="/uploads/short-url/foBysNTpTqXcrLMlwn4zNBPzKXx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png" alt="image" data-base62-sha1="foBysNTpTqXcrLMlwn4zNBPzKXx" width="690" height="483" data-dominant-color="201F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1385×971 46.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
got consistent 6/25 after even running the file 6 times <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/s.anand">@s.anand</a> Please sir check this, just because my docker image needs .env, I cannot get full 0…I need to maintain my cgpa (by getting 0 in project my grade is going too close to E grade sir and already in D, already my ROE got bad due to technical issues which on the same day around 6pm after finding way to unlock the input of answers for roe I completed the roe again in short amount of time like 10 or 20 minutes and got 10/10 but still it was rejected because it was late, max 3 minutes after 1:45PM was allowed…I’m not asking to any extra marks, just my marks) I’m trying to improve it already I have 4 subjects in a single term, please give me atleast this marks with the bonus 1 mark for prerequisites (total 7)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png" data-download-href="/uploads/short-url/koGrEdssvCGfmZaTriig54BkN0u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png" alt="image" data-base62-sha1="koGrEdssvCGfmZaTriig54BkN0u" width="690" height="243" data-dominant-color="EBEBED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">704×248 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616532)

Yes,the Same case happend to me also we have put lot of efforts in this project but after seeing that in mail you have no mit licence, I added that license but with name of mit license actually to just name that license file as MIT license but due to this all our hardwork is just an experience but actually we are not awarding any marks in project1 . I request the TDS team to consider this issue.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616536)

I have passed the pre requisites, but there is no log file for my email.
At least docker logs should be there, right?
Was it missed by any chance?<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png" data-download-href="/uploads/short-url/wCb3txFxnaYfK4JYyVtmFLcFRqO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png" alt="image" data-base62-sha1="wCb3txFxnaYfK4JYyVtmFLcFRqO" width="690" height="120" data-dominant-color="D9D9D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">916×160 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616584)

Sorry to repeatedly ask <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
couldnt see my id (22f3002723) in any of the logs  evaluation or docker .. was there any issue in building image out of docker file in github

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616590)

Hi <a class="mention" href="/u/22f3002723">@22f3002723</a>
 /bin/sh: 1: uv: not found 
This is error that we got on your evaluation while building docker image through github repo.
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username"  # Replace with your actual GitHub …
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616600)

This was error with your submission.<code>tried copying file named </code>app<code> which is not there in github repo</code>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616601)

Respected Sir , <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
My roll number is 23f3001688<br>
Pls check my repository properly because I have dockerfile in my repo but it is mentioned that it is not present.<br>
Here is my repository link and screenshot for your reference sir and the dockerfile is present sir<aside class="onebox githubrepo" data-onebox-src="https://github.com/Sharmilecholan/tds_project1">
  <header class="source">

      <a href="https://github.com/Sharmilecholan/tds_project1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4296a48f50a92933eb573695c91faee58b51a1_2_690x344.png" class="thumbnail" data-dominant-color="F1F3F7">

  <h3><a href="https://github.com/Sharmilecholan/tds_project1" target="_blank" rel="noopener nofollow ugc">GitHub - Sharmilecholan/tds_project1</a></h3>

    <span class="github-repo-description">Contribute to Sharmilecholan/tds_project1 development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

I think the mistake would have been because in my repo the file name is “dockerfile” and you have mentioned it as “Dockerfile” . So is it a mistake to put “D” in lowercase.<br>
Kindly look into this sir because of this I got 0 in project 1 even though many of the tasks of my projects passed the evaluation test.
Regards,<br>
S Sharmile<br>
23f3001688<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8.png" data-download-href="/uploads/short-url/bsbL74iFS0JzQRrxlTsAhpeWVi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_690x281.png" alt="image" data-base62-sha1="bsbL74iFS0JzQRrxlTsAhpeWVi" width="690" height="281" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_690x281.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_1035x421.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_1380x562.png 2x" data-dominant-color="13171D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1904×778 83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616602)

<a class="mention" href="/u/carlton">@carlton</a> sir, i want to clarify about this. I had got 9/20 in the previous mail in my evaluation log and now the recent mail say i got 1 mark. I want to ask about this. Please help me<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d.jpeg" data-download-href="/uploads/short-url/aO4Sn2HSjXQEfa4jq6zDAWdQbs9.jpeg?dl=1" title="WhatsApp Image 2025-04-07 at 15.37.17_fb28b652" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_225x500.jpeg" alt="WhatsApp Image 2025-04-07 at 15.37.17_fb28b652" data-base62-sha1="aO4Sn2HSjXQEfa4jq6zDAWdQbs9" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_450x1000.jpeg 2x" data-dominant-color="181819"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2025-04-07 at 15.37.17_fb28b652</span><span class="informations">720×1600 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c342418d20b935d414f96817c92300bcec289598.jpeg" data-download-href="/uploads/short-url/rRl3HrYSFSFmf26O3wu1Q3zbxBC.jpeg?dl=1" title="WhatsApp Image 2025-04-07 at 15.39.10_edb0b829" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_225x500.jpeg" alt="WhatsApp Image 2025-04-07 at 15.39.10_edb0b829" data-base62-sha1="rRl3HrYSFSFmf26O3wu1Q3zbxBC" width="225" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_225x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_337x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_450x1000.jpeg 2x" data-dominant-color="29282F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2025-04-07 at 15.39.10_edb0b829</span><span class="informations">720×1600 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616622)

I don’t know how to check for the errors I made, <a class="mention" href="/u/jivraj">@Jivraj</a> sir can you at least show the prerequisite form that I submitted so I can check for myself ?.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616631)

<a class="mention" href="/u/jivraj">@jivraj</a>
earlier I built the project inside app folder so it was
<pre><code class="lang-auto">COPY app /app
</code></pre>
it should have been
<pre><code class="lang-auto">COPY . /app
</code></pre>
Is there anything that can be done on your end now?<br>
All the code is there.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616646)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765.png" data-download-href="/uploads/short-url/dKjAqDk0XAiObCod7fUIITBhoFL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_690x86.png" alt="image" data-base62-sha1="dKjAqDk0XAiObCod7fUIITBhoFL" width="690" height="86" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_690x86.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_1035x129.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_1380x172.png 2x" data-dominant-color="1A1F26"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1822×229 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Sorry for late reply,These are 2 submissions that you made we are considering the latest one.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616654)

No we don’t consider any changes after deadline.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616655)

There was a module missing error while lead the docker image to run.
Follow below steps for replicating test environment.<br>
<a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616657)

For dockerfile you have in repo, It was named differently, correct naming has to be Dockerfile.
<aside class="quote quote-modified" data-post="354" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    You can take it up with <a class="mention" href="/u/s.anand">@s.anand</a> 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616663)

<a class="mention" href="/u/24ds1000119">@24ds1000119</a> and <a class="mention" href="/u/yaswanthvaddi">@YaswanthVaddi</a>
We are not considering mismatch in naming for License.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616665)

Dear <a class="mention" href="/u/carlton">@carlton</a>
This is Senthur. I have reviewed the logs, and it indicates that the<br>
<code>/app/app/main.py</code>     file is missing. However, in my project directory, the<br>
<code>main.py</code>   file is located in the   <code>app/</code>   folder, and the   <code>run.py</code>   file is in the root folder of the project, which is   <code>LLM_Automation_Agent</code>  . This structure allows the <code>run.py</code> file to run the project without any issues by calling the appropriate functions from <code>app/main.py</code>.
To run the project, the command I used is:
<pre><code class="lang-auto">python run.py
</code></pre>
Since <code>run.py</code> is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to <code>app/main.py</code>.
I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the <code>run.py</code> script located in the root folder (<code>llm-automation-agent</code>).
For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.
Here is the GitHub link to my project:
<aside class="onebox githubrepo" data-onebox-src="https://github.com/ksenthurkumaran18052004/llm-automation-agent">
  <header class="source">

      <a href="https://github.com/ksenthurkumaran18052004/llm-automation-agent" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce9394993a2cc41f2a17658d6ed40ff9fff7d6a7_2_690x344.png" class="thumbnail" data-dominant-color="EEF2F3">

  <h3><a href="https://github.com/ksenthurkumaran18052004/llm-automation-agent" target="_blank" rel="noopener nofollow ugc">GitHub - ksenthurkumaran18052004/llm-automation-agent</a></h3>

    <span class="github-repo-description">Contribute to ksenthurkumaran18052004/llm-automation-agent development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404.jpeg" data-download-href="/uploads/short-url/e6XLFjN5PrQqC90ksjTjrlFdGPW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_255x500.jpeg" alt="image" data-base62-sha1="e6XLFjN5PrQqC90ksjTjrlFdGPW" width="255" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_255x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_382x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_510x1000.jpeg 2x" data-dominant-color="1D1F21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×2823 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Lookig forward towards your support.
With Regards<br>
K Senthur Kumaran

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616666)

Same here sir, i only changed LICENSE to MIT LICENSE due to the mail i received.<br>
The LICENSE file was already present in the repo as i submitted my project. The change too was made on the 16th of Feb.<br>
Sir, I would highly appreciate if you consider it as the rest of the pre-requisites are working well.Due to this, the project is also not being evaulated.<br>
Thankyou<br>
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616667)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9.png" data-download-href="/uploads/short-url/rEDhJXcG5IlxU7DRnlQ7T7u0QIh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_690x149.png" alt="image" data-base62-sha1="rEDhJXcG5IlxU7DRnlQ7T7u0QIh" width="690" height="149" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_690x149.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_1035x223.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_1380x298.png 2x" data-dominant-color="171717"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1823×395 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Just checked right now. I am getting this error.
Replicate test environment following this post.<br>
<a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA</a>0

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616672)

<pre><code class="lang-auto">🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

</code></pre>
<h1><a name="p-616683-result-header-1" class="anchor" href="#p-616683-result-header-1"></a><img src="https://emoji.discourse-cdn.com/google/warning.png?v=14" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20"> RESULT:<br>
Header</h1>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:left">Start</th>
<th>Mid</th>
<th style="text-align:right">End</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">1</td>
<td>2</td>
<td style="text-align:right">3</td>
</tr>
</tbody>
</table>
</div>Paragraph has extra   spaces and trailing whitespace.
<pre data-code-wrap="py"><code class="lang-py">print("23f3003027@ds.study.iitm.ac.in")

</code></pre>
<img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> A2 FAILED
<pre><code class="lang-auto">I am facing Npx error... can I know what went wrong?
@carlton @Jivraj</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616683)

<aside class="quote group-ds-students" data-username="23F300327" data-post="424" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png" class="avatar"> 23F300327:</div>
<blockquote>
<pre><code class="lang-auto">I am facing Npx error... can I know what went wrong?
</code></pre>
</blockquote>
</aside>
This <code>npx</code> error is originating from your Docker container—it’s not being generated by our script. Try to look for what caused this error.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616681)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090.png" data-download-href="/uploads/short-url/5Q6aDx3wNkklXwRs2Xt6qb0qOuQ.png?dl=1" title="Screenshot 2025-04-07 213538" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_690x311.png" alt="Screenshot 2025-04-07 213538" data-base62-sha1="5Q6aDx3wNkklXwRs2Xt6qb0qOuQ" width="690" height="311" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_690x311.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_1035x466.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_1380x622.png 2x" data-dominant-color="141D2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-07 213538</span><span class="informations">1868×843 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Oh I see what happened, the image names are different, I don’t know how, given I pushed the latest at 11:51pm and submitted the form at 11:59pm. Thank You <a class="mention" href="/u/jivraj">@Jivraj</a> for showing me.<br>
Question: Now that I know. how can I test the container myself, if I want to do exactly what you guys are doing?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616713)

My code uses <code>npx</code> to format Markdown files using Prettier, specifically via <code>subprocess.run(["npx", "prettier@3.4.2", "--write", ...])</code>, which assumes that <code>npx</code> is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or <code>npx</code>, this results in an error during evaluation.
To test the functionality correctly, <code>npx</code> must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:
bash:<code> apt-get update &amp;&amp; apt-get install -y nodejs npm</code>
Once installed, <code>npx prettier@3.4.2</code> should work as expected.
For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where <code>npx</code> is available by default.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616718)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Before the project evaluation, I ran the test script and successfully passed all Task A and Task B checks. I also built the Docker image as required.<br>
But, when you gus evaluated , I get the following error:docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: “uvicorn”: executable file not found in $PATH: unknown.<br>
Could you please help me understand why this is happening even though the evaluation script ran fine?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2.png" data-download-href="/uploads/short-url/mnzjuzbggtgmEioNaqAmglPuNii.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_690x308.png" alt="image" data-base62-sha1="mnzjuzbggtgmEioNaqAmglPuNii" width="690" height="308" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_690x308.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_1035x462.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_1380x616.png 2x" data-dominant-color="ECF1F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1591×712 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58.png" data-download-href="/uploads/short-url/46C14tdqZzBLJXFGMHfybZu3hK8.png?dl=1" title="Screenshot 2025-04-07 192419" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_690x341.png" alt="Screenshot 2025-04-07 192419" data-base62-sha1="46C14tdqZzBLJXFGMHfybZu3hK8" width="690" height="341" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_690x341.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_1035x511.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_1380x682.png 2x" data-dominant-color="F6F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-07 192419</span><span class="informations">1534×760 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616726)

Can you tell me what application is this (FastAPI) one ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616741)

idk why i am doing this but this is my last request (for evaluation) with proofs. me and my friend both have same docker file code with missing flask dependency (i will try as much to not reveal his id/name) he got 12/20 even tough i tried same methods given by you and same error popped up flask module not found in his case but you gave him 12/20 marks but for me you gave 0? did i done something wrong? I know in industry level it matters much but right now we are students and for us CGPA matters. i am also uploading his docker file image and mine with 0 commits after 18th feb.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7.png" data-download-href="/uploads/short-url/hfGGrCZc5ujQNmm1RFe8BSzkevt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_690x377.png" alt="image" data-base62-sha1="hfGGrCZc5ujQNmm1RFe8BSzkevt" width="690" height="377" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_690x377.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_1035x565.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_1380x754.png 2x" data-dominant-color="13171D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1670×914 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70.png" data-download-href="/uploads/short-url/6R7JPTABdp08gdr9D0UZsdUIota.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70_2_690x468.png" alt="image" data-base62-sha1="6R7JPTABdp08gdr9D0UZsdUIota" width="690" height="468" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70_2_690x468.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70_2_1035x702.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70.png 2x" data-dominant-color="12161C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1376×935 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616767)

Dear Sirs,<br>
<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> <a class="mention" href="/u/carlton">@carlton</a>
As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png" data-download-href="/uploads/short-url/hCTkBDgDY5RETIdMAkhDpLOtTex.png?dl=1" title="Screenshot 2025-04-07 233513" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png" alt="Screenshot 2025-04-07 233513" data-base62-sha1="hCTkBDgDY5RETIdMAkhDpLOtTex" width="690" height="168" data-dominant-color="39444A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-07 233513</span><span class="informations">805×197 9.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<strong>Github repo submitted:</strong> <a href="https://github.com/wasimansari-iitm/Project-AI-Agent" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wasimansari-iitm/Project-AI-Agent</a><br>
<strong>Docker repo submitted:</strong> wasimansariiitm/my-ai-agent
The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the <code>app.py</code> file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.
I would like to respectfully bring this to your kind attention that the <code>app.py</code> file does exist in the repository, but it is located inside a subfolder:<br>
<a href="https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py" rel="noopener nofollow ugc">https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py</a>.<br>
But as per the submission instructions, I provided the GitHub repo link only: <a href="https://github.com/wasimansari-iitm/Project-AI-Agent" rel="noopener nofollow ugc">https://github.com/wasimansari-iitm/Project-AI-Agent</a>.
Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.
I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.
Thank You and Regards,
24ds3000090

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616782)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png" data-download-href="/uploads/short-url/nuja8ivRzao9XSmkZlLA9RYFAsP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png" alt="image" data-base62-sha1="nuja8ivRzao9XSmkZlLA9RYFAsP" width="690" height="455" data-dominant-color="313131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1298×857 29.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.
Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…<br>
But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.
Edit 2:<br>
Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png" data-download-href="/uploads/short-url/dDIQy9HZw7zCPuZ0utgGoCbXRkM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png" alt="image" data-base62-sha1="dDIQy9HZw7zCPuZ0utgGoCbXRkM" width="690" height="342" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1027×510 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.
Thank you.<br>
Regards,<br>
Shivaditya

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616788)

Hi Haricharan
Your Dockerfile does not build the repo. Its misconfigured.<br>
This is the error when building it:
<pre><code class="lang-auto">=&gt; ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 &gt; [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | &gt;&gt;&gt; COPY .env /app/
  21 |     
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png" data-download-href="/uploads/short-url/iWIIlgMm6iiSN3X2eus14cfi7sL.png?dl=1" title="Screenshot 2025-04-08 at 11.12.18 am"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png" alt="Screenshot 2025-04-08 at 11.12.18 am" data-base62-sha1="iWIIlgMm6iiSN3X2eus14cfi7sL" width="690" height="276" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png 2x" data-dominant-color="2E2C2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-08 at 11.12.18 am</span><span class="informations">754×302 41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
This is because if you look at your Dockerfile .env does not exist in your repo.<br>
Therefore it does not build.<br>
Your docker is supposed to take the AIPROXY token from our environment not from yours.<br>
This is passed dynamically at runtime of the Docker.
Since it fails to build, we cannot evaluate it.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616843)

Your docker failed to build from your Dockerfile
<pre><code class="lang-auto"> =&gt; ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 &gt; [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |     
  24 |     # Verify uv installation
  25 | &gt;&gt;&gt; RUN uv --version
  26 |     
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127
</code></pre>
Since we cannot build your docker from your Docker manifest file we cannot evaluate it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616847)

Your container failed to run after building it.
<pre><code class="lang-auto">docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "uv": executable file not found in $PATH: unknown
</code></pre>
Thats why we cannot evaluate it.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616853)

There is <strong>clearly</strong> <em>some difference</em> between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in &lt;module&gt;
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "&lt;frozen importlib._bootstrap&gt;", line 1387, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1360, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 1331, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 935, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in &lt;module&gt;
    from tasksB import *
  File "/app/tasksB.py", line 83, in &lt;module&gt;
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'
</code></pre>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616862)

Noted your concerns wrt Edit 1 and Edit 2 (and datagen.py running latest python version): Will raise it with <a class="mention" href="/u/s.anand">@s.anand</a> during our Wednesday meeting. Once we have an update, we will inform you of the outcome.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616864)

Hi,
Please let me know the reason on why I have not got any bonus marks.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png" data-download-href="/uploads/short-url/nv2LBjsOTgW23fOi7uzcT0M7EJB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png" alt="image" data-base62-sha1="nv2LBjsOTgW23fOi7uzcT0M7EJB" width="690" height="358" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1310×681 14.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387.png" data-download-href="/uploads/short-url/9eQ4I5cTYsRk40DEwPf2mOjX67B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_690x297.png" alt="image" data-base62-sha1="9eQ4I5cTYsRk40DEwPf2mOjX67B" width="690" height="297" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_690x297.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_1035x445.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_1380x594.png 2x" data-dominant-color="F9FAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1696×732 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616924)

We used some internal parameters with weights to auto calculate the bonus. Unless your submission met that threshold of 0.5 after scaling you would not get any bonus. Your score was normalised so instead of 3 you got 4 (3.75 got rounded up). But the metrics used to evaluate the quality of your submission only scored you at 0.007 which is far below the threshold required to get a bonus.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/616935)

Respected Sir,
<ul>
<li>Yes Sir, I said the same,  <code>.env</code> was not able to be uploaded to repo as .env file was not allowed to be uploaded</li>
<li>when we download the repository it doesn’t have the <code>.env</code> file,</li>
<li>for docker image to build we need to add <code>.env</code> with <code>AIPROXY_TOKEN</code></li>
<li>after that docker image will build, I had given about this in previous message</li>
<li>As you said Sir that you will use separate <code>AIPROXY_TOKEN</code>…you can put that in <code>.env</code> file and build the docker image</li>
<li>after that Sir its optional to pass <code>AIPROXY_TOKEN</code> again while running the docker Image</li>
<li>just the <code>.env</code> file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable</li>
</ul>
and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:
<pre><code class="lang-auto">git clone https://github.com/23f2001390/llmagent.git
</code></pre>
adding <code>.env</code> with AIPROXY token and replacing <code>evaluate.py</code> and <code>datagen.py</code> with new ones according to test environment
<pre><code class="lang-auto">docker build -t llm-agent .
</code></pre>
<pre><code class="lang-auto">docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent
</code></pre>
and in another terminal
<pre><code class="lang-auto">uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000
</code></pre>
Thank you<br>
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617017)

Respected sir<br>
I understand it’s my mistake sir and I apologize for that sir, but please consider this time sir since because of this my entire project score went from 9/20 to 0, which would make me difficult to pass this course and continue my diploma.<br>
Please consider this request sir, sorry sir and this would never be repeated in future. My project evaluation was 9/20 initially sir, but later it came down to 0 because of this issue. Kindly consider sir please.
Regards,<br>
S Sharmile<br>
23f3001688

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617039)

Thanks for relentless efforts <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>
I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..
Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of  my office environment,
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png" data-download-href="/uploads/short-url/o73Mf3a72M2sl5QitGxzibKmytv.png?dl=1" title="image (18)" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png" alt="image (18)" data-base62-sha1="o73Mf3a72M2sl5QitGxzibKmytv" width="690" height="363" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_1035x544.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png 2x" data-dominant-color="D7D4DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (18)</span><span class="informations">1272×671 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
build output
<pre><code class="lang-auto">#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update &amp;&amp; apt-get install -y --no-install-recommends curl ca-certificates &amp;&amp;     apt-get clean &amp;&amp; rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done
</code></pre>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59.png" data-download-href="/uploads/short-url/qolXTUtpETES0uyBNNmc1hh6Lj3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png" alt="image" data-base62-sha1="qolXTUtpETES0uyBNNmc1hh6Lj3" width="690" height="54" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_1035x81.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_1380x108.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1480×117 9.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617096)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4.png" data-download-href="/uploads/short-url/r1GvMyIqZObTda5HTCebIAACpSs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_690x387.png" alt="image" data-base62-sha1="r1GvMyIqZObTda5HTCebIAACpSs" width="690" height="387" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_690x387.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_1035x580.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_1380x774.png 2x" data-dominant-color="141619"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1079 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
<aside class="quote group-ds-students" data-username="22f3002723" data-post="442" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png" class="avatar"> 22f3002723:</div>
<blockquote>
Was the latest docker file used from git lab
</blockquote>
</aside>
No, we are not allowing any changes to repo after deadline, this is consistent rule for every student. We pulled your github repo latest commit before 18th feb, I am getting following error.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617127)

follow the steps mentioned in post below <img src="https://emoji.discourse-cdn.com/google/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">
<a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617129)

<aside class="quote group-ds-students" data-username="23F300327" data-post="427" data-topic="171141">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png" class="avatar"> 23F300327:</div>
<blockquote>
To test the functionality correctly, <code>npx</code> must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:
</blockquote>
</aside>
That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617130)

Thanks <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
As mentioned earlier, the pre Feb 18 dockerFile commited in GIT had  my office proxy url’s set as http_proxy and https_proxy.. It worked in my office envuironment and i tested everything in my office environment but based on the results which came on March last week realised that the proxies were preventing the uv to be installed in other environments.
Post that realised we have cloud based "docker playground’ utility where docker builds can be tested agonistic of any environment.. The good thing with playground is our instances last for only 3 hrs and next day we try we are kind of gauranteed of fresh environment without any caches,
Now after March 30th checkin validated the same in docker playground and ensured that the image got tagged and createdd successfully..
It would be great if the March 30th checkin could be considered, Again appreciate all your help so far.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617234)

<strong>Subject:</strong> Request for Verification of Dockerfile and Reevaluation of Marks for Project 1<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir,<br>
Regarding the recent feedback on <strong>Project 1</strong> for <strong>TDS</strong>, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named <strong><code>dockerfile</code></strong> (not <strong><code>Dockerfile</code></strong>). Please verify the repository again with this in mind.
Additionally, my Docker image architecture is <em>linux/amd64</em> (64-bit <strong>x86</strong>). I have also filled out the <strong>Architecture Information Collector</strong> form as requested.
<strong>Pre-requisites check: (1 for pass, 0 for fail)</strong><br>
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1<br>
Github repo exists and is public (should have a timestamp before 18th of Feb): 1<br>
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1<br>
Gihub repo check - Dockerfile exists: 0<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f.png" data-download-href="/uploads/short-url/xwamdoQkYPFDWm0tz2ZcixQ6iXJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_690x368.png" alt="image" data-base62-sha1="xwamdoQkYPFDWm0tz2ZcixQ6iXJ" width="690" height="368" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_690x368.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_1035x552.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_1380x736.png 2x" data-dominant-color="E6E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×1021 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Here’s the link to my GitHub repository:<aside class="onebox githubrepo" data-onebox-src="https://github.com/23f1001822/Task_agent_api">
  <header class="source">

      <a href="https://github.com/23f1001822/Task_agent_api" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/8/d83b83eaf69931596b2cddbbfea39884f17e047a_2_690x344.png" class="thumbnail" data-dominant-color="EDF0F3">

  <h3><a href="https://github.com/23f1001822/Task_agent_api" target="_blank" rel="noopener nofollow ugc">GitHub - 23f1001822/task_agent_api</a></h3>

    <span class="github-repo-description">Contribute to 23f1001822/task_agent_api development by creating an account on GitHub.</span>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<strong>Docker repo submitted:</strong> <em>sakshamumate/task_agent_api</em>
I kindly request a <strong>reevaluation of my project marks</strong> based on these clarifications.
Thank you for your attention to this matter. Please let me know if you need any further information or clarification.
Best regards,<br>
Saksham Umate ,<br>
23f1001822@ds.study.iitm.ac.in

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617273)

Sir, I had posted the query on A8 and datagen exception. Is this a reply to that?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617292)

oh yeah sorry, hit the reply to the wrong button, but yes its to your post.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617294)

I’ve got good news for you and 30 other students. Thanks to your diligent debugging effort that we were able to find this bug. For now the fix is that we will not evaluate you on a8 and catch the datagen exception so as to not cause cascading failures.
Thanks and kind regards.<br>
We will let you know the outcome of the evaluations soon.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617296)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
any way out for my earlier query ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617576)

<a class="mention" href="/u/carlton">@carlton</a><br>
Thank you for the reply .But it was working when i ran the initial evalaute.py .If you don’t  mind could you tell what may have caused this to happen.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617594)

Hi Hilal,
You have to recreate the test environment as shown in this post
<aside class="quote quote-modified" data-post="316" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.…
  </blockquote>
</aside>

That way you will be able to identify why the error was occuring.
The specific error itself means:<br>
Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.
If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/617664)

sir for my project 1 i got a mail stating that the docker file isn’t public and that’s why prerequisite failed. but i checked it and it seemed absolutely perfect to me. Please look into this issue as my docker repo is public and absolutely as per the requirement.  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618023)

Hi <a class="mention" href="/u/22f3003083">@22f3003083</a>
Following was your submission, which is not a valid dockerrepo.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6.png" data-download-href="/uploads/short-url/tzymtAyX9jKKvQKR6pxbORjcMES.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_690x94.png" alt="image" data-base62-sha1="tzymtAyX9jKKvQKR6pxbORjcMES" width="690" height="94" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_690x94.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_1035x141.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_1380x188.png 2x" data-dominant-color="191E25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1829×251 22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618030)

Now I feel so good getting 0.<br>
0 is best.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618032)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
As requested earlier, Could you please reevaluate my submission.  The only change that had to be done post Feb 18 checkin was to remove my office proxies on Mar 30 from the docker file  to make it work in all environments.. It  would be great if this could be accomodated..

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618061)

Hi Jayaram,
Unfortunately, we are not able to relax restrictions on changes to your repo, regardless of the reason. We have kept this rule uniform for everyone. If we allow this change, then everyone has a legitimate reason to request changes and would make the rule meaningless because then everyone will be able to make corrections to their submission. We do not even allow spelling changes.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618117)

Thanks for the response <a class="mention" href="/u/carlton">@carlton</a> ..  just a small suggestion, to avoid scenarios like what i faced and also with softwares like docker/podman not being too windows friendly, i think students can find it easier if a dev/mock  linux env is provided for course term duration, instead of   everyone having to figuring out with AWS/Azure and all providers.. Anyway thanks and appreciate all the help

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618125)

Sir, I have done everything for my project, but I am getting zero. I have uploaded my Docker file, but the email says it is not public. Sir, this is affecting my grades — please help me out. <a class="mention" href="/u/carlton">@Carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618204)

These are your project 1 responses,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c.png" data-download-href="/uploads/short-url/nRxJMiuYj88WV3hfVjfdjtzAJ8o.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_690x115.png" alt="image" data-base62-sha1="nRxJMiuYj88WV3hfVjfdjtzAJ8o" width="690" height="115" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_690x115.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_1035x172.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_1380x230.png 2x" data-dominant-color="191E25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1737×291 23.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
We are considering latest submission which have docker repo <code>maheshsingh01/tdsrepos </code><br>
which is not accessible publically.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782.png" data-download-href="/uploads/short-url/3k707SsLTwpU5fIttlYi4yib67M.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_690x350.png" alt="image" data-base62-sha1="3k707SsLTwpU5fIttlYi4yib67M" width="690" height="350" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_690x350.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_1035x525.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_1380x700.png 2x" data-dominant-color="154161"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1866×949 92.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618203)

Sir, could you please check it once more? I think the issue has been resolved. <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618225)

Since repo was not public during evaluation, we won’t be rechecking, or reevaluating.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618231)

<a class="mention" href="/u/jivraj">@Jivraj</a> I’ve completed all the required steps, but I’m still getting 0, It was working fine before. Could you please help me identify what might be going wrong?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618301)

Hi <a class="mention" href="/u/21f3003107">@21f3003107</a>
You need to look it up yourself, We have sent out evaluation log and docker log files, check those out.<br>
Evaluation script and other scripts that we have used are there in github repository over here.<br>
<a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1">Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA</a><br>
If there is some mistake from our end let us know about it.
To replicate test environment follow steps provided below.
<a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316">Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618314)

<a class="mention" href="/u/carlton">@carlton</a> Requested sir<br>
This is to request that in my evaluation a got 0 cause of the use of lowercase d instead of uppercase D but I have already submitted the  docker file in my git hub repo also.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5.jpeg" data-download-href="/uploads/short-url/2IJDQs92yWcHMcrAkae5moo7fcV.jpeg?dl=1" title="WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5_2_627x500.jpeg" alt="WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5" data-base62-sha1="2IJDQs92yWcHMcrAkae5moo7fcV" width="627" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5_2_627x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5.jpeg 2x" data-dominant-color="12151D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5</span><span class="informations">912×727 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618359)

<a class="mention" href="/u/carlton">@carlton</a><br>
Thank you i found my mistake in my docker file i wrote  this  CMD [“uv”, “run”, “app.py”]  instead of<br>
CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618525)

Sir my repo was public

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618965)

Sir any news on this? Did my score increase at all? My dashboard still shows the old score.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/618997)

<a class="mention" href="/u/carlton">@carlton</a> sir, my project 1 marks have still not increased even though while during evaluation it shows 4/10 for the task 1. It was said that the docker image prerequisite will be removed and without that the evaluation would be done, but there is still no change in my marks. please look into it once, as my dashboard currently reflects 0 for project 1.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/619160)

These evals are being handled separately. They have not yet been completed. Kindly bear with us till they are complete.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/619360)

Same here <a class="mention" href="/u/carlton">@carlton</a> in my evaluation logs i have scored 10 while marks being reflected are not the same neither on mail nor on site

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/619619)

I looked at your evaluation logs and it says 1 score instead of 10.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/619655)

Good evening!<br>
<a href="/uploads/short-url/30ijyIo5UiUUEVvnPZklfYVY2mI.jpeg">1000092114|690x198</a>
I am writing to you to request you please relook into the evaluation.
The docker image which I share is working at my end.  The size of the image is 6 GB which may take more than 5 minutes to load as I wasn’t aware of the infra level restrictions.
I request you to kindly consider my request and please re-evaluate the assignment as I have contributed a lot of effort into it.
Thanks,<br>
Garima

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620018)

Sir, so will my score get updated because now it is marked as 0.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620556)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Sir,<br>
I am Saksham Umate and my project 1 was to be re-evaluation because of docker file not found in root ,but it was their so you had given me confirmation that it will re-evaluate after end term. I had already shared my docker file systems configuration at docker hub
So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it
Tell me if any information is needed about project from my side<br>
Thank you!
Best regards,<br>
Saksham
My docker repo details in previous post:<aside class="quote quote-modified" data-post="447" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…
  </blockquote>
</aside>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d.jpeg" data-download-href="/uploads/short-url/94gdAia3CpfNm8OXPu04KY1yckR.jpeg?dl=1" title="IMG_20250417_114002" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_259x500.jpeg" alt="IMG_20250417_114002" data-base62-sha1="94gdAia3CpfNm8OXPu04KY1yckR" width="259" height="500" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_259x500.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_388x750.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_518x1000.jpeg 2x" data-dominant-color="E5E3E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20250417_114002</span><span class="informations">1080×2083 469 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620587)

Evaluations are done for such cases where Dockerfile(with name of Dockerfile as <code>Dockerfile</code>) was present inside other folders than root folder of your github repo.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620590)

<a class="mention" href="/u/carlton">@carlton</a> sir, any info on outcome of <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451">this bug in P1 datagen.py</a> ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620595)

Did Mark’s are updated or being update for this students ?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620608)

Hi <a class="mention" href="/u/22f3000819">@22f3000819</a>
We had updated datagen.py(try block for task) which affected 30 students, but scores changed only for 4 students, for others it remained the same.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620628)

We will be pushing marks today.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620630)

I probably wasn’t 1 of the 4, right? Anyways thanks for paying attention to the matter.
Regards,<br>
Shivaditya

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620636)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
Respected Sir,
I hope you are doing well.<br>
This is with reference to your confirmation mail that my project 1 will be re-evaluated after end term<br>
I would like to sincerely apologize for the oversight in my Project 1 submission. Upon reviewing my GitHub repository, I realized that the file was named <code>dockerfile</code> (with a lowercase ‘d’) in the Github root repo instead of the required <code>Dockerfile</code> (with an uppercase ‘D’).
While the contents of the file were correct and my project passed several evaluation tests, I understand that the evaluation script could not detect the Dockerfile due to this naming issue. I genuinely did not intend to deviate from the standard, and I now fully understand the importance of following naming conventions precisely.
I humbly request you to kindly consider this as an honest mistake and allow a one-time exception, Please sir. This issue has unfortunately resulted in my project score being reduced to 0, which puts my overall course performance at risk. I assure you that I have learned from this experience and such an error will not occur again in the future.<br>
So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it.<br>
Thank you very much for your time and consideration.
Warm regards,<br>
S. Sharmile<br>
Roll No: 23f3001688

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/620829)

Sir, my marks still did not get updated, please help me in that regard.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/621017)

Hi Everyone,
We have sent the updated marks to Operations. At this time of the term they are very busy with lots of updates, so it will take time for them to push it to the dashboard. As soon as they inform us that the scores have been pushed, we will send out a discrepancy form if you find any issues with your score.
Thanks &amp; Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/621117)

Sir, my project 1 marks are still 0 even though I had passsd few cases. Please help me sir as my final score is coming as 69.8 , it will be very valuable for me if it crosses 70, please sir help me with this regard

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/621247)

<a class="mention" href="/u/carlton">@carlton</a><br>
Hi Sir,<br>
I hope you’re doing well. I just wanted to let you know that I put a lot of effort into completing <strong>Project1</strong>, but I accidentally named the <strong>Dockerfile</strong> as <code>dockerfile</code> (with a lowercase ‘d’).<br>
Could you please consider evaluating it with that name? I’d really appreciate it.<br>
Thank you!<br>
My discourse post for more information:<aside class="quote quote-modified" data-post="447" data-topic="171141">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png" class="avatar">
    <a href="https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447">Tds-official-Project1-discrepencies</a> <a class="badge-category__wrapper " href="/c/courses/tds-kb/34"><span data-category-id="34" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="9" data-drop-close="true" class="badge-category --has-parent" title="This category is created to address subject-specific queries related to Tools in Data Science"><span class="badge-category__name">Tools in Data Science</span></span></a>
  </div>
  <blockquote>
    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…
  </blockquote>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/621699)

