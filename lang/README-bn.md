<h1 align="center">&nbsp</br>পাইথনট'এ প্রাইভেট ফাংশন</br>Private Function in Python</br>&nbsp</h1>
<p align="center"><i>"পাইথনে প্রাইভেট ফাংশন তৈরি করার একটি স্মার্ট উপায়"</i><p>
  
<h2 align="center">from <a href="https://faheem41.github.io" target="_blank" rel="noreferrer">FAHEEM41</br></a></h2>
<a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/lang/README-bn.md#কিভাবে-কোড-ব্যবহার-করবেন-pip-ব্যবহার-করে" rel="noreferrer"><img src="https://img.shields.io/badge/pip-ডাউনলোড-purple" /></a>&nbsp&nbsp
<a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/README.md" rel="noreferrer"><img src="https://img.shields.io/badge/lang-English-black" /></a>

### 
------------------

<p>
  <ul>
    <li>সংস্করণ: <strong>১.৪.২২</strong></li>
    <li>প্রথম প্রকাশিত: <strong><a href="https://www.sololearn.com" target="_blank" rel="noreferrer">Sololearn</a></strong></li>
    <li>Github প্রথম প্রকাশের তারিখ: <strong>৮ শ্রাবণ ১৪২৯ বঙ্গাব্দ (23rd July, 2022)</strong></li>
    <li>সর্বশেষ সংষ্করণ: <strong>১৮ আশ্বিন ১৪২৯ বঙ্গাব্দ (3rd October, 2022)</strong>
  </ul>
</p>
</br>

<p>
<h2>কেন ব্যবহার করবেন?</h2>
প্রাইভেট ফাংশনের ধারণা দিয়ে শুরু করা যাক। প্রাইভেট ফাংশনগুলি এমন ফাংশন যা শুধুমাত্র ঘোষিত মডিউলের মধ্যে অ্যাক্সেসযোগ্য, অন্য কোনও মডিউল থেকে অন্য কোনও ফাংশন এটি অ্যাক্সেস করতে পারে না৷</br>
এই প্রকল্পটি প্রধানত একটি কোডের নিরাপত্তা সংক্রান্ত বিষয়গুলির উপর দৃষ্টি নিবদ্ধ করে। এটি অন্য মডিউলগুলি থেকে অন্য ফাংশনগুলি কোড অ্যাক্সেস সীমাবদ্ধ করার একট সক্ষমি উপায়। এটি নিশ্চিত করে যে শুধুমাত্র নন-প্রাইভেট ফাংশনগুলি অর্থাৎ পাবলিক ফাংশনগুলি কোডের বাইরে যে কোনও জায়গা থেকে অ্যাক্সেস করতে পারে।</br></br>
এখানে একটি উদাহরণ, ধরুন একটি মডিউলের দুটি ফাংশন আছে: <i>add()</i> এবং <i>main()</i>। <i>main()</i> ফাংশন মূল ফাংশন এবং অন্যান্য মডিউল থেকে কল করা যেতে পারে। অন্যদিকে, <i>add()</i> ফাংশন হল একটি ফাংশন যা শুধুমাত্র <i>main()</i> ফাংশন দ্বারা ডাকা হয়, এবং আমরা এই ফাংশনটিকে ব্যক্তিগত রাখতে চাই, অর্থাৎ নিশ্চিত করতে চাই যে এটি অন্য কোন মডিউল থেকে অ্যাক্সেস বা কল করা যাবে না।
</p>
</br>

<p>
<h2>কোড বুঝুন</h2>
এখানে আমরা আমাদের কাজ সম্পন্ন করার জন্য একটি খুব সহজ ধারণা বাস্তবায়ন করেছি। আমরা একটি <i>ডেকোরেটর</i> ব্যবহার করেছি যা ফাংশনটি একটি ব্প্রাইভেট বা সর্বজনীন ফাংশন কিনা তা পরীক্ষা করবে এবং এর ফলে যথাক্রমে অ্যাক্সেস অস্বীকার বা অনুমোদন করবে। <i>ডেকোরেটর</i> চলবে, যথারীতি, ফাংশন কলের সাথে, এবং ফাংশন চালানোর আগে।</br>
বিস্তারিত বোঝার জন্য, একটি লক্ষপাত করুন <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/src/privatefunc.py" rel="noreferrer">privatefunc.py</a> ফাইল; কোডের ডকুমেন্টেশন, কোডটি কীভাবে কাজ করে, সোর্স কোডের ভিতরে দেওয়া আছে।
</p>
</br>

<p>
<h2>কিভাবে কোড ব্যবহার করবেন?</h2>
<b>1.</b> <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/src/privatefunc.py" rel="noreferrer">privatefunc.py</a> আপনার রেপুসিেটরিতে কপি এবং পেস্ট করুন।</br>
<b>2.</b> আপনার মডিউলে <b>privatefunc.py</b> আমদানি করুন </br><code>from privatefunc import PrivateFunc</code>।</br>
<b>3.</b> তারপর তৈরি করুন, <code>privatefunc = PrivateFunc("nameOfThisModuleHere")</code>।</br>
<b>4.</b> এখন আপনি যে ফাংশনটিকে প্রাইভেট করতে চান তার আগে <code>@privatefunc.private</code> যোগ করুন।</br></br>
ভালভাবে বোঝার জন্য লক্ষপাত করুন <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/test/moduleWithPrivateFunc.py" rel="noreferrer">moduleWithPrivateFunc.py</a>।
</p>
</br>

## কিভাবে কোড ব্যবহার করবেন? (pip ব্যবহার করে)
টার্মিনালে কমান্ডটি টাইপ করুন:
```
pip install privatefunc
```
আপনার মডিউলে এই লাইনগুলো যোগ করুন:
```
from privatefunc import PrivateFunc
privatefunc = PrivateFunc("nameOfThisModuleWithoutExtension")
```

এখন আপনি যে ফাংশনটিকে প্রাইভেট করতে চান তার আগে `@privatefunc.private` যোগ করুন।</br></br>
সবকিছু একসাথে করে:
```
# example.py
from privatefunc import PrivateFunc
privatefunc = PrivateFunc("example")

@privatefunc.private
def privatedef():
  pass
```
ভালভাবে বোঝার জন্য লক্ষপাত করুন <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/test/moduleWithPrivateFunc.py" rel="noreferrer">moduleWithPrivateFunc.py।</a>

</br>

<p>
<h2>উদাহরণ কোড</h2>
উৎসের অন্তর্দৃষ্টি সম্পূর্ণরূপে বুঝতেে <a href="https://github.com/Faheem41/Private-Function-in-Python/tree/main/test" rel="noreferrer">ডেমো কোড</a> দেখুন।
</p>
</br>

#
-------------------
<h6 align="center">© 2021-2022 Md. Faheem Hossain fmhossain2941@gmail.com</h6>
