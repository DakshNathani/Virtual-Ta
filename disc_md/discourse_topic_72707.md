# Post No: 72707
# Queries regarding End Term exam solutions
**Topic Slug**: queries-regarding-end-term-exam-solutions
**Created At**: April 15, 2025 09:59:50

Hi <a class="mention" href="/u/carlton">@carlton</a> and <a class="mention" href="/u/jivraj">@Jivraj</a> sir,
I appeared for the end term examination held on 13th April 2025 during the FN shift. I would like to bring to your attention that the exam interface did not provide an option for multiple selections. However, a few questions appeared to have multiple correct answers.
I have noted down the specific questions and the corresponding options I believe to be correct.So, kindly review them and let me know if there were any errors in my understanding of the questions. The questions are as follows:
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8.jpeg" data-download-href="/uploads/short-url/A6rPaqEeHL4nw1GGBGp4tKdfWWs.jpeg?dl=1" title="1000042547" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_690x369.jpeg" alt="1000042547" data-base62-sha1="A6rPaqEeHL4nw1GGBGp4tKdfWWs" width="690" height="369" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_690x369.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_1035x553.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8.jpeg 2x" data-dominant-color="F0E8E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042547</span><span class="informations">1080×578 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Question 2: Fields needed to filter “POST requests under /images/ from 15:00 to 18:00 on Mondays”
To filter such logs, we need:
Time → for the hour and the day (Monday)<br>
Method → to filter POST<br>
URL → to filter /images/
So, the correct minimal set is:
<blockquote>
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Time, Method, URL
</blockquote>
Time → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
Method → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
URL → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
Referer → not needed, but not harmful
So this option includes all the necessary fields, just with one extra — which doesn’t invalidate it.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913.jpeg" data-download-href="/uploads/short-url/kBi3KxCTBUs9L4ifYXzDfQKdZRh.jpeg?dl=1" title="1000042548" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_690x192.jpeg" alt="1000042548" data-base62-sha1="kBi3KxCTBUs9L4ifYXzDfQKdZRh" width="690" height="192" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_690x192.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_1035x288.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913.jpeg 2x" data-dominant-color="F5F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042548</span><span class="informations">1080×301 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Acc to solutions only option 6406534159827 is valid:
Status is numeric (200)<br>
Method (GET), Protocol (HTTP/1.1), and URL (/index.html) are correct
All required fields are present and properly formatted
The other options were as follows:
9825 uses invalid protocol (INVALID)
9826 uses invalid status code (OK instead of numeric)
9824 has no critical issue — it is technically also valid (only uses a private IP 192.168.1.1, which is unusual but not invalid). So both 9824 and 9827 are valid, but the answer marked only 9827
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373.jpeg" data-download-href="/uploads/short-url/wzS0A3Uz9s9vYMNHAkB3yKh7cn.jpeg?dl=1" title="1000042545" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_690x299.jpeg" alt="1000042545" data-base62-sha1="wzS0A3Uz9s9vYMNHAkB3yKh7cn" width="690" height="299" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_690x299.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_1035x448.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373.jpeg 2x" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042545</span><span class="informations">1079×468 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Correct Answer(s):
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> PUT – Correct: It replaces the resource entirely. Multiple identical PUTs = same result.
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> GET – Also correct: It only fetches data, no side-effects. Multiple GETs = same result.
<img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> DELETE – Technically correct: Deleting the same resource multiple times has the same result as deleting once (resource stays deleted).
<hr>
Incorrect Answer:
<img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> POST – Not idempotent. Each POST usually creates a new resource or changes server state.
(This is the mistake on my part that I put the ans as POST as I thought since 3/4 are idempotent and one is not I should select the odd one out but I hope this could be resolved)
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/619552)

