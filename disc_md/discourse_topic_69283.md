# Post No: 69283
# Graded assignment 6
**Topic Slug**: graded-assignment-6
**Created At**: March 06, 2025 13:48:38

Please post any questions related to <a href="https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&amp;type=assignment&amp;tab=courses&amp;unitId=23">Graded Assignment 6 - Data Analysis</a>
Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.
Deadline <span class="discourse-local-date" data-date="2025-03-16" data-email-preview="2025-03-15T18:30:00Z UTC" data-timezone="Asia/Calcutta">2025-03-15T18:30:00Z</span>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/603963)



[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/603964)

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?
<a class="mention" href="/u/carlton">@carlton</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/603966)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
I have similar concern<br>
For Q1, I used the following code:
<pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')
</code></pre>
And got the following output:
<pre><code class="lang-auto">Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04
</code></pre>
Whereas options are below where none of them are correct.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" data-download-href="/uploads/short-url/nPaaIWtriJMunrro5mxPkkzgs0I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" alt="image" data-base62-sha1="nPaaIWtriJMunrro5mxPkkzgs0I" width="281" height="219"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">281×219 9.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Whereas for Q2 (Punjab and Yamaha) I used the following code:
<pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') &amp; (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')
</code></pre>
and got the following answers:
<pre><code class="lang-auto">Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08
</code></pre>
The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" data-download-href="/uploads/short-url/bEEgmsyChZ5YyAlqcLdD1S91PE2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" alt="image" data-base62-sha1="bEEgmsyChZ5YyAlqcLdD1S91PE2" width="278" height="216"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">278×216 9.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/602355)

<a class="mention" href="/u/24f2006061">@24f2006061</a> We are looking into it. We will update based on our analysis. Thanks for letting us know.
Kind regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/603367)

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630.png" data-download-href="/uploads/short-url/qYtCOu4iFTJRgTpq1aybIwZqRVe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png" alt="image" data-base62-sha1="qYtCOu4iFTJRgTpq1aybIwZqRVe" width="690" height="131" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_1035x196.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_1380x262.png 2x" data-dominant-color="FAF9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1383×263 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/603970)

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/604313)

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 &amp; Q2, but both these questions are single-choice questions. Kindly look into it and help us out <a class="mention" href="/u/carlton">@carlton</a> !

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/604590)

I guess for both Q1 &amp; Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605292)

Any updates on these? I am too facing the same issue.
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605551)

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04.png" data-download-href="/uploads/short-url/A4m6gPBqXgQhJ3fsG8iEiLd5pKQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png" alt="image" data-base62-sha1="A4m6gPBqXgQhJ3fsG8iEiLd5pKQ" width="690" height="190" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_1035x285.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_1380x380.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2083×575 47.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605753)

Kindly update us regarding the status of Q1 &amp; Q2 <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605798)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Dear TDS Team,
There are multiple issues in Graded Assignment 6 that require urgent attention:
<ol>
<li>Questions 1 and 2, along with their options, are ambiguous.</li>
<li>In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.</li>
<li>The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.</li>
</ol>
The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.
Thank you for your support.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605954)

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.
For instance:
<blockquote>
forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.
</blockquote>
but is this talking about the average resale value as no input features are specified?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/605995)

Let’s wait for their response.<br>
I submitted nearby option for Q3 and Q4

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606007)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).<br>
Thanks

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606017)

Hi <span class="mention">@all</span>
Question intends you to select most correlated one.<br>
Select option which is absolute highest.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606228)

<a class="mention" href="/u/jivraj">@Jivraj</a>  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.<br>
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) &amp; Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606558)

<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png" data-download-href="/uploads/short-url/lrXmd4rKqCvHw9vxjDwssxhuPML.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png" alt="image" data-base62-sha1="lrXmd4rKqCvHw9vxjDwssxhuPML" width="690" height="197" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_1035x295.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1318×377 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
what to do if 3 options have same value -0.04 and all are correct?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606603)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
My question 7 for GA6 is :<br>
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) &amp; Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance<br>
Whose options provided are :<br>
10418 meters
12287 meters
10965 meters
11149 meters
However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)
I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)<br>
Kindly look into the question, and let me know about the same (the destination from central command post)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606761)

Have you succeeded in running the shape file for Q10? It seems to have some error.
<a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606802)

No,<br>
I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606808)

I  downloaded the complete shape file zip from the <a href="http://census.gov" rel="noopener nofollow ugc">census.gov</a> site.<br>
Here is the link: <a href="https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip" rel="noopener nofollow ugc">https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip</a>
It works fine in QGIS.<br>
<a class="mention" href="/u/lakshaygarg654">@lakshaygarg654</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606825)

they have not provide all the files needed to read that shp file in the question .<br>
but your link includes them. thanks…

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606854)

I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.<br>
Thanks for sharing.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/606897)

