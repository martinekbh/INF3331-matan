# -*- coding: utf-8 -*-:w
import re
from urllib import urlopen

def find_urls(text):
    """
    Looks for and returns urls from a string of HTML.
    A url is here assumed to be of the form 
        <a href="PROTOCOL://www.HOST.DOMAIN/PATH"></a>
    where PROTOCOL is either http or https, HOST and DOMAIN consists of [a-zA-z0-9~.-] chars,
    and PATH consists of [a-zA-z0-9~./-] chars. The "www" part of the url is optional, so the
    search-function does not specify that this has to be in the url (if it is, it will be part
    of the HOST string). HOST and DOMAIN have to be at least one char long, while PATH can be
    empty.
    """

    #For "" quotations
    urls = re.findall(r"<a href=\"(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/[a-zA-z0-9~./-]*)\">.*</a>", text)
    #For '' quotations
    urls = urls + re.findall(r"<a href=\'(https?://[a-zA-z0-9~.-]+.[a-zA-z0-9~.-]+/[a-zA-z0-9~./-]*)\'>.*</a>", text)


    return urls

def find_emails(text):
    """
    Looks for and returns what most likely is email addresses in a (long) string.
    An email-like substring is of the form NAME@SERVER.DOMAIN.
    NAME and SERVER can consist of [a-zA-z0-9#$%&~’\*+-/=?_‘|{}.]
    DOMAIN can only consist of alphabetical characters and '.', i.e. [a-zA-Z.], but the first and last
    characters have to be alphabetical. It is (logically) assumed that the DOMAIN name cannot be
    shorter than two characters.
    """

    emails = re.findall(r"[a-zA-z0-9#$%&~’\*+-/=?_‘|{}.]+@[a-zA-z0-9#$%&~’\*+-/=?_‘|{}.]+\.[a-zA-Z][a-zA-z.]*[a-zA-Z]+", text)
    return emails

def all_the_emails(url, depth):
    #website = urllib2.urlopen(url)

    url_req = urlopen(url)
    url_read = url_req.read()
    string = url_read.decode("utf8")
    url_req.close()
    
    print(string)
    return



depth = 5 #Number of times all_the_emails will call itself
url = "https://lucidtech.io/"
all_the_emails(url, depth)


sample_inputs = [
    """
    This is a long string
    without an email address
    It is what it is
    """,
    """
    This string has an email!
    karl@erik.no
    (don't expect replies!)
    """,
    """
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either. 
    """,
    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>
    """,
    """This is text which contains some email-like strings which aren't emails 
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    """
]

expected_outputs = [
    [],
    ["karl@erik.no"],
    ["simon@funke.no", "funsim@uio.no"],
    ["karleh@ifi.uio.no", "karleh@ifi.uio.no"],
    ["na&me@domain.com", "n~ame@dom_ain.com", "name@domain.c_o.uk"]
    
]

"""
print("\nEMAIL SEARCH")
for sample in sample_inputs:
    print(find_emails(sample))
print("Expected outputs:")
for output in expected_outputs:
    print(output)
"""

sample_inputs = [
    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"

    <a href="http://mn.uio.no/ifi/personer/vit/karleh/index.html"></a>
    <a href="https://mn.uio.no/ifi/personer/vit/karleh/index.html"></a>
    <a href="http://www.google.no/"></a>
    <a href='http://www.doorway.no/'></a>
    """,
    
    """
    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>


    
    """,

    
]

expected_outputs = [
    [
        "http://www.mn.uio.no/ifi/personer/vit/karleh/index.html",
    ],
    
    []
    
]

"""
print("\nURL SEARCH")
for sample in sample_inputs:
    print(find_urls(sample))
print("Expected outputs:")
for output in expected_outputs:
    print(output)

"""