Agree &amp; second all thoughts shared by <a class="mention" href="/u/24f2003130">@24f2003130</a> above.
<ul>
<li>
I also wanted to clarify on this question on filtered entries. The question mentions that a list filtered_entries is being created , and with the way the question is structured it seems like the filtering conditions mentioned in the question have already been applied. In that case <code>len(filtered entries)</code> seems to be correct. However the right answer is marked ‘None of these’ .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0.png" data-download-href="/uploads/short-url/z5Qvydw8nYEYuIyQ5RZLKdwMgzS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_690x245.png" alt="image" data-base62-sha1="z5Qvydw8nYEYuIyQ5RZLKdwMgzS" width="690" height="245" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_690x245.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_1035x367.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0.png 2x" data-dominant-color="F2EFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1108×394 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</li>
<li>
The valid log entry had me stumped too, option 1 and 4 both look absolutely fine yet only option 4 is marked correct.
</li>
<li>
Also, only POST request is not idempotent, all other requests are idempotent yet only PUT is marked correct.
</li>
</ul>
Request you to please clarify and consider these points.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/619868)

Yes <a class="mention" href="/u/carlton">@carlton</a> the wording of the question made it seem like the filters were already applied on the list <code>filtered_entries</code>.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/619891)

<h1><a name="p-620130-clarifications-on-queries-1" class="anchor" href="#p-620130-clarifications-on-queries-1"></a>Clarifications on Queries</h1>
<ol>
<li>
<strong>Which of the following is a valid log entry based on the provided format?</strong><br>
Due to a technical issue in the portal, both options 1 and 4 are correct answers. The final scoring has been adjusted accordingly, and full marks will be awarded for either response.
</li>
<li>
<strong>HTTP method is idempotent</strong><br>
This question has been excluded from scoring as three methods (GET, PUT, and DELETE) are idempotent, with only POST being non-idempotent.
</li>
<li>
<strong>Entries with 404 status code</strong><br>
Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.
</li>
<li>
<strong>Which of the following fields are necessary to filter “POST requests made for pages under /images/ from 15:00 to 18:00 on Mondays”?</strong><br>
Option A (Time, Request, Method, URL) is correct because:
</li>
</ol>
<ul>
<li>Option B includes Size and Status, which aren’t needed for filtering by time, method, and URL</li>
<li>Option C includes Referer, which is unnecessary unless filtering by source page</li>
<li>Option D includes Status and Server, which aren’t relevant for this specific filtering requirement</li>
</ul>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620130)

Thank you for the clarification provided regarding Question 4 and resolution of errors in other questions. I understand the reasoning behind choosing Option A (Time, Request, Method, URL). However, I respectfully believe Option C (Time, Method, URL, Referer) is more accurate for the following reasons:
<ol>
<li>
Redundancy in Option A:<br>
The Request field already contains the HTTP method, URL, and protocol (e.g., “POST /images/logo.png HTTP/1.1”). Including both Request and separate Method and URL fields introduces redundancy. If we already extract Method and URL separately for filtering, the full Request field becomes unnecessary.
</li>
<li>
Simplicity in Filtering:<br>
Filtering for “POST requests under /images/” from 15:00 to 18:00 on Mondays can be done using:
</li>
</ol>
Time → for checking the hour and weekday.
Method → to filter only POST.
URL → to ensure the request is under /images/.
Thus, Option C (Time, Method, URL, Referer) already includes all needed fields. While Referer is not essential, it doesn’t interfere with the filtering and might be useful in future extended filtering cases (e.g., source tracking). Therefore, Option C is complete and accurate without being redundant.
<ol start="3">
<li>Consistency with Log Parsing Practices:<br>
In most log analysis scripts or systems (e.g., Python’s re or pandas parsing of logs), Method and URL are parsed from Request for separate use. This further supports the idea that including Request alongside Method and URL is not best practice.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620133)

Sir, regarding point 3, score-checker tells a different story. While all the other changes have been made with the same reflecting in the score, that question still says “The question and answer remain the same . No changes required”, which is different from your post.
<img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_690x31.png" alt="image" data-base62-sha1="9aSHAfq31r6LUlSOz4aOuDJd1s9" width="690" height="31" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_690x31.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_1035x46.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_1380x62.png 2x" data-dominant-color="EBEEF2"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/91a843fad0075c603424114af0cfca114941a304.png" data-download-href="/uploads/short-url/kMxJUqb03TNPiIf0e1wW5LmlOh6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/91a843fad0075c603424114af0cfca114941a304_2_690x263.png" alt="image" data-base62-sha1="kMxJUqb03TNPiIf0e1wW5LmlOh6" width="690" height="263" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/91a843fad0075c603424114af0cfca114941a304_2_690x263.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/91a843fad0075c603424114af0cfca114941a304.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/91a843fad0075c603424114af0cfca114941a304.png 2x" data-dominant-color="F2F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">923×352 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Can you please look into it?
Thanks<br>
Regards,<br>
Shivaditya

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620467)