My question 9 for GA6 is :<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png" data-download-href="/uploads/short-url/mAux9PF93ZPiL5yWJIHJbWOBS6B.png?dl=1" title="Screenshot 2025-03-15 205444" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png" alt="Screenshot 2025-03-15 205444" data-base62-sha1="mAux9PF93ZPiL5yWJIHJbWOBS6B" width="657" height="500" data-dominant-color="EBECEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-15 205444</span><span class="informations">878×668 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902.png" data-download-href="/uploads/short-url/90Bt4FXPELiOL7vTo120QRInE.png?dl=1" title="Screenshot 2025-03-15 205456" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_690x189.png" alt="Screenshot 2025-03-15 205456" data-base62-sha1="90Bt4FXPELiOL7vTo120QRInE" width="690" height="189" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_690x189.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_1035x283.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-15 205456</span><span class="informations">1333×366 45.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
I solved it in colab but options are getting mismatched there…kindly clarify this issue..

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607050)

for the above question the options are None of these are matching and answer is around 11.5 kms<br>
3848 meters<br>
6265 meters<br>
4110 meters<br>
5106 meters

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607057)

For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are<br>
6069 meters<br>
7687 meters<br>
6106 meters<br>
7035 meters<br>
<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607119)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a>
for question 4, i have tried <code>=forecast</code> and also <code>=forecast.ets</code>, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.
for question 7, none of the options match. I am selecting the <code>MOST ACCURATE</code> among the given options. Hope, it is correct

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607151)

Can anyone help me out on how to approach and solve the 10th question please!?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607211)

Check the distances of other locations from the central location. One student found <strong>Question 7</strong> of the <strong>GA6 Option Set</strong> based on the distances of other points, which do not match the requirements of Question 7.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607252)

i have the same issue

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607272)

yes i have the same issue<br>
and i got the same answer and am give the same options<br>
<a class="mention" href="/u/carlton">@carlton</a> sir what to do?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607273)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are<br>
6069 meters<br>
7687 meters<br>
6106 meters<br>
7035 meters

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607277)

Hello Sir,
Can you please check if this is the right answer. As per email received from <a class="mention" href="/u/carlton">@carlton</a> sir we should select the absolute maximum value.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa.png" data-download-href="/uploads/short-url/pJYoCCd8RUifNVz5EQEN3nd6bXQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa_2_690x277.png" alt="image" data-base62-sha1="pJYoCCd8RUifNVz5EQEN3nd6bXQ" width="690" height="277" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa_2_690x277.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">978×393 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.
For the first question the correlation matrix is as follows,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc.png" data-download-href="/uploads/short-url/s80SERWXLf5h1F6b2sPPUE8anfK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc_2_690x397.png" alt="image" data-base62-sha1="s80SERWXLf5h1F6b2sPPUE8anfK" width="690" height="397" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc_2_690x397.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc.png 2x" data-dominant-color="C3BBE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">748×431 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
So shouldn’t it be -0.13?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607316)

Thanks for the colour picture.<br>
If you read the aforementioned email…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83.png" data-download-href="/uploads/short-url/ykRYf68vCg80lpXIVoLIi3LOTxF.png?dl=1" title="Screenshot 2025-03-17 at 9.09.55 am"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_690x247.png" alt="Screenshot 2025-03-17 at 9.09.55 am" data-base62-sha1="ykRYf68vCg80lpXIVoLIi3LOTxF" width="690" height="247" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_690x247.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_1035x370.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_1380x494.png 2x" data-dominant-color="F6F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-17 at 9.09.55 am</span><span class="informations">1760×632 65.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
Kind regards (in colour <img src="https://emoji.discourse-cdn.com/google/wink.png?v=14" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20">)

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/607333)

Thank you sir. i have got questions 1 and 2 both marked as 0.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f.png" data-download-href="/uploads/short-url/lBf64UZa2qvheoQRCs5jwb7qv4X.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f_2_690x329.png" alt="image" data-base62-sha1="lBf64UZa2qvheoQRCs5jwb7qv4X" width="690" height="329" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f_2_690x329.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×459 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.<br>
I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.
|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||<br>
-0.026685695
|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||<br>
0.003953219
|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||<br>
-0.010839295
|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||<br>
0.029128825
|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||<br>
0.013019585
|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||<br>
-0.056866212

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/608219)

<a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a><br>
Dear sirs,<br>
I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845.png" data-download-href="/uploads/short-url/Aps1xCBnODq52FkirYERHqrI0Jf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845_2_690x390.png" alt="image" data-base62-sha1="Aps1xCBnODq52FkirYERHqrI0Jf" width="690" height="390" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845_2_690x390.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">935×529 40.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/608222)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect
My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) &amp; Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance
10418 meters
12287 meters
10965 meters
11149 meters
Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)
Also, my question 4 was :<br>
As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.
134483
94774
150666
199711
Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect
So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)
Kindly look into it
Thanks and Regards

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/608561)

<a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.
<div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d.png" data-download-href="/uploads/short-url/hWqmlQlqzKAsjVaXT6VqH3FshEF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_690x250.png" alt="image" data-base62-sha1="hWqmlQlqzKAsjVaXT6VqH3FshEF" width="690" height="250" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_690x250.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_1035x375.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d.png 2x" data-dominant-color="FCFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1227×446 24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/608883)

<span class="mention">@all</span><br>
we are looking into problems with question 4, 6 and 10.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/609762)

Hi,
Have the corrections been done on GA6 marks?

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/618164)

Yes, corrections have been done in Ga6 marks.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/618197)

Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

[Link to Post](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/618321)