<a class="mention" href="/u/iamprasna">@iamprasna</a> sir , the scores have been updated on the dashboard as well and the answer for the question in point 3 is still the same
Additionally , sir I have attached the snapshot of a dec’24 TDS PYQ which is a replica of this question and the answer for the same is mention the first option.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44.jpeg" data-download-href="/uploads/short-url/AbHSGMuXF9zvg4FybyCD4uGyueo.jpeg?dl=1" title="1000042796" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44_2_690x343.jpeg" alt="1000042796" data-base62-sha1="AbHSGMuXF9zvg4FybyCD4uGyueo" width="690" height="343" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44_2_690x343.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44_2_1035x514.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fda110de0ada74e60ba0e160ab21463c4ebdbd44.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042796</span><span class="informations">1080×538 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
The link for the same has been attached for your referance<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk">
  <header class="source">

      <a href="https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk" target="_blank" rel="noopener nofollow ugc">IIT M FOUNDATION DIPLOMA FN EXAM QDF2 22 Dec 2024.pdf</a></h3>

Google Drive file.

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620472)

That’s a great find. They’re the same question with just different parameters. Please look into it <a class="mention" href="/u/iamprasna">@iamprasna</a> sir.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620477)

<a class="mention" href="/u/carlton">@carlton</a> sir and <a class="mention" href="/u/jivraj">@Jivraj</a> sir please look into this question and clarify this
Thank you

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620539)

Hi,<br>
From where are you checking the transcripts? I’m not able to see the answer transcripts in the score checker app.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f.png" data-download-href="/uploads/short-url/8KxftzhVAR7hdIl6XyT5lEFAL6v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f_2_690x226.png" alt="image" data-base62-sha1="8KxftzhVAR7hdIl6XyT5lEFAL6v" width="690" height="226" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f_2_690x226.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f_2_1035x339.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3d54127deb9243fce2a75dace8f4b52f14f9057f_2_1380x452.png 2x" data-dominant-color="CBD2D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1891×622 31.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620540)

Click on the eye button …then you will be able to view your transcript

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620544)

Thanks for the reply, but I only see the question id’s and answer id’s, not able to find the transcripts.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a.png" data-download-href="/uploads/short-url/zl48WsOV7M3b9v0o3ZveMo6b6ye.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a_2_690x341.png" alt="image" data-base62-sha1="zl48WsOV7M3b9v0o3ZveMo6b6ye" width="690" height="341" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a_2_690x341.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a_2_1035x511.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7adba30daf6dbdfda4884a7b821a593557a466a_2_1380x682.png 2x" data-dominant-color="E0E3CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×923 94.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620546)

It seems that the option to download the answer key has been removed. However, you could consider reaching out to someone in the group or checking the dashboard for  solution pdf of question paper. You can then match the questions in order, even if the IDs don’t align exactly—it should still give you a general idea. From there, you can proceed accordingly.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/620547)

<a class="mention" href="/u/iamprasna">@iamprasna</a> <a class="mention" href="/u/carlton">@carlton</a> Please look into it once. According to point 3 of <a class="mention" href="/u/iamprasna">@iamprasna</a>’s post, I should get full credit for that question and it will take me to a perfect 100 score in ET from the current 97. I brought this into attention before the scores were pushed to the dashboard.
Regards,<br>
Shivaditya

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/621044)

The correction has been done to the following question for both the FN and AN sessions. You must be able to see the change in scores shortly
<ol>
<li><strong>Entries with 404 status code</strong><br>
Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.</li>
</ol>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/621914)

Thank you sir for acknowledging our requests and resolving the error

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/621957)

